#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# SPDX-License-Identifier: GPL-2.0-or-later

import os
import json
import asyncio
import uvicorn
import argparse
from pathlib import Path
from importlib import resources
from contextlib import asynccontextmanager
import stagedings

from stagedings.core.control import Controller
from stagedings.core.connection import ConnectionManager

from fastapi import Request, FastAPI, WebSocket, WebSocketDisconnect, Response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.openapi.utils import get_openapi
from scalar_fastapi import get_scalar_api_reference

BASE_DIR = Path(stagedings.__file__).resolve().parent

description = """
### You will be able to:

* **Navigating Scenes and Subscenes**
* **Control mididings**
"""
title = "stagedings"
version = "0.1.2"

@asynccontextmanager
async def lifespan(app: FastAPI):
    controller = Controller(app.state.control_port,app.state.listen_port)
    delegates = build_delegates(controller)
    
    app.state.controller = controller
    app.state.delegates = delegates

    yield  # >>> app runs here (WS + API active)

    # --- SHUTDOWN PHASE ---
    # optional cleanup
    
app = FastAPI(lifespan=lifespan)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    app.openapi_schema = get_openapi(
        title=title,
        version=version,
        description=description,
        routes=app.routes,
        openapi_version="3.1.0",
        summary="An UI and API for mididings community version"
    )
    app.openapi_schema["info"]["x-logo"] = {
        "url": "https://avatars.githubusercontent.com/u/121540801?s=400&u=2d3daf12927631aecd807b2d6dfb90652cc22ae8&v=4"
    }
    return app.openapi_schema

app.openapi = custom_openapi    


"""  Configuration """

app.mount(
    "/static",
    StaticFiles(directory=str(BASE_DIR / "static")),
    name="static"
)
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# WebSocket connection manager
connection_manager = ConnectionManager()

async def mididings_context_update():
    await app.state.controller.set_dirty(False)
    await connection_manager.broadcast(
        {"action": "mididings_context_update", "payload": app.state.controller.scene_controller.payload}
    )

# UI enpoints
@app.get("/scalar", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
        # Your OpenAPI document
        openapi_url=app.openapi_url,
        # Avoid CORS issues (optional)
        # scalar_proxy_url="https://proxy.scalar.com",
    )


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def entry_point(request: Request):
    return templates.TemplateResponse(
        name="ui.html" if request.app.state.controller.scene_controller.scenes else "no_context.html",
        context={
            "request": request,
            "title": title,
            "version": version,
        },
        request=request,
    )

# Navigation endpoints
# -----
@app.post("/api/scenes/{sceneId}/subscenes/{subsceneId}/activate", 
    description="Switch to the given scene and subscene number.", 
    summary="Switch to the given scene and subscene number.", 
    tags=["Navigation"], responses={204: {"description": "No content"}}
)
async def switch_scene(request: Request,sceneId: int, subsceneId: int):
    await request.app.state.controller.switch_scene(sceneId)
    await request.app.state.controller.switch_subscene(subsceneId)
    return Response(status_code=204)

# -----
@app.post("/api/scenes/{sceneId}/activate", 
    description="Switch to the given scene number.", 
    summary="Switch to the given scene number.", 
    tags=["Navigation"], responses={204: {"description": "No content"}}
)
async def switch_scene(request: Request, sceneId: int):
    await request.app.state.controller.switch_scene(sceneId)
    return Response(status_code=204)

# -----
@app.post("/api/subscenes/{subsceneId}/activate", 
    description="Switch to the given subscene number.", 
    summary="Switch to the given subscene number.", 
    tags=["Navigation"], responses={204: {"description": "No content"}}
)
async def switch_subscene(request: Request, subsceneId: int):
    await request.app.state.controller.switch_subscene(subsceneId)
    return Response(status_code=204)

# -----
@app.post("/api/scenes/prev", description="Switch to the previous scene.",
    summary="Switch to the previous scene.", tags=["Navigation"], responses={204: {"description": "No content"}}
)
async def prev_scene(request: Request):
    await request.app.state.controller.prev_scene()
    return Response(status_code=204)

