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

def getPlot():
    positions = [0, 1, 2, 3, 4, 5]
    labels = ['2015', '2016', '2017', '2018', '2019', '2020']
    data = [0, 1, 3, 0, 0, 6]
    fiveav = 4/5
    years = np.arange(0, 6, 1)
    fig, ax = plt.subplots()
    ax.plot(years, data, 'r')
    ax.set_xticks(positions)
    ax.set_xticklabels(labels)
    plt.hlines(fiveav, xmin=-0, xmax=5, colors='k', linestyles='dashdot', label='Five Year Average')
    plt.legend(loc='upper right')
    plt.title('Anecdotal lightning strike reports', fontsize=20)
    plt.ylabel('Number of strikes reported', fontsize=14)
    plt.savefig('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/Plots/aneclightningplot.pdf', bbox_inches='tight')
    plt.close()