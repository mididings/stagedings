#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# SPDX-License-Identifier: GPL-2.0-or-later


'''
    OSC control
'''
from mididings.live.osc_control import LiveOSC


class OscController:
    def __init__(self, control_port, listen_port, scene_controller):

        self.server = LiveOSC(self, control_port, listen_port)

        self.dirty = self.running = False

        self.scene_controller = scene_controller

        self.server.start()
        self.server.query()

    ''' LiveOSC callbacks '''

    '''Data offset'''

    def set_data_offset(self, data_offset):
        self.scene_controller.data_offset = data_offset

    '''Scenes dictionary'''

    def set_scenes(self, scenes):
        self.scene_controller.set_scenes(scenes)

    '''This is the last OSC operation from /query'''

    def set_current_scene(self, scene_id, subscene_id):
        self.scene_controller.set_current_scene(scene_id, subscene_id)
        self.dirty = self.running = True

    def on_start(self):
        ''' Engine start '''
        self.running = True

    def on_exit(self):
        ''' Engine stopped '''
        self.running = False
