#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 13:14:39 2021

@author: BenButcher
"""
from PIL import Image

def getColourGif(imlist, filepath):
    
    frames = []
    for i in imlist:
        new_frame = Image.open(i)
        frames.append(new_frame)
    frames[0].save(filepath+'daily.gif', format='GIF', append_images=frames[1:], save_all=True, duration=100, loop=0)