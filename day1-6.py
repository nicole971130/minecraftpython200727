# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 15:30:07 2020

@author: user
"""



from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

a=0
while true:
    mc.postToChat("這是第"+
                  str(a)+"次")
    a=a+1
    time.sleep(1)