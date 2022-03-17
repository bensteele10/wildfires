#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 18:39:45 2021

@author: BenButcher
"""

import sys
sys.path.insert(0, '/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/ip')
from ip import *

filepath = '/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/MOD14A1/2019'

filenames = files.getFilenames(filepath)

images.getBWImages(filenames, filepath)

filepath = '/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/MOD14A1/2018'

filenames = files.getFilenames(filepath)

images.getBWImages(filenames, filepath)

filepath = '/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/MOD14A1/2017'

filenames = files.getFilenames(filepath)

images.getBWImages(filenames, filepath)

filepath = '/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/MOD14A1/2016'

filenames = files.getFilenames(filepath)

images.getBWImages(filenames, filepath)

filepath = '/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/MOD14A1/2015'

filenames = files.getFilenames(filepath)

images.getBWImages(filenames, filepath)