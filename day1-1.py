# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 11:03:19 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

print(mc.player.getTilePos())