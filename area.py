#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 15:47:20 2021

@author: BenButcher
"""
import numpy as np
from pyhdf.SD import *

def getAreaData(filenames):
    """Calculates total area of fire based on number of pixels."""
    centareas = []
    for i in range(0, len(filenames)):
        print('For image '+str(i+1)+':')
        file = filenames[i]  # selects data
        f = SD(file, SDC.READ)
        data = f.select("FireMask")[:,:]
        unique, counts = np.unique(data, return_counts=True)
        pixels = dict(zip(unique, counts))
        total_fire = pixels[7]+pixels[8]+pixels[9]  # total number of fire pixels of any confidence
        cent = round(total_fire*100/pixels[5], 2)
        centareas.append(cent)
        print('Percentage of fire:', cent, '%', '\n')  # calculates fire pixels percentage of land pixels
    return centareas