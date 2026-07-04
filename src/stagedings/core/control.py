#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# SPDX-License-Identifier: GPL-2.0-or-later

'''
    The Orchestrator, handling scene changes and osc communication with mididings.
'''


from .osc import OscController
from .scene import SceneController

class Orchestrator:
    def __init__(self, control_port, listen_port) -> None:
        self.scene_controller = SceneController()
        self.osc_controller = OscController(control_port, listen_port, self.scene_controller)

    async def is_dirty(self):
        return self.osc_controller.dirty

    async def set_dirty(self, value):
        self.osc_controller.dirty = value

    async def is_running(self):
        return self.osc_controller.running

    async def next_scene(self):
        self.osc_controller.server.next_scene()

    async def next_subscene(self):
        self.osc_controller.server.next_subscene()

    async def prev_scene(self):
        self.osc_controller.server.prev_scene()

    async def prev_subscene(self):
        self.osc_controller.server.prev_subscene()

    async def panic(self):
        self.osc_controller.server.panic()

    async def restart(self):
        self.osc_controller.server.restart()

    async def query(self):
        self.osc_controller.server.query()

    async def quit(self):
        self.osc_controller.server.quit()

    async def switch_scene(self, value):
        self.osc_controller.server.switch_scene(value)

    async def switch_subscene(self, value):
        self.osc_controller.server.switch_subscene(value)

    async def on_connect(self):
        await self.set_dirty(True)
        
    async def execute(self, action = None, id = None):
        if action == "next_scene":
            await self.next_scene()
        elif action == "prev_scene":
            await self.prev_scene()
        elif action == "next_subscene":
            await self.next_subscene()
        elif action == "prev_subscene":
            await self.prev_subscene()
        elif action == "panic":
            await self.panic()
        elif action == "restart":
            await self.restart()
        elif action == "query":
            await self.query()
        elif action == "quit":
            await self.quit()
        elif action == "switch_scene" and id is not None:
            await self.switch_scene(id)
        elif action == "switch_subscene" and id is not None:
            await self.switch_subscene(id)
        elif action == "on_connect":
            await self.on_connect()
        else:
            print(f"Unknown action: {action} with id: {id}")
        
