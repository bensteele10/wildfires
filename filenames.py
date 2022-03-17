#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 11:46:31 2021

@author: BenButcher
"""

import re
import numpy as np
import glob

def getFilenames(directory):
    """ Collects filenames in the directory and sorts them in date order"""

    directory = directory+'/*.hdf'
    filenames = glob.glob(directory)  # gathers hdf filenames
    filenumbers = np.zeros(len(filenames))  # initialise array
    for i in range(0, len(filenames)):
        n = re.findall(r'A2020(\d+).', filenames[i])  # finds the annual ordinal
        filenumbers[i] = int(str(n)[2:-2])
    sort_index = np.argsort(filenumbers)
    filenames = [filenames[i] for i in sort_index]  # sorts according the annual ordinals
    
    return filenames