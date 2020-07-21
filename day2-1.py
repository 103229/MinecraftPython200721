# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 09:04:53 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()


mc.setBlocks(x+20,y+5,z+20,x-20,y+5,z-20,79)
    