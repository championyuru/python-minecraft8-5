# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:50:25 2020

@author: SCE
"""

from mcpi.minecraft import Minecraft

mc = Minecraft.create()

while True:
    hits=mc.events.pollBlockHits()
    if len(hits) > 0:
        hit = hits[0]
        x,y,z=hit.pos.x,hit.pos.y,hit.pos.z
        mc.setBlock(x,y,z,41)