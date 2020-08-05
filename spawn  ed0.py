# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:50:25 2020

@author: SCE
"""

from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x,y,z=mc.player.getTilePos()
mc.spawnEntity(x,y,z,63)