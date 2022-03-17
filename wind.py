#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 18:49:14 2021

@author: BenButcher
"""
import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt

def getData(noaafiles):
    avwind = []
    for i in range(0, len(noaafiles)):
        data = pd.read_csv(noaafiles[i])
        wind = data['AWND']
        w = 0
        d = 0
        for j in range(0, len(wind)):
            if wind[j] == wind[j]:
                w += wind[j]
                d += 1
        avwind.append(w/d)
    return avwind


def getPlot(noaafiles, avwind, noaapath):
    positions = []
    labels = []
    fiveav = 0
    for i in range(0, len(avwind)-1):
        fiveav += avwind[i]
    fiveav = fiveav/5
    for i in range(0, len(noaafiles)):
        positions.append(i)
        n = re.findall(r'NOAA \w+/(\d+).', noaafiles[i])
        labels.append(n[0])
    years = np.arange(0, len(avwind), 1)
    fig, ax = plt.subplots()
    ax.plot(years, avwind, 'rx')
    ax.set_xticks(positions)
    ax.set_xticklabels(labels)
    plt.hlines(fiveav, xmin=-0, xmax=5, colors='k', linestyles=(0, (3, 1, 1, 1)), label='Five Year Average')
    plt.legend(loc='upper right')
    plt.title('Average wind speed each year in August', fontsize=20)
    plt.ylabel('Evaporation', fontsize=14)
    plt.savefig(noaapath+'/Plots/avwindplot.pdf', bbox_inches='tight')
    plt.close()