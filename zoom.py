#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 21:33:03 2021

@author: BenButcher
"""

from pyhdf.SD import *
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def getClusterImages(filenames, firedata):
    """Generates zoomed images of each cluster in each hdf file"""
    
    for i in range(0, len(filenames)):  # cycles through files
            file = filenames[i]  # selects data
            f = SD(file, SDC.READ)  # opens data
            data = f.select('FireMask')[:,:]  # selects fire mask
            
            data = np.where(data==3, 1, data)
            data = np.where(data==4, 0, data)
            data = np.where(data==5, 2, data)
            data = np.where(data==6, 0, data)
            data = np.where(data==7, 3, data)
            data = np.where(data==8, 3, data)
            data = np.where(data==9, 3, data)

            cmap = mpl.colors.LinearSegmentedColormap.from_list('', ['white', '#0000A0', '#347C2C', '#E41B17'])  # sets a red, green, blue colour map
            
            # plot and save image
            for n in range(0, len(firedata[i+1])):
                fig = plt.imshow(data, cmap=cmap, interpolation='nearest')
                x = (firedata[i+1][n][0][0])
                y = (firedata[i+1][n][0][1])
                plt.xlim(x-50,x+50)
                plt.ylim(y+50,y-50)
                plt.axis('off')
                fig.axes.get_xaxis().set_visible(False)
                fig.axes.get_yaxis().set_visible(False)
                plt.savefig('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/MOD14A2/image '+str(i+1)+', cluster '+str(n+1), bbox_inches='tight', pad_inches = 0)
                
                
def getIndividual(filenames, firedata, image, fire, z=50):
    """Generates image for specific cluster"""
    
    (a, b) = np.divmod(image, 8)
    c = b.item()
    file = filenames[a]
    f = SD(file, SDC.READ)
    data = f.select('FireMask')[c-1,:,:]
    
    data = np.where(data==3, 1, data)
    data = np.where(data==4, 0, data)
    data = np.where(data==5, 2, data)
    data = np.where(data==6, 0, data)
    data = np.where(data==7, 3, data)
    data = np.where(data==8, 3, data)
    data = np.where(data==9, 3, data)
    
    cmap = mpl.colors.LinearSegmentedColormap.from_list('', ['white', '#0000A0', '#347C2C', '#E41B17'])  # sets a red, green, blue colour map
    
    fig = plt.imshow(data, cmap=cmap, interpolation='nearest')
    x = (firedata[image][fire-1][0][0])
    y = (firedata[image][fire-1][0][1])
    plt.xlim(x-z,x+z)
    plt.ylim(y+z,y-z)
    plt.axis('off')
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    plt.show()
    #plt.savefig('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/MOD14A2/image '+str(image)+', cluster '+str(cluster), bbox_inches='tight', pad_inches = 0)
     