# -----
@app.post("/api/scenes/next", description="Switch to the next scene.", 
         summary="Switch to the next scene.", tags=["Navigation"], responses={204: {"description": "No content"}}
)
async def next_scene(request: Request):
    await request.app.state.controller.next_scene()
    return Response(status_code=204)

# -----
@app.post("/api/subscenes/prev", description="Switch to the previous subscene.", 
         summary="Switch to the previous subscene.", 
         tags=["Navigation"], responses={204: {"description": "No content"}}
)
async def prev_subscene(request: Request):
    await request.app.state.controller.prev_subscene()
    return Response(status_code=204)

# -----
@app.post("/api/subscenes/next", description="Switch to the next subscene.", 
         summary="Switch to the next subscene.", tags=["Navigation"], responses={204: {"description": "No content"}}
)
async def next_subscene(request: Request):
    await request.app.state.controller.next_subscene()
    return Response(status_code=204)    

# System endpoints
# -----
@app.post("/api/system/panic", description="Send all-notes-off on all channels and on all output ports.", 
         summary="Send all-notes-off on all channels and on all output ports.", 
         tags=["System"], responses={204: {"description": "No content"}})
async def panic(request: Request):
    await request.app.state.controller.panic()
    return Response(status_code=204)

# -----
@app.post("/api/system/quit", description="Terminate mididings.", summary="Terminate mididings.", 
         tags=["System"], responses={204: {"description": "No content"}}
)
async def quit(request: Request):
    await request.app.state.controller.quit()
    return Response(status_code=204)

# -----
@app.post("/api/system/restart", description="Restart mididings.", summary="Restart mididings.", 
         tags=["System"], responses={204: {"description": "No content"}}
)
async def restart(request: Request):
    await request.app.state.controller.restart()
    return Response(status_code=204)

# -----
@app.post("/api/system/query", description="Send config, current scene/subscene to all notify ports.", 
         summary="Send config, current scene/subscene to all notify ports.", 
         tags=["System"], responses={204: {"description": "No content"}}
)
async def query(request: Request):
    await request.app.state.controller.query()
    return Response(status_code=204)

""" Websocket handler """


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await connection_manager.connect(websocket)
    last_running_state = None
    stop_event = asyncio.Event()

    async def receive_loop():
        try:
            while websocket in connection_manager.active_connections:
                data = await websocket.receive_json()
                action = data.get("action")
                if action in app.state.delegates:
                    if "id" in data:
                        await app.state.delegates[action](int(data["id"]))
                    else:
                        await app.state.delegates[action]()
        except WebSocketDisconnect:
            pass
        except Exception as exc:
            print(f"WebSocket receive error: {exc}")
        finally:
            stop_event.set()

    async def monitor_loop():
        nonlocal last_running_state
        while not stop_event.is_set() and websocket in connection_manager.active_connections:
            current_running = await app.state.controller.is_running()
            if last_running_state is None or current_running != last_running_state:
                await connection_manager.broadcast(
                    {"action": "on_start" if current_running else "on_exit"}
                )
                last_running_state = current_running

            if await app.state.controller.is_dirty():
                await app.state.delegates["mididings_context_update"]()

            await asyncio.sleep(0.1)

    receiver_task = asyncio.create_task(receive_loop())
    monitor_task = asyncio.create_task(monitor_loop())

    try:
        await asyncio.gather(receiver_task, monitor_task)
    finally:
        stop_event.set()
        receiver_task.cancel()
        monitor_task.cancel()
        await asyncio.gather(receiver_task, monitor_task, return_exceptions=True)
        connection_manager.disconnect(websocket)


async def on_connect(websocket: WebSocket = None):
    await app.state.controller.set_dirty(True)

def build_delegates(controller: Controller):
    return {

        "on_connect": on_connect,

        "quit": controller.quit,
        "panic": controller.panic,
        "query": controller.query,
        "restart": controller.restart,

        "next_scene": controller.next_scene,
        "prev_scene": controller.prev_scene,
        "next_subscene": controller.next_subscene,
        "prev_subscene": controller.prev_subscene,

        "switch_scene": controller.switch_scene,
        "switch_subscene": controller.switch_subscene,

        "mididings_context_update": mididings_context_update,
    }

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