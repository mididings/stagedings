import asyncio

from fastapi import APIRouter, Request, WebSocket, WebSocketDisconnect

router = APIRouter()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    ws_manager: ConnectionManager = websocket.app.state.ws_manager
    await ws_manager.connect(websocket)
    stop_event = asyncio.Event()

    async def receive_loop():
        try:
            while websocket in ws_manager.active_connections:
                data = await websocket.receive_json()
                action = data.get("action")
                scene_id = int(data["id"]) if "id" in data else None 
                await ws_manager.controller.execute(action, scene_id)
        except WebSocketDisconnect:
            pass
        except Exception as exc:
            print(f"WebSocket receive error: {exc}")
        finally:
            stop_event.set()

    async def monitor_loop():
        while not stop_event.is_set():
            await ws_manager.publish_mididings_context(websocket)
            await asyncio.sleep(0.125)

    receiver_task = asyncio.create_task(receive_loop())
    monitor_task = asyncio.create_task(monitor_loop())

    try:
        await asyncio.gather(receiver_task, monitor_task)
    finally:
        stop_event.set()
        receiver_task.cancel()
        monitor_task.cancel()
        await asyncio.gather(receiver_task, monitor_task, return_exceptions=True)
        ws_manager.disconnect(websocket)