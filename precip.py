#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 14:57:19 2021

@author: BenButcher
"""

import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt

def getData(noaafiles):
    precipdata = []
    for i in range(0, len(noaafiles)):
        data = pd.read_csv(noaafiles[i])
        prcp = data['PRCP']
        p = 0
        d = 0
        for j in range(0, len(prcp)):
            if prcp[j] == prcp[j]:
                p += prcp[j]
                d += 1
        precipdata.append(p/d)
    return precipdata


def getPlot(noaafiles, precipdata, noaapath):
    x = []
    x_pos = []
    for i in range(0, len(precipdata)):
        x_pos.append(i)
        n = re.findall(r'NOAA \w+/(\d+).', noaafiles[i])
        x.append(n[0])
    plt.bar(x_pos, precipdata, color='blue')
    plt.xticks(x_pos, x)
    plt.title('Total Precipitation in August Each Year', fontsize=20)
    plt.ylabel('Precipitation', fontsize=14)
    plt.savefig(noaapath+'/Plots/precipplot.pdf', bbox_inches='tight')
    plt.close()