#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# SPDX-License-Identifier: GPL-2.0-or-later

import uvicorn
import argparse
from contextlib import asynccontextmanager

import stagedings
from stagedings.core.control import Orchestrator
from stagedings.core.ws_manager import ConnectionManager
from stagedings.api import rest, ws
from stagedings.core.paths import STATIC_DIR
from stagedings.core import config

from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.utils import get_openapi

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.controller = Orchestrator(app.state.control_port,app.state.listen_port)
    app.state.ws_manager = ConnectionManager(app.state.controller)
    
    yield  # >>> app runs here (WS + API active)

    # --- SHUTDOWN PHASE ---
    # optional cleanup
    
app = FastAPI(lifespan=lifespan)

app.include_router(rest.router)
app.include_router(ws.router)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    app.openapi_schema = get_openapi(
        title=config.TITLE,
        version=config.VERSION,
        description=config.DESCRIPTION,
        routes=app.routes,
        summary="An UI and API for mididings community version"
    )
    app.openapi_schema["info"]["x-logo"] = {
        "url": "https://avatars.githubusercontent.com/u/121540801?s=400&u=2d3daf12927631aecd807b2d6dfb90652cc22ae8&v=4"
    }
    return app.openapi_schema

app.openapi = custom_openapi    


"""  Configuration """

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

def main():
    parser = argparse.ArgumentParser(description="Run stagedings FastAPI server", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        "--host",
        default="localhost",
        help="FastAPI listen host",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=5000,
        help="FastAPI listen port",
    )
    
    parser.add_argument(
        "--control-port",
        type=int,
        default=56418,
        help="OSC port where mididings listens for commands.",
    )

    parser.add_argument(
        "--listen-port",
        type=int,
        default=56419,
        help="OSC port where stagedings listens for notifications from mididings.",
    )

    args = parser.parse_args()
    
    # pass config via uvicorn
    app.state.control_port = args.control_port
    app.state.listen_port = args.listen_port

    uvicorn.run(
        "stagedings.cli:app",
        host=args.host,
        port=args.port,
    )