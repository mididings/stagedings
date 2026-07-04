from fastapi import APIRouter, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from scalar_fastapi import get_scalar_api_reference
from stagedings.core.templates import templates
from stagedings.core import config

router = APIRouter()

@router.get("/scalar", include_in_schema=False)
async def scalar_html(request: Request):
    return get_scalar_api_reference(
        # Your OpenAPI document
        openapi_url=request.app.openapi_url,
        # Avoid CORS issues (optional)
        # scalar_proxy_url="https://proxy.scalar.com",
    )

@router.get("/", response_class=HTMLResponse, include_in_schema=False)
async def entry_point(request: Request):
    return templates.TemplateResponse(
        name="ui.html" if request.app.state.controller.scene_controller.scenes else "no_context.html",
        context={
            "request": request,
            "title": config.TITLE,
            "version": config.VERSION,
            "description": config.DESCRIPTION,
        },
        request=request,
    )

# --------------------
# Navigation endpoints
# --------------------
@router.post("/api/scenes/{sceneId}/subscenes/{subsceneId}/activate", 
    description="Switch to the given scene and subscene number.", 
    summary="Switch to the given scene and subscene number.", 
    tags=["Navigation"], responses={204: {"description": "No content"}}
)
async def switch_scene(request: Request,sceneId: int, subsceneId: int):
    await request.app.state.controller.switch_scene(sceneId)
    await request.app.state.controller.switch_subscene(subsceneId)
    return Response(status_code=204)

# -----
@router.post("/api/scenes/{sceneId}/activate", 
    description="Switch to the given scene number.", 
    summary="Switch to the given scene number.", 
    tags=["Navigation"], responses={204: {"description": "No content"}}
)
async def switch_scene(request: Request, sceneId: int):
    await request.app.state.controller.switch_scene(sceneId)
    return Response(status_code=204)

# -----
@router.post("/api/subscenes/{subsceneId}/activate", 
    description="Switch to the given subscene number.", 
    summary="Switch to the given subscene number.", 
    tags=["Navigation"], responses={204: {"description": "No content"}}
)
async def switch_subscene(request: Request, subsceneId: int):
    await request.app.state.controller.switch_subscene(subsceneId)
    return Response(status_code=204)

# -----
@router.post("/api/scenes/prev", description="Switch to the previous scene.",
    summary="Switch to the previous scene.", tags=["Navigation"], responses={204: {"description": "No content"}}
)
async def prev_scene(request: Request):
    await request.app.state.controller.prev_scene()
    return Response(status_code=204)

# -----
@router.post("/api/scenes/next", description="Switch to the next scene.", 
         summary="Switch to the next scene.", tags=["Navigation"], responses={204: {"description": "No content"}}
)
async def next_scene(request: Request):
    await request.app.state.controller.next_scene()
    return Response(status_code=204)

# -----
@router.post("/api/subscenes/prev", description="Switch to the previous subscene.", 
         summary="Switch to the previous subscene.", 
         tags=["Navigation"], responses={204: {"description": "No content"}}
)
async def prev_subscene(request: Request):
    await request.app.state.controller.prev_subscene()
    return Response(status_code=204)

# -----
@router.post("/api/subscenes/next", description="Switch to the next subscene.", 
         summary="Switch to the next subscene.", tags=["Navigation"], responses={204: {"description": "No content"}}
)
async def next_subscene(request: Request):
    await request.app.state.controller.next_subscene()
    return Response(status_code=204)    

# System endpoints
# -----
@router.post("/api/system/panic", description="Send all-notes-off on all channels and on all output ports.", 
         summary="Send all-notes-off on all channels and on all output ports.", 
         tags=["System"], responses={204: {"description": "No content"}})
async def panic(request: Request):
    await request.app.state.controller.panic()
    return Response(status_code=204)

# -----
@router.post("/api/system/quit", description="Terminate mididings.", summary="Terminate mididings.", 
         tags=["System"], responses={204: {"description": "No content"}}
)
async def quit(request: Request):
    await request.app.state.controller.quit()
    return Response(status_code=204)

# -----
@router.post("/api/system/restart", description="Restart mididings.", summary="Restart mididings.", 
         tags=["System"], responses={204: {"description": "No content"}}
)
async def restart(request: Request):
    await request.app.state.controller.restart()
    return Response(status_code=204)

# -----
@router.post("/api/system/query", description="Send config, current scene/subscene to all notify ports.", 
         summary="Send config, current scene/subscene to all notify ports.", 
         tags=["System"], responses={204: {"description": "No content"}}
)
async def query(request: Request):
    await request.app.state.controller.query()
    return Response(status_code=204)