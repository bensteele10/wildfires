#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 15:25:03 2021

@author: BenButcher
"""
import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt

def getData(noaafiles):
    tmin = []
    tmax = []
    tavg = []
    for i in range(0, len(noaafiles)):
        data = pd.read_csv(noaafiles[i])
        mint = data['TMIN']
        maxt = data['TMAX']
        avgt = data['TAVG']
        a = 0
        b = 0
        c = 0
        da = 0
        db = 0
        dc = 0
        for j in range(0, len(data)):
            if mint[j] == mint[j]:
                a += mint[j]
                da += 1
            if maxt[j] == maxt[j]:
                b += maxt[j]
                db += 1
            if avgt[j] == avgt[j]:
                c += avgt[j]
                dc += 1
        tmin.append(a/da)
        tmax.append(b/db)
        tavg.append(c/dc)
    return tmin, tmax, tavg


def getPlot(noaafiles, tmin, tmax, tavg, noaapath):
    positions = []
    labels = []
    fiveavmin = 0
    fiveavmax = 0
    fiveavavg = 0
    for i in range(0, len(tmin)-1):
        fiveavmin += tmin[i]
        fiveavmax += tmax[i]
        fiveavavg += tavg[i]
    fiveavmin = fiveavmin/5
    fiveavmax = fiveavmax/5
    fiveavavg = fiveavavg/5
    for i in range(0, len(noaafiles)):
        positions.append(i)
        n = re.findall(r'NOAA \w+/(\d+).', noaafiles[i])
        labels.append(n[0])
    years = np.arange(0, len(noaafiles), 1)
    fig, ax = plt.subplots()
    ax.plot(years, tmax, 'rx', label='Tmax')
    ax.plot(years, tavg, 'gx', label='Tavg')
    ax.plot(years, tmin, 'bx', label='Tmin')
    ax.set_xticks(positions)
    ax.set_xticklabels(labels)
    plt.hlines(fiveavmin, xmin=-0, xmax=5, colors='k', linestyles=(0, (3, 1, 1, 1)), label='Five Year Average')
    plt.hlines(fiveavmax, xmin=-0, xmax=5, colors='k', linestyles=(0, (3, 1, 1, 1)))
    plt.hlines(fiveavavg, xmin=-0, xmax=5, colors='k', linestyles=(0, (3, 1, 1, 1)))
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.title('Temperates each year in August', fontsize=20)
    plt.ylabel('Temperature', fontsize=14)
    plt.savefig(noaapath+'/Plots/tempplot.pdf', bbox_inches='tight')
    plt.close()