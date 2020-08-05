# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:50:25 2020

@author: SCE
"""

from mcpi.minecraft import Minecraft

mc = Minecraft.create()
x,y,z=mc.player.getTilePos()

for i in range(20):
    mc.setBlock(x+i,y-1,z+i+1,1)
    mc.setBlock(x+i,y-1,z+i+2,1)
    mc.setBlock(x+i,y-1,z+i,1)