#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# SPDX-License-Identifier: GPL-2.0-or-later

from fastapi import  WebSocket
from typing import List

class ConnectionManager:
    def __init__(self, controller):
        self.active_connections: List[WebSocket] = []
        self.controller = controller
        self.last_running_state = None

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        if websocket not in self.active_connections:
            print(f"Connecting: {websocket.client}")
            self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            print(f"Disconnecting: {websocket.client}")
        try:
            self.active_connections.remove(websocket)
        except:
            pass

    async def broadcast(self, message: dict):
        for websocket in self.active_connections[:]:
            try:
                await websocket.send_json(message)
            except Exception as e:
                print(f"WebSocket error: {e} for {websocket.client}")
                self.disconnect(websocket)
                
    async def publish_mididings_context(self, websocket: WebSocket = None):
        if not websocket in self.active_connections:
            return
        await self.publish_mididings_state()
        if await self.controller.is_dirty():
            await self.controller.set_dirty(False)
            await self.broadcast(
                {"action": "mididings_context_update", "payload": self.controller.scene_controller.payload}
        )
            
    async def publish_mididings_state(self):
        current_running = await self.controller.is_running()
        if self.last_running_state is None or current_running != self.last_running_state:
            await self.broadcast(
                {"action": "on_start" if current_running else "on_exit"}
            )
            self.last_running_state = current_running
