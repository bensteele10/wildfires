#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 17:38:26 2021

@author: BenButcher
"""
import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt

def getData(noaafiles):
    evaps = []
    for i in range(0, len(noaafiles)):
        data = pd.read_csv(noaafiles[i])
        ev = data['EVAP']
        e = 0
        d = 0
        for j in range(0, len(ev)):
            if ev[j] == ev[j]:
                e += ev[j]
                d += 1
        evaps.append(e/d)
    return evaps


def getPlot(noaafiles, evaps, noaapath):
    positions = []
    labels = []
    fiveav = 0
    for i in range(0, len(evaps)-1):
        fiveav += evaps[i]
    fiveav = fiveav/5
    for i in range(0, len(noaafiles)):
        positions.append(i)
        n = re.findall(r'NOAA \w+/(\d+).', noaafiles[i])
        labels.append(n[0])
    years = np.arange(0, len(evaps), 1)
    fig, ax = plt.subplots()
    ax.plot(years, evaps, 'rx')
    ax.set_xticks(positions)
    ax.set_xticklabels(labels)
    plt.hlines(fiveav, xmin=-0, xmax=5, colors='k', linestyles=(0, (3, 1, 1, 1)), label='Five Year Average')
    plt.legend(loc='upper right')
    plt.title('Pan evaporation each year in August', fontsize=20)
    plt.ylabel('Evaporation', fontsize=14)
    plt.savefig(noaapath+'/Plots/evapplot.pdf', bbox_inches='tight')
    plt.close()