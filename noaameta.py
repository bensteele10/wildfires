#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 14:51:18 2021

@author: BenButcher
"""

import sys
sys.path.insert(0, '/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/ip')
from ip import *

"""Input NOAA data filepath"""
noaapath = '/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA Mendocino'

"""Get NOAA filenames"""
noaafiles = noaa.getFilenames(noaapath)

"""Get total precipitation data for August each year"""
precipdata = precip.getData(noaafiles)

"""Get total precipitation plot"""
precip.getPlot(noaafiles, precipdata, noaapath)

"""Get temperature data"""
tmin, tmax, tavg = temps.getData(noaafiles)

"""Get temperature plot"""
temps.getPlot(noaafiles, tmin, tmax, tavg, noaapath)

"""Get evap data"""
#evaps = evap.getData(noaafiles)

"""Get evap plot"""
#evap.getPlot(noaafiles, evaps, noaapath)

"""Get average wind data"""
avwind = wind.getData(noaafiles)

"""Get average wind plot"""
wind.getPlot(noaafiles, avwind, noaapath)

"""Get lightning reports plot"""
#reportdata.getLightningPlot()

"""Get lightning reports plot"""
#reportdata.getStrongWindPlot()

"""Get lightning reports plot"""
#reportdata.getTSWindPlot()