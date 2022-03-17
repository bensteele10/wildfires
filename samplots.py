#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 17:07:51 2021

@author: BenButcher
"""

import seaborn as sns
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#import matplotlib.ticker as ticker
from datetime import date
import networkx as nx
from mpl_toolkits.axes_grid1 import make_axes_locatable

d0 = date(2019, 12, 27)
d1 = date(2020, 1, 1)
d2 = date(2020, 2, 1)
d3 = date(2020, 3, 1)
d4 = date(2020, 4, 1)
d5 = date(2020, 5, 1)
d6 = date(2020, 6, 1)
d7 = date(2020, 7, 1)
d8 = date(2020, 8, 1)
d9 = date(2020, 9, 1)
d10 = date(2020, 10, 1)
d11 = date(2020, 11, 1)
d12 = date(2020, 12, 1)
d13 = date(2021, 1, 1)

delta = d1-d0
jan = delta.days
delta = d2-d0
feb = delta.days
delta = d3-d0
mar = delta.days
delta = d4-d0
apr = delta.days
delta = d5-d0
may = delta.days
delta = d6-d0
jun = delta.days
delta = d7-d0
jul = delta.days
delta = d8-d0
aug = delta.days
delta = d9-d0
sep = delta.days
delta = d10-d0
octo = delta.days
delta = d11-d0
nov = delta.days
delta = d12-d0
dec = delta.days
delta = d13-d0
njan = delta.days

positions = [jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec, njan]
positions = np.array(positions)
positions = positions-jan
hals = np.zeros(len(positions)-1)
for i in range(0, len(positions)-1):
    hals[i] = (positions[i]+positions[i+1])/2
labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

netpositions = [aug, sep, octo]
nethals = [(aug+sep)/2, (sep+octo)/2]
netlabels = ['August', 'September']

front = [0, 0, 0, 0, 0, 5]
end = [2, 2, 2, 2, 2, 5]

def getSamAreaCountPlot(allareacount, filepath='/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/MOD14A1/2020'):
    sns.set_style('darkgrid')
    days = np.arange(0, 366, 1)
    fig, ax = plt.subplots(figsize=(20,10))
    ax.plot(days, allareacount[5][3][front[5]:-end[5]], color='red', label='2020')
    fiveav = np.zeros(len(allareacount[0][0]))
    for i in range(0, len(allareacount[0])-1):
        #ax.plot(days, allareacount[i][3][front[i]:-end[i]], color='blue')
        a = np.array(allareacount[i][3])
        fiveav += a
    fiveav = fiveav/5
    fiveav = fiveav[front[0]:-end[0]]
    ax.plot(days, fiveav, color='black', label='Five Year Average')
    ax.set_xticks(positions)
    ax.set_xticks(hals, minor=True)
    ax.set_xticklabels([])
    ax.set_xticklabels(labels, minor=True)
    ax.tick_params(axis='x', which='minor', length=0)
    plt.title('Total Fire Area', fontsize=20)
    plt.ylabel('Area [km$^2$]', fontsize=14)
    plt.legend(loc='upper right')
    plt.savefig(filepath+'/Plots/samareacountplot.pdf', bbox_inches='tight')
    plt.close()
    
    
getAreaCountPlot(allareacount, filepath)
getAreaRollAvPlot(allareacount, filepath)
getAreaRollAvCompPlot(allareacount, filepath)
getAreaRollAvCompFilledPlot(allareacount, filepath)
getAreaRollAvSumPlot(allareacount, filepath)
getAreaCountStem(allareacount, filepath)
getAreaCountTypePlot(allareacount, filepath)
getCumulativeCountPlot(allcarea, filepath)
getMeanAreaPlot(allareacount, allfirecount, filepath)
getMeanAreaRollAvPlot(allareacount, allfirecount, filepath)
getMeanAreaRollAvCompPlot(allareacount, allfirecount, filepath)
getFiresPlot(allfirecount, filepath)
getFiresCountPlot(allfiresets, filepath)
getFiresRollAvPlot(allfirecount, filepath)
getFiresRollAvCompPlot(allfirecount, filepath)
getFireandAreaPlot(allareacount, allfirecount, filepath)
getComplexFiresPlot(allclustercount, filepath)
getFireTypePlot(allclustercount, allfirecount, filepath)
getFireTypeFilledPlot(allclustercount, allfirecount, filepath)
plotLines(flts, allfiresets, filepath)
plotAugLines(flts, allfiresets, filepath)
getVCountPlot(vdata)
getAreaRollAvLightningPlot(allareacount, vdata, filepath)
getFiresLightningPlot(allfiresets, vdata, filepath)
getGCLightningPlot(vdata, filepath)
getFiresDerivPlot(allfiresets, vdata, filepath)
plotLinesLightning(lifetimes, vdata, filepath)
getNetworkPlot(allfirecount, allfiresets, allareacount, filepath)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    