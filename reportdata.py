#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 14:39:25 2021

@author: BenButcher
"""

import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt

def getLightningPlot():
    x = ['2015', '2016', '2017', '2018', '2019', '2020']
    x_pos = [0, 1, 2, 3, 4, 5]
    data = [0, 1, 3, 0, 0, 6]
    plt.bar(x_pos, data, color='black')
    plt.xticks(x_pos, x)
    plt.title('Anecdotal Lightning Reports in August Each Year', fontsize=20)
    plt.ylabel('Number of reports', fontsize=14)
    plt.savefig('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/Plots/anec/lightningplot.pdf', bbox_inches='tight')
    plt.close()
    
    
def getStrongWindPlot():
    x = ['2015', '2016', '2017', '2018', '2019', '2020']
    x_pos = [0, 1, 2, 3, 4, 5]
    data = [0, 0, 0, 0, 0, 4]
    plt.bar(x_pos, data, color='black')
    plt.xticks(x_pos, x)
    plt.title('Anecdotal Strong Wind Reports in August Each Year', fontsize=20)
    plt.ylabel('Number of reports', fontsize=14)
    plt.savefig('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/Plots/anec/strongwindplot.pdf', bbox_inches='tight')
    plt.close()

    
    
def getTSWindPlot():
    x = ['2015', '2016', '2017', '2018', '2019', '2020']
    x_pos = [0, 1, 2, 3, 4, 5]
    data = [1, 2, 13, 5, 2, 16]
    plt.bar(x_pos, data, color='black')
    plt.xticks(x_pos, x)
    plt.title('Anecdotal thunderstorm wind Reports in August Each Year', fontsize=20)
    plt.ylabel('Number of reports', fontsize=14)
    plt.savefig('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/Plots/anec/tswindplot.pdf', bbox_inches='tight')
    plt.close()