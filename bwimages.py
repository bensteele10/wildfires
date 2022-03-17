#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 16:00:17 2021

@author: BenButcher
"""

from matplotlib import pyplot as plt
import matplotlib as mpl
from pyhdf.SD import *
import numpy as np

def getBWImages(filenames):
    
    bwimages = []
    for i in range(0, len(filenames)):  # cycles through files
        file = filenames[i]  # selects data
        f = SD(file, SDC.READ)  # opens data
        data = f.select('FireMask')[:,:]  # selects fire mask
        data = np.where(data==3, 0, data)
        data = np.where(data==4, 0, data)
        data = np.where(data==5, 0, data)
        data = np.where(data==6, 0, data)
        data = np.where(data==7, 1, data)
        data = np.where(data==8, 1, data)
        data = np.where(data==9, 1, data)

        cmap = mpl.colors.LinearSegmentedColormap.from_list('', ['black', 'white'])  # sets a red, green, blue colour map for fire, land, and water

        # plot and save image
        fig = plt.imshow(data, cmap=cmap, interpolation='nearest')
        plt.axis('off')
        fig.axes.get_xaxis().set_visible(False)
        fig.axes.get_yaxis().set_visible(False)
        plt.savefig('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/MOD14A2/bwimage '+str(i+1), bbox_inches='tight', pad_inches = 0)
        bwimages.append('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/MOD14A2/bwimage ' +str(i+1)+'.png')
    return bwimages