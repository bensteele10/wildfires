#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 14:29:55 2021

@author: BenButcher
"""

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#import matplotlib.ticker as ticker
from datetime import date
import networkx as nx
#from mpl_toolkits.axes_grid1 import make_axes_locatable
import seaborn as sns
#from matplotlib import rc
import pandas as pd
from sklearn import preprocessing
from scipy.stats import pearsonr
from sklearn.decomposition import PCA
from matplotlib.patches import Rectangle

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
labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

netpositions = [aug, sep, octo]
nethals = [(aug+sep)/2, (sep+octo)/2]
netlabels = ['August', 'September']

noaapositions = [jul, aug, sep, octo]
noaahals = [(jul+aug)/2, (aug+sep)/2, (sep+octo)/2]
noaalabels = ['July', 'August', 'September']

front = [0, 0, 0, 0, 0, 5]
end = [2, 2, 2, 2, 2, 5]

matplotlib.rcParams.update(matplotlib.rcParamsDefault)
sns.set_style('darkgrid')
matplotlib.rcParams['lines.linewidth'] = 1

green = '#07c40d'
lightgreen = '#00dc00'
darkgreen = '#008a00'

"""
def getTestPlot(dayarea, filepath):
    areas = np.zeros(len(dayarea))
    days = np.arange(0, len(dayarea), 1)
    for i in range(0, len(dayarea)):
        areas[i] = dayarea[i+1]
    fig, ax = plt.subplots()
    ax.plot(days, areas, 'r')
    ax.set_xticks(positions)
    ax.set_xticks(hals, minor=True)
    ax.set_xticklabels([])
    ax.set_xticklabels(labels, minor=True)
    ax.tick_params(axis='x', which='minor', length=0)
    plt.title('Total Number of Fires', fontsize=20)
    plt.xlabel('Days', fontsize=14)
    plt.ylabel('Area [km$^2$]', fontsize=14)
    plt.show()


def getTotalAreaPlot(alldayarea, filepath):
    allareas = []
    days = np.arange(0, 366, 1)
    for i in range(0, len(alldayarea)):
        areas = np.zeros(len(alldayarea[i])//2)
        for j in range(1, (len(alldayarea[i])//2)+1):
            try:
                areas[j-1] = alldayarea[i][2*j]+alldayarea[i][2*j-1]
            except KeyError:
                areas[j-1] = alldayarea[i][str(2*j)]+alldayarea[i][str(2*j-1)]
        areas = areas[front[i]:-end[i]]
        allareas.append(areas)
    avarea = np.zeros(366)
    for i in range(0, len(allareas)-1):
        avarea += allareas[i]
    avarea = avarea/(len(alldayarea)-1)
    fig, ax = plt.subplots(figsize=(20,10))
    ax.plot(days, allareas[(len(alldayarea)-1)], 'r', label='2020')
    ax.plot(days, avarea, 'k', label='Five Year Average')
    #ax.plot(days, allareas[0], 'b')
    #ax.plot(days, allareas[1], 'g')
    ax.set_xticks(positions)
    ax.set_xticks(hals, minor=True)
    ax.set_xticklabels([])
    ax.set_xticklabels(labels, minor=True)
    ax.tick_params(axis='x', which='minor', length=0)
    plt.title('Total Fire Area', fontsize=20)
    plt.ylabel('Area [km$^2$]', fontsize=14)
    plt.legend(loc='upper right')
    plt.savefig(filepath+'/Plots/totalareaplot.pdf', bbox_inches='tight')
    plt.close()
"""   
    
def getAreaCountPlot(allareacount, filepath):
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
    ax.vlines(sep+6, 0, 4500)
    plt.ylabel('Area [km$^2$]', fontsize=14)
    plt.legend(loc='upper right')
    plt.title('Total Fire Area', fontsize=20)
    plt.savefig(filepath+'/Plots/areacountplot.pdf', bbox_inches='tight')
    plt.close()
    
    
def getAreaRollAvPlot(allareacount, filepath):
    days = np.arange(0, 366, 1)
    fig, ax = plt.subplots(figsize=(20,10))
    a = allareacount[5][3][front[5]:-end[5]]
    ax.plot(days, a, color='red', label='Signal')
    rollav = np.zeros(len(a)-14)
    for i in range(7, len(a)-7):
        av = 0
        for j in range(1, 8):
            av += a[i-j]+a[i+j]
        rollav[i-7] = (av+a[i])/15
    ax.plot(days[7:-7], rollav, color='black', label='15 day rolling average')
    fiveav = np.zeros(len(allareacount[0][0]))
    for i in range(0, len(allareacount[0])-1):
        #ax.plot(days, allareacount[i][3][front[i]:-end[i]], color='blue')
        a = np.array(allareacount[i][3])
        fiveav += a
    fiveav = fiveav/5
    fiveav = fiveav[front[0]:-end[0]]
    #ax.plot(days, fiveav, color='black', label='Five Year Average')
    ax.set_xticks(positions)
    ax.set_xticks(hals, minor=True)
    ax.set_xticklabels([])
    ax.set_xticklabels(labels, minor=True)
    ax.tick_params(axis='x', which='minor', length=0)
    plt.title('Total Fire Area', fontsize=20)
    plt.ylabel('Area [km$^2$]', fontsize=14)
    plt.legend(loc='upper right')
    plt.savefig(filepath+'/Plots/arearollavplot.pdf', bbox_inches='tight')
    plt.close()
    
    
def getJointAreaCountPlot(allareacount, filepath):
    days = np.arange(0, 366, 1)
    fig, ax = plt.subplots(2, figsize=(20,10))
    ax[0].plot(days, allareacount[5][3][front[5]:-end[5]], color='red', label='2020')
    fiveav = np.zeros(len(allareacount[0][0]))
    for i in range(0, len(allareacount[0])-1):
        #ax.plot(days, allareacount[i][3][front[i]:-end[i]], color='blue')
        a = np.array(allareacount[i][3])
        fiveav += a
    fiveav = fiveav/5
    fiveav = fiveav[front[0]:-end[0]]
    ax[0].plot(days, fiveav, color='black', label='Five Year Average')
    ax[0].set_xticks(positions)
    ax[0].set_xticks(hals, minor=True)
    ax[0].set_xticklabels([])
    ax[0].set_xticklabels(labels, minor=True)
    ax[0].tick_params(axis='x', which='minor', length=0)
    ax[0].set_ylabel('Area [km$^2$]', fontsize=14)
    ax[0].legend(loc='upper right')
    a = allareacount[5][3][front[5]:-end[5]]
    ax[1].plot(days, a, color='red', label='Signal')
    rollav = np.zeros(len(a)-14)
    for i in range(7, len(a)-7):
        av = 0
        for j in range(1, 8):
            av += a[i-j]+a[i+j]
        rollav[i-7] = (av+a[i])/15
    ax[1].plot(days[7:-7], rollav, color='black', label='15 day rolling average')
    fiveav = np.zeros(len(allareacount[0][0]))
    for i in range(0, len(allareacount[0])-1):
        #ax.plot(days, allareacount[i][3][front[i]:-end[i]], color='blue')
        a = np.array(allareacount[i][3])
        fiveav += a
    fiveav = fiveav/5
    fiveav = fiveav[front[0]:-end[0]]
    ax[1].set_xticks(positions)
    ax[1].set_xticks(hals, minor=True)
    ax[1].set_xticklabels([])
    ax[1].set_xticklabels(labels, minor=True)
    ax[1].tick_params(axis='x', which='minor', length=0)
    ax[1].set_ylabel('Area [km$^2$]', fontsize=14)
    ax[1].legend(loc='upper right')
    plt.suptitle('Total Fire Area', fontsize=20)
    plt.savefig(filepath+'/Plots/jointareacountplot.pdf', bbox_inches='tight')
    plt.close()
    
    
def getAreaRollAvCompPlot(allareacount, filepath):
    days = np.arange(0, 366, 1)
    fig, ax = plt.subplots(figsize=(8,5))
    rollavs = np.zeros(len(allareacount[0][3][front[0]:-end[0]])-14)
    for i in range(0, len(allareacount)-2):
        a = np.array(allareacount[i][3][front[i]:-end[i]])
        rollav = np.zeros(len(a)-14)
        for i in range(7, len(a)-7):
            av = 0
            for j in range(1, 8):
                av += a[i-j]+a[i+j]
            rollav[i-7] = (av+a[i])/15
        rollavs += rollav
        ax.plot(days[7:-7], rollav, color='black', alpha=0.35)
    i =4
    a = np.array(allareacount[i][3][front[i]:-end[i]])
    rollav = np.zeros(len(a)-14)
    for i in range(7, len(a)-7):
        av = 0
        for j in range(1, 8):
            av += a[i-j]+a[i+j]
        rollav[i-7] = (av+a[i])/15
    rollavs += rollav
    ax.plot(days[7:-7], rollav, color='black', alpha=0.35, label='2015-2019')
    a = allareacount[5][3][front[5]:-end[5]]
    rollavs = rollavs/5
    for i in range(7, len(a)-7):
        av = 0
        for j in range(1, 8):
            av += a[i-j]+a[i+j]
        rollav[i-7] = (av+a[i])/15
    ax.plot(days[7:-7], rollav, color='red', label='15 day rolling average 2020')
    ax.plot(days[7:-7], rollavs, color=green, label='Mean 15 day rolling average 2015-2019')
    ax.plot(label='15 day rolling average for 2015-2019')
    ax.set_xticks(positions)
    ax.set_xticks(hals, minor=True)
    ax.set_xticklabels([])
    ax.set_xticklabels(labels, minor=True)
    ax.tick_params(axis='x', which='minor', length=0)
    plt.ylabel('Area ($km^2$)', fontsize=14)
    plt.legend(loc='upper left')
    plt.savefig(filepath+'/Plots/arearollavcompplot.pdf', bbox_inches='tight')
    plt.close()
    
def getAreaRollAvCompFilledPlot(allareacount, filepath):
    days = np.arange(0, 366, 1)
    fig, ax = plt.subplots(figsize=(20,10))
    rollavs = []
    for i in range(0, len(allareacount)-1):
        a = np.array(allareacount[i][3][front[i]:-end[i]])
        rollav = np.zeros(len(a)-14)
        for i in range(7, len(a)-7):
            av = 0
            for j in range(1, 8):
                av += a[i-j]+a[i+j]
            rollav[i-7] = (av+a[i])/15
            #plt.fill_between(days[7:-7], rollav, color='black', alpha=0.5)
            rollavs.append(rollav)
    fill = np.zeros(len(rollav))
    for i in range(0, len(rollav)):
        fill[i] = max(rollavs[0][i], rollavs[1][i], rollavs[2][i], rollavs[3][i], rollavs[4][i])
    plt.fill_between(days[7:-7], fill, color='black', label='2015-2019', alpha=0.5)
    a = allareacount[5][3][front[5]:-end[5]]
    for i in range(7, len(a)-7):
        av = 0
        for j in range(1, 8):
            av += a[i-j]+a[i+j]
        rollav[i-7] = (av+a[i])/15
    ax.plot(days[7:-7], rollav, color='red', label='15 day rolling average for 2020')
    #plt.axvspan(10+aug-(d1-d0).days, nov-15-(d1-d0).days, color='g', alpha=0.25, lw=0)
    ax.plot(label='15 day rolling average for 2015-2019')
    ax.set_xticks(positions)
    ax.set_xticks(hals, minor=True)
    ax.set_xticklabels([])
    ax.set_xticklabels(labels, minor=True)
    ax.tick_params(axis='x', which='minor', length=0)
    plt.title('Total Fire Area', fontsize=20)
    plt.ylabel('Area [km$^2$]', fontsize=14)
    plt.legend(loc='upper right')
    plt.savefig(filepath+'/Plots/testarearollavcompfilledplot.pdf', bbox_inches='tight')
    plt.close()
    
    
def getAreaRollAvSumPlot(allareacount, filepath):
    days = np.arange(0, 366, 1)
    fig, ax = plt.subplots(figsize=(20,10))
    total = np.zeros(len(allareacount[0][3])-16)
    for i in range(0, len(allareacount)-1):
        a = np.array(allareacount[i][3][front[i]:-end[i]])
        rollav = np.zeros(len(a)-14)
        for i in range(7, len(a)-7):
            av = 0
            for j in range(1, 8):
                av += a[i-j]+a[i+j]
            rollav[i-7] = (av+a[i])/15
        total += rollav
    plt.fill_between(days[7:-7], total, color='black', alpha=0.5)
    plt.fill_between(days[7:-7], rollav, color='black', label='Sum of 2015-2019', alpha=0.5)
    a = allareacount[5][3][front[5]:-end[5]]
    for i in range(7, len(a)-7):
        av = 0
        for j in range(1, 8):
            av += a[i-j]+a[i+j]
        rollav[i-7] = (av+a[i])/15
    ax.plot(days[7:-7], rollav, color='red', label='15 day rolling average for 2020')
    plt.axvspan(sep-(d1-d0).days, nov-20-(d1-d0).days, color='b', alpha=0.1, lw=0)
    ax.set_xticks(positions)
    ax.set_xticks(hals, minor=True)
    ax.set_xticklabels([])
    ax.set_xticklabels(labels, minor=True)
    ax.tick_params(axis='x', which='minor', length=0)
    plt.title('Total Fire Area', fontsize=20)
    plt.ylabel('Area [km$^2$]', fontsize=14)
    plt.legend(loc='upper right')
    plt.savefig(filepath+'/Plots/arearollavsumplot.pdf', bbox_inches='tight')
    plt.close()
    
    
def getAreaCountStem(allareacount, filepath):
    days = np.arange(0, 366, 1)
    fig, ax = plt.subplots(figsize=(20,10))
    ax.stem(days, allareacount[5][3][front[5]:-end[5]], 'rx', label='2020')
    fiveav = np.zeros(len(allareacount[0][0]))
    for i in range(0, len(allareacount[0])-1):
        ax.stem(days, allareacount[i][3][front[i]:-end[i]], 'b.')
        a = np.array(allareacount[i][3])
        fiveav += a
    fiveav = fiveav/5
    fiveav = fiveav[front[0]:-end[0]]
    ax.stem(days, fiveav, 'k.', label='Five Year Average')
    ax.set_xticks(positions)
    ax.set_xticks(hals, minor=True)
    ax.set_xticklabels([])
    ax.set_xticklabels(labels, minor=True)
    ax.tick_params(axis='x', which='minor', length=0)
    plt.title('Total Fire Area', fontsize=20)
    plt.ylabel('Area [km$^2$]', fontsize=14)
    plt.legend(loc='upper right')
    plt.savefig(filepath+'/Plots/areacountstem.pdf', bbox_inches='tight')
    plt.close()
    
    
def getAreaCountTypePlot(allareacount, filepath):
    days = np.arange(0, 366, 1)
    fig, ax = plt.subplots(figsize=(8,5))
    ax.plot(days, allareacount[5][0][front[5]:-end[5]], color='#FCD12A', label='Low confidence')
    ax.plot(days, allareacount[5][1][front[5]:-end[5]], color='orange', label='Nominal confidence')
    ax.plot(days, allareacount[5][2][front[5]:-end[5]], color='red', label='High confidence')
    ax.plot(days, allareacount[5][3][front[5]:-end[5]], color='black', label='Total')
    ax.set_xticks(positions)
    ax.set_xticks(hals, minor=True)
    ax.set_xticklabels([])
    ax.set_xticklabels(labels, minor=True)
    ax.tick_params(axis='x', which='minor', length=0)
    #plt.title('Total fire area for each pixel confidence', fontsize=20, fontweight='bold')
    plt.ylabel('Area ($km^2$)', fontsize=14)
    plt.legend(loc='upper left')
    plt.yscale('log')
    plt.savefig(filepath+'/Plots/areacounttypeplot.pdf', bbox_inches='tight')
    plt.close()
    
    
def getCumulativeCountPlot(allcarea, filepath):
    days = np.arange(0, 366, 1)
    fig, ax = plt.subplots(figsize=(8,5))
    for i in range(0, len(allcarea)-2):
        ax.plot(days, allcarea[i][front[i]:-end[i]], color='black')
    ax.plot(days, allcarea[4][front[4]:-end[4]], color='black', label='2015-2019')
    ax.text(days[365]+3, allcarea[0][365]-600, '2015')
    ax.text(days[365]+3, allcarea[1][365]+300, '2016')
    ax.text(days[365]+3, allcarea[2][365]+600, '2017')
    ax.text(days[365]+3, allcarea[3][365]-600, '2018')
    ax.text(days[365]+3, allcarea[4][365]-150, '2019')
    ax.text(days[365]+3, allcarea[5][365]-100, '2020')
    fiveav = np.zeros(len(allcarea[0]))
    for i in range(0, len(allcarea)-1):
        fiveav += np.array(allcarea[i])
    fiveav = fiveav[front[0]:-end[0]]/5
    ax.plot(days, fiveav, color=green, label='Five Year Average')
    ax.plot(days, allcarea[5][front[5]:-end[5]], color='red', label='2020')
    ax.text(days[365]+3, fiveav[365]-300, 'Mean')
    #print('2020: '+str(allcarea[5][365]))
    #print('Mean: '+str(fiveav[365]))
    #print('Factor: '+str((allcarea[5][365])/fiveav[365]))
    print('2020: '+str(allcarea[5][sep]-allcarea[5][aug]))
    print('Mean: '+str(fiveav[sep]-fiveav[aug]))
    print('Factor: '+str((allcarea[5][sep]-allcarea[5][aug])/(fiveav[sep]-fiveav[aug])))
    ax.set_xticks(positions)
    ax.set_xticks(hals, minor=True)
    ax.set_xticklabels([])
    ax.set_xticklabels(labels, minor=True)
    ax.tick_params(axis='x', which='minor', length=0)
    ax.set_xlim(-10, 395)
    #plt.title('Cumulative fire area', fontsize=20, fontweight='bold')
    plt.ylabel('Area ($km^2$)', fontsize=14)
    #plt.legend(loc='upper left')
    #plt.yscale('log')
    plt.savefig(filepath+'/Plots/cumulativecountplot.pdf', bbox_inches='tight')
    plt.close()

    
def getMeanAreaPlot(allareacount, allfirecount, filepath):
    meanareas = []
    days = np.arange(0, 366, 1)
    for i in range(0, len(allareacount)):
        m = np.zeros(len(allareacount[i][3]))
        for j in range(0, len(allareacount[i][3])):
            if allareacount[i][3][j] != 0:
                m[j] = allareacount[i][3][j]/allfirecount[i][str(j+1)]
        m = m[front[i]:-end[i]]
        meanareas.append(m)
    avarea = np.zeros(366)
    for i in range(0, len(meanareas)-1):
        avarea += np.array(meanareas[i])
    avarea = avarea/(len(allareacount)-1)
    fig, ax = plt.subplots(figsize=(20,10))
    #ax.plot(days, meanareas[0], 'b', label='2015')
    #ax.plot(days, meanareas[1], 'b', label='2016')
    #ax.plot(days, meanareas[2], 'b', label='2017')
    #ax.plot(days, meanareas[3], 'b', label='2018')
    #ax.plot(days, meanareas[4], 'b', label='2019')
    ax.plot(days, meanareas[5], 'r', label='2020')
    ax.plot(days, avarea, 'k', label='Five Year Average')
    ax.set_xticks(positions)
    ax.set_xticks(hals, minor=True)
    ax.set_xticklabels([])
    ax.set_xticklabels(labels, minor=True)
    ax.tick_params(axis='x', which='minor', length=0)
    plt.title('Mean Fire Size', fontsize=20)
    plt.ylabel('Area [km$^2$]', fontsize=14)
    plt.legend(loc='upper right')
    plt.savefig(filepath+'/Plots/meanareaplot.pdf', bbox_inches='tight')
    plt.close()
    
    
def getMeanAreaRollAvPlot(allareacount, allfirecount, filepath):
    days = np.arange(0, 366, 1)
    m = np.zeros(len(allareacount[5][3]))
    for j in range(0, len(allareacount[5][3])):
        if allareacount[5][3][j] != 0:
            m[j] = allareacount[5][3][j]/allfirecount[5][str(j+1)]
    m = m[front[5]:-end[5]]
    rollav = np.zeros(len(m)-14)
    for i in range(7, len(m)-7):
        av = 0
        for j in range(1, 8):
            av += m[i-j]+m[i+j]
        rollav[i-7] = (av+m[i])/15
    fig, ax = plt.subplots(figsize=(20,10))
    ax.plot(days, m, 'r', label='Signal')
    ax.plot(days[7:-7], rollav, 'k', label='15 day rolling average')
    ax.set_xticks(positions)
    ax.set_xticks(hals, minor=True)
    ax.set_xticklabels([])
    ax.set_xticklabels(labels, minor=True)
    ax.tick_params(axis='x', which='minor', length=0)
    plt.title('Mean Fire Size', fontsize=20)
    plt.ylabel('Area [km$^2$]', fontsize=14)
    plt.legend(loc='upper right')
    plt.savefig(filepath+'/Plots/meanarearollavplot.pdf', bbox_inches='tight')
    plt.close()
    
    
def getMeanAreaRollAvCompPlot(allareacount, allfirecount, filepath):
    meanareas = []
    for i in range(0, len(allareacount)):
        m = np.zeros(len(allareacount[i][3]))
        for j in range(0, len(allareacount[i][3])):
            if allareacount[i][3][j] != 0:
                m[j] = allareacount[i][3][j]/allfirecount[i][str(j+1)]
        m = m[front[i]:-end[i]]
        meanareas.append(m)
    avarea = np.zeros(366)
    for i in range(0, len(meanareas)-1):
        avarea += np.array(meanareas[i])
    avarea = avarea/(len(allareacount)-1)
    days = np.arange(0, 366, 1)
    m = np.zeros(len(allareacount[5][3]))
    for j in range(0, len(allareacount[5][3])):
        if allareacount[5][3][j] != 0:
            m[j] = allareacount[5][3][j]/allfirecount[5][str(j+1)]
    m = m[front[5]:-end[5]]
    rollav = np.zeros(len(m)-14)
    rollbv = np.zeros(len(avarea)-14)
    for i in range(7, len(m)-7):
        av = 0
        bv = 0
        for j in range(1, 8):
            av += m[i-j]+m[i+j]
            bv += avarea[i-j]+avarea[i+j]
        rollav[i-7] = (av+m[i])/15
        rollbv[i-7] = (bv+avarea[i])/15
    fig, ax = plt.subplots(figsize=(8,5))
    #ax.plot(days, m, 'r', label='Signal')
    ax.plot(days[7:-7], rollav, 'r', label='15 day rolling average')
    ax.plot(days[7:-7], rollbv, color=green, label='Five year 15 day rolling average')
    ax.set_xticks(positions)
    ax.set_xticks(hals, minor=True)
    ax.set_xticklabels([])
    ax.set_xticklabels(labels, minor=True)
    ax.tick_params(axis='x', which='minor', length=0)
    #plt.title('Mean Fire Size', fontsize=20, fontweight='bold')
    plt.ylabel('Area ($km^2$)', fontsize=14)
    plt.legend(loc='upper left')
    plt.savefig(filepath+'/Plots/groupmeanarearollavcompplot.pdf', bbox_inches='tight')
    plt.close()

"""
def getCumulativeAreaPlot(alldayarea, filepath):
    totareas = []
    days = np.arange(0, 366, 1)
    for i in range(0, len(alldayarea)):
        areas = np.zeros(len(alldayarea[i])//2)
        subtotal = 0
        try:
            for j in range(1, (len(alldayarea[i])//2)+1):
                subtotal += alldayarea[i][2*j]+alldayarea[i][2*j-1]
                areas[j-1] = subtotal
        except KeyError:
            for j in range(1, (len(alldayarea[i])//2)+1):
                subtotal += alldayarea[i][str(2*j)]+alldayarea[i][str(2*j-1)]
                areas[j-1] = subtotal
        areas = areas[front[i]:-end[i]]
        totareas.append(areas)
    avarea = np.zeros(366)
    for i in range(0, len(totareas)-1):
        avarea += totareas[i]
    avarea = avarea/(len(alldayarea)-1)
    fig, ax = plt.subplots(figsize=(20,10))
    ax.plot(days, totareas[(len(alldayarea)-1)], 'r', label='2020')
    ax.text(days[365]+3, totareas[(len(alldayarea)-1)][365]-4000, '2020')
    ax.plot(days, avarea, 'g', label='Five Year Average')
    print(avarea[365])
    var = 0
    for i in range(0, len(alldayarea)-1):
        ax.plot(days, totareas[i], 'k')
        var += (totareas[i][365]-avarea[365])**2
        if i == 0:
            ax.text(days[365]+3, totareas[i][365]-12500, '201'+str(i+5))
        elif i == 1:
            ax.text(days[365]+3, totareas[i][365]+7500, '201'+str(i+5))
        else:
            ax.text(days[365]+3, totareas[i][365]-4000, '201'+str(i+5))
    ax.text(days[365]+3, avarea[365]-4000, 'Mean')
    var = var/4
    sd = var**0.5
    print(var)
    print(totareas[5][365])
    print(((totareas[5][365])-(avarea[365]))/(sd))
    print('p=0.00003')
    print('Occurs normally every 33,333 years')
    ax.set_xticks(positions)
    ax.set_xticks(hals, minor=True)
    ax.set_xticklabels([])
    ax.set_xticklabels(labels, minor=True)
    ax.tick_params(axis='x', which='minor', length=0)
    plt.title('Cumulative Fire Area', fontsize=20)
    plt.ylabel('Area [km$^2$]', fontsize=14)
    plt.legend(loc='upper left')
    plt.savefig(filepath+'/Plots/cumulativeareaplot.pdf', bbox_inches='tight')
    plt.close()
    
    
def getCumulativeAdjustedPlot(alldayarea, filepath):
    totareas = []
    days = np.arange(0, 366, 1)
    for i in range(0, len(alldayarea)):
        areas = np.zeros(len(alldayarea[i])//2)
        subtotal = 0
        try:
            for j in range(1, (len(alldayarea[i])//2)+1):
                subtotal += alldayarea[i][2*j]+alldayarea[i][2*j-1]
                areas[j-1] = subtotal
        except KeyError:
            for j in range(1, (len(alldayarea[i])//2)+1):
                subtotal += alldayarea[i][str(2*j)]+alldayarea[i][str(2*j-1)]
                areas[j-1] = subtotal
        areas = areas[front[i]:-end[i]]
        totareas.append(areas)
    for i in range(0, len(totareas)):
        for j in range(0, len(totareas[i])):
            totareas[i][j] = totareas[i][j]/(j+1)
    avarea = np.zeros(366)
    for i in range(0, len(totareas)-1):
        avarea += totareas[i]
    avarea = avarea/(len(alldayarea)-1)
    fig, ax = plt.subplots(figsize=(20,10))
    ax.plot(days, totareas[(len(alldayarea)-1)], 'r', label='2020')
    ax.text(days[365]+3, totareas[(len(alldayarea)-1)][365], '2020')
    ax.plot(days, avarea, 'g', label='Five Year Average')
    print(avarea[365])
    var = 0
    for i in range(0, len(alldayarea)-1):
        ax.plot(days, totareas[i], 'k')
        var += (totareas[i][365]-avarea[365])**2
        if i == 0:
            ax.text(days[365]+3, totareas[i][365], '201'+str(i+5))
        elif i == 1:
            ax.text(days[365]+3, totareas[i][365], '201'+str(i+5))
        else:
            ax.text(days[365]+3, totareas[i][365], '201'+str(i+5))
    ax.text(days[365]+3, avarea[365], 'Mean')
    var = var/4
    sd = var**0.5
    print(var)
    print(totareas[5][365])
    print(((totareas[5][365])-(avarea[365]))/(sd))
    print('p=0.00003')
    print('Occurs normally every 33,333 years')
    ax.set_xticks(positions)
    ax.set_xticks(hals, minor=True)
    ax.set_xticklabels([])
    ax.set_xticklabels(labels, minor=True)
    ax.tick_params(axis='x', which='minor', length=0)
    plt.title('Cumulative Fire Area', fontsize=20)
    plt.ylabel('Area [km$^2$]', fontsize=14)
    plt.legend(loc='upper left')
    plt.savefig(filepath+'/Plots/adjustedcumulativeareaplot.pdf', bbox_inches='tight')
    plt.close()
    
    
def getLogCumulativeAreaPlot(alldayarea, filepath):
    totareas = []
    days = np.arange(0, 366, 1)
    for i in range(0, len(alldayarea)):
        areas = np.zeros(len(alldayarea[i])//2)
        subtotal = 0
        try:
            for j in range(1, (len(alldayarea[i])//2)+1):
                subtotal += alldayarea[i][2*j]+alldayarea[i][2*j-1]
                areas[j-1] = subtotal
        except KeyError:
            for j in range(1, (len(alldayarea[i])//2)+1):
                subtotal += alldayarea[i][str(2*j)]+alldayarea[i][str(2*j-1)]
                areas[j-1] = subtotal
        areas = areas[front[i]:-end[i]]
        totareas.append(areas)
    avarea = np.zeros(366)
    for i in range(0, len(totareas)-1):
        avarea += totareas[i]
    avarea = avarea/(len(alldayarea)-1)
    fig, ax = plt.subplots(figsize=(20,10))
    ax.plot(days, totareas[(len(alldayarea)-1)], 'r', label='2020')
    ax.text(days[365]+3, totareas[(len(alldayarea)-1)][365]-30000, '2020')
    ax.plot(days, avarea, 'g', label='Five Year Average')
    print(avarea[365])
    var = 0
    for i in range(0, len(alldayarea)-1):
        ax.plot(days, totareas[i], 'k')
        var += (totareas[i][365]-avarea[365])**2
        if i == 0:
            ax.text(days[365]+3, totareas[i][365]-15000, '201'+str(i+5))
        elif i == 1:
            ax.text(days[365]+3, totareas[i][365]+7500, '201'+str(i+5))
        elif i == 2:
            ax.text(days[365]+3, totareas[i][365]-30000, '201'+str(i+5))
        elif i == 3:
            ax.text(days[365]+3, totareas[i][365]+7500, '201'+str(i+5))
        elif i == 4:
            ax.text(days[365]+3, totareas[i][365]-7500, '201'+str(i+5))
    ax.text(days[365]+3, avarea[365]-4000, 'Mean')
    var = var/4
    sd = var**0.5
    print(var)
    print(totareas[5][365])
    print(((totareas[5][365])-(avarea[365]))/(sd))
    print('p=0.00003')
    print('Occurs normally every 33,333 years')
    ax.set_xticks(positions)
    ax.set_xticks(hals, minor=True)
    ax.set_xticklabels([])
    ax.set_xticklabels(labels, minor=True)
    ax.tick_params(axis='x', which='minor', length=0)
    plt.title('Cumulative Fire Area', fontsize=20)
    plt.ylabel('Area [km$^2$]', fontsize=14)
    plt.yscale("log")
    plt.legend(loc='upper left')
    plt.savefig(filepath+'/Plots/logcumulativeareaplot.pdf', bbox_inches='tight')
    plt.close()


def getFiresPlot(allfirecount, filepath):
    allfires = []
    days = np.arange(0, 366, 1)
    for i in range(0, len(allfirecount)):
        areas = np.zeros(len(allfirecount[i])//2)
        try:
            for j in range(1, (len(allfirecount[i])//2)+1):
                areas[j-1] = allfirecount[i][2*j]+allfirecount[i][2*j-1]
        except KeyError:
            for j in range(1, (len(allfirecount[i])//2)+1):
                areas[j-1] = allfirecount[i][str(2*j)]+allfirecount[i][str(2*j-1)]
        areas = areas[front[i]:-end[i]]
        allfires.append(areas)
    avfires = np.zeros(366)
    for i in range(0, len(allfires)-1):
        avfires += allfires[i]
    avfires = avfires/(len(allfirecount)-1)
    fig, ax = plt.subplots(figsize=(20,10))
    ax.plot(days, allfires[(len(allfirecount)-1)], 'r', label='2020')
    ax.plot(days, avfires, 'k', label='Five Year Average')
    #ax.plot(days, totareas[0], 'b')
    #ax.plot(days, totareas[1], 'g')
    ax.set_xticks(positions)
    ax.set_xticks(hals, minor=True)
    ax.set_xticklabels([])
    ax.set_xticklabels(labels, minor=True)
    ax.tick_params(axis='x', which='minor', length=0)
    plt.title('Number of Fires', fontsize=20)
    plt.ylabel('Number of Fires', fontsize=14)
    plt.legend(loc='upper right')
    plt.savefig(filepath+'/Plots/firesplot.pdf', bbox_inches='tight')
    plt.close()
"""
    
def getFiresPlot(allfirecount, filepath):
    days = np.arange(0, 366, 1)
    fig, ax = plt.subplots(figsize=(20,10))
    fires = np.zeros(len(allfirecount[5]))
    for i in range(0, len(fires)):
        fires[i] = allfirecount[5][str(i+1)]
    ax.plot(days, fires[front[5]:-end[5]], color='red', label='2020')
    fiveav = np.zeros(len(allfirecount[0]))
    for i in range(0, len(allfirecount)-1):
        a = np.zeros(len(allfirecount[i]))
        for j in range(0, len(allfirecount[i])):
            a[j] = allfirecount[i][str(j+1)]
        fiveav += a
    fiveav = fiveav/5
    fiveav = fiveav[front[0]:-end[0]]
    ax.plot(days, fiveav, color='black', label='Five Year Average')
    ax.set_xticks(positions)
    ax.set_xticks(hals, minor=True)
    ax.set_xticklabels([])
    ax.set_xticklabels(labels, minor=True)
    ax.tick_params(axis='x', which='minor', length=0)
    plt.title('Number of Fires', fontsize=20)
    plt.ylabel('Area [km$^2$]', fontsize=14)
    plt.legend(loc='upper right')
    plt.savefig(filepath+'/Plots/firecountplot.pdf', bbox_inches='tight')
    plt.close()
    

def getFiresCountPlot(allfiresets, filepath):
    fig, ax = plt.subplots(figsize=(20,10))
    days = np.arange(0, 366, 1)
    for i in range(0, len(allfiresets)):
        a = np.zeros(len(allfiresets[i]))
        for j in range(0, len(allfiresets[i])):
            a[j] = len(allfiresets[i][j])
        ax.plot(days, a[front[i]:-end[i]], 'k', label=str(i))
    ax.set_xticks(positions)
    ax.set_xticks(hals, minor=True)
    ax.set_xticklabels([])
    ax.set_xticklabels(labels, minor=True)
    ax.tick_params(axis='x', which='minor', length=0)
    plt.title('Number of Fires', fontsize=20)
    plt.ylabel('Area [km$^2$]', fontsize=14)
    plt.legend(loc='upper right')
    plt.savefig(filepath+'/Plots/firecountplot.pdf', bbox_inches='tight')
    plt.close()
        
    
    
def getFiresRollAvPlot(allfirecount, filepath):
    days = np.arange(0, 366, 1)
    fig, ax = plt.subplots(figsize=(20,10))
    f = np.zeros(len(allfirecount[5]))
    for i in range(0, len(allfirecount[5])):
        f[i] = allfirecount[5][str(i+1)]
    f = f[front[5]:-end[5]]
    ax.plot(days, f, color='red', label='Signal')
    rollav = np.zeros(len(f)-14)
    for i in range(7, len(f)-7):
        av = 0 
        for j in range(1, 8):
            av += f[i-j]+f[i+j]
        rollav[i-7] = (av+f[i])/15
    ax.plot(days[7:-7], rollav, color='black', label='15 day rolling average')
    ax.set_xticks(positions)
    ax.set_xticks(hals, minor=True)
    ax.set_xticklabels([])
    ax.set_xticklabels(labels, minor=True)
    ax.tick_params(axis='x', which='minor', length=0)
    plt.title('Number of Fires', fontsize=20)
    plt.ylabel('Area [km$^2$]', fontsize=14)
    plt.legend(loc='upper right')
    plt.savefig(filepath+'/Plots/firerollavplot.pdf', bbox_inches='tight')
    plt.close()
    
    
def getFiresRollAvCompPlot(allfirecount, allcomplexcount, filepath):
    days = np.arange(0, 366, 1)
    fig, ax = plt.subplots(figsize=(8,5))
    
    avsimple = np.zeros(len(allfirecount[0]))
    for i in range(0, len(allfirecount)-1):
        fsimple = np.zeros(len(allfirecount[i]))
        for j in range(0, len(fsimple)):
            fsimple[j] = allfirecount[i][str(j+1)]-allcomplexcount[i][j]
        avsimple += fsimple
    avsimple /= 5
    avsimple = avsimple[front[0]:-end[0]]
    
    avcomplex = np.zeros(len(allcomplexcount[0]))
    for i in range(0, 4):
        avcomplex += allcomplexcount[i]
    avcomplex /= 5
    avcomplex = avcomplex[front[0]:-end[0]]
    
    simple = np.zeros(len(allfirecount[5]))
    for i in range(0, len(allfirecount[5])):
        simple[i] = allfirecount[5][str(i+1)]-allcomplexcount[5][j]
    simple = simple[front[5]:-end[5]]
    complex = allcomplexcount[5][front[5]:-end[5]]
    
    rollmsimple = np.zeros(len(avsimple)-14)
    rollmcomplex = np.zeros(len(avcomplex)-14)
    rollsimple = np.zeros(len(simple)-14)
    rollcomplex = np.zeros(len(complex)-14)
    
    for i in range(7, len(rollmsimple)+7):
        avs = 0
        avc = 0
        s = 0
        c = 0
        for j in range(1, 8):
            avs += avsimple[i-j]+avsimple[i+j]
            avc += avcomplex[i-j]+avcomplex[i+j]
            s += simple[i-j]+simple[i+j]
            c += complex[i-j]+complex[i+j]
        rollmsimple[i-7] = (avs+avsimple[i])/15
        rollmcomplex[i-7] = (avc+avcomplex[i])/15
        rollsimple[i-7] = (s+simple[i])/15
        rollcomplex[i-7] = (c+complex[i])/15
    ax.plot(days[7:-7], rollsimple, color='orange', label='15 day rolling average of simple fires 2020')
    ax.plot(days[7:-7], rollcomplex, color='red', label='15 day rolling average of complex fires 2020')
    ax.plot(days[7:-7], rollmsimple, color=lightgreen, label='Mean 15 day rolling average of simple fires \n 2015-2019')
    ax.plot(days[7:-7], rollmcomplex, color=darkgreen, label='Mean 15 day rolling average of complex fires \n 2015-2019')
    ax.set_xticks(positions)
    ax.set_xticks(hals, minor=True)
    ax.set_xticklabels([])
    ax.set_xticklabels(labels, minor=True)
    ax.tick_params(axis='x', which='minor', length=0)
    #plt.title('Number of fires', fontsize=20, fontweight='bold')
    plt.ylabel('Number of fires', fontsize=14)
    plt.legend(loc='upper left')
    plt.savefig(filepath+'/Plots/firerollavcompplot.pdf', bbox_inches='tight')
    plt.close()
    
    
def getFireandAreaPlot(allareacount, allfirecount, filepath):
    days = np.arange(0, 366, 1)
    fig, ax = plt.subplots(figsize=(20,10))
    ax.plot(days, allareacount[5][3][front[5]:-end[5]], color='red', label='area of fires')
    fires = np.zeros(len(allfirecount[5]))
    for i in range(0, len(fires)):
        fires[i] = allfirecount[5][str(i+1)]
    ax.plot(days, fires[front[5]:-end[5]], color='black', label='number of fires')
    fiveav = np.zeros(len(allfirecount[0]))
    for i in range(0, len(allfirecount)-1):
        a = np.zeros(len(allfirecount[i]))
        for j in range(0, len(allfirecount[i])):
            a[j] = allfirecount[i][str(j+1)]
        fiveav += a
    fiveav = fiveav/5
    fiveav = fiveav[front[0]:-end[0]]
    #ax.plot(days, fiveav, color='black', label='Five Year Average')
    ax.set_xticks(positions)
    ax.set_xticks(hals, minor=True)
    ax.set_xticklabels([])
    ax.set_xticklabels(labels, minor=True)
    ax.tick_params(axis='x', which='minor', length=0)
    plt.title('Number of Fires', fontsize=20)
    plt.ylabel('Area [km$^2$]', fontsize=14)
    plt.legend(loc='upper right')
    plt.savefig(filepath+'/Plots/fireandareaplot.pdf', bbox_inches='tight')
    plt.close()
    
"""
def getFiresAndAreaPlot(allareacount, allfirecount, filepath):
    allfires = []
    days = np.arange(0, 366, 1)
    for i in range(0, len(allfirecount)):
        areas = np.zeros(len(allfirecount[i])//2)
        try:
            for j in range(1, (len(allfirecount[i])//2)+1):
                areas[j-1] = allfirecount[i][2*j]+allfirecount[i][2*j-1]
        except KeyError:
            for j in range(1, (len(allfirecount[i])//2)+1):
                areas[j-1] = allfirecount[i][str(2*j)]+allfirecount[i][str(2*j-1)]
        areas = areas[front[i]:-end[i]]
        allfires.append(areas)
    avfires = np.zeros(366)
    for i in range(0, len(allfires)-1):
        avfires += allfires[i]
    avfires = avfires/(len(allfirecount)-1)
    aac = np.array(allareacount[5][3][front[5]:-end[5]])/50
    fig, ax = plt.subplots(figsize=(20,10))
    ax.plot(days, aac, 'r', label='Area on fire (scaled)')
    ax.plot(days, allfires[(len(allfirecount)-1)], 'k', label='Number of fires')
    #ax.plot(days, avfires, 'k', label='Five Year Average')
    #ax.plot(days, totareas[0], 'b')
    #ax.plot(days, totareas[1], 'g')
    ax.set_xticks(positions)
    ax.set_xticks(hals, minor=True)
    ax.set_xticklabels([])
    ax.set_xticklabels(labels, minor=True)
    ax.tick_params(axis='x', which='minor', length=0)
    plt.title('Number of Fires', fontsize=20)
    plt.ylabel('Number of Fires', fontsize=14)
    plt.legend(loc='upper right')
    plt.savefig(filepath+'/Plots/firesandareaplot.pdf', bbox_inches='tight')
    plt.close()
    
    
def getShapePlot(contours):
    x = np.zeros(len(contours[0]))
    y = np.zeros(len(contours[0]))
    for i in range(0, len(contours[0])-1):
        x[i] = float((contours[0][i][0][0])/1000)
        y[i] = float((contours[0][i][0][1])/1000)
    plt.scatter(x, y)
    plt.xlim(1.2, 1.45)
    plt.ylim(10.1, 10.3)
    plt.show()

    
def getComplexFiresPlot(allclustercount, filepath):
    allclusters = []
    days = np.arange(0, 366, 1)
    for i in range(0, len(allclustercount)):
        clusters = np.zeros(len(allclustercount[i])//2)
        for j in range(1, (len(allclustercount[i])//2)+1):
            try:
                clusters[j-1] = (allclustercount[i][2*j])+(allclustercount[i][2*j-1])
            except KeyError:
                clusters[j-1] = (allclustercount[i][str(2*j)])+(allclustercount[i][str(2*j-1)])
        clusters = clusters[front[i]:-end[i]]
        allclusters.append(clusters)
    avclusters = np.zeros(366)
    for i in range(0, len(allclusters)-1):
        avclusters += allclusters[i]
    avclusters = avclusters/(len(allclustercount)-1)
    fig, ax = plt.subplots(figsize=(20,10))
    ax.plot(days, allclusters[(len(allclustercount)-1)], 'r', label='2020')
    ax.plot(days, avclusters, 'k', label='Five Year Average')
    #ax.plot(days, allclusters[0], 'k', label='2015')
    #ax.plot(days, allclusters[1], 'k', label='2016')
    #ax.plot(days, allclusters[2], 'k', label='2017')
    #ax.plot(days, allclusters[3], 'k', label='2018')
    #ax.plot(days, allclusters[4], 'k', label='2019')
    #ax.plot(days, allclusters[5], 'k', label='2020')
    ax.set_xticks(positions)
    ax.set_xticks(hals, minor=True)
    ax.set_xticklabels([])
    ax.set_xticklabels(labels, minor=True)
    ax.tick_params(axis='x', which='minor', length=0)
    plt.title('Number of Complex Fires', fontsize=20)
    plt.ylabel('Number of Complex Fires', fontsize=14)
    plt.legend(loc='upper right')
    plt.savefig(filepath+'/Plots/testtestcomplexplot.pdf', bbox_inches='tight')
    plt.close()
"""    
    
def getComplexFiresPlot(allclustercount, filepath):
    clusters = []
    days = np.arange(0, 366, 1)
    for i in range(0, len(allclustercount)):
        c = np.zeros(len(allclustercount[i]))
        for j in range(0, len(allclustercount[i])):
            c[j] = allclustercount[i][str(j+1)]
        clusters.append(c)
    avclusters = np.zeros(366)
    for i in range(0, len(clusters)-1):
        avclusters += clusters[i][front[i]:-end[i]]
    avclusters = avclusters/5
    fig, ax = plt.subplots(figsize=(20,10))
    ax.plot(days, clusters[5][front[5]:-end[5]], 'r', label='2020')
    ax.plot(days, avclusters, 'k', label='Five Year Average')
    #ax.plot(days, allclusters[0], 'k', label='2015')
    #ax.plot(days, allclusters[1], 'k', label='2016')
    #ax.plot(days, allclusters[2], 'k', label='2017')
    #ax.plot(days, allclusters[3], 'k', label='2018')
    #ax.plot(days, allclusters[4], 'k', label='2019')
    #ax.plot(days, allclusters[5], 'k', label='2020')
    ax.set_xticks(positions)
    ax.set_xticks(hals, minor=True)
    ax.set_xticklabels([])
    ax.set_xticklabels(labels, minor=True)
    ax.tick_params(axis='x', which='minor', length=0)
    plt.title('Number of Complex Fires', fontsize=20)
    plt.ylabel('Number of Complex Fires', fontsize=14)
    plt.legend(loc='upper right')
    plt.savefig(filepath+'/Plots/complexplot.pdf', bbox_inches='tight')
    plt.close()
    
"""
def getFireTypePlot(allclustercount, allfirecount, filepath):
    allclusters = []
    allsimples = []
    days = np.arange(0, 366, 1)
    for i in range(0, len(allclustercount)):
        clusters = np.zeros(len(allclustercount[i])//2)
        simples = np.zeros(len(allfirecount[i])//2)
        for j in range(1, (len(allclustercount[i])//2)+1):
            try:
                clusters[j-1] = allclustercount[i][2*j]+allclustercount[i][2*j-1]
                simples[j-1] = allfirecount[i][2*j]+allfirecount[i][2*j-1]-clusters[j-1]
            except KeyError:
                clusters[j-1] = allclustercount[i][str(2*j)]+allclustercount[i][str(2*j-1)]
                simples[j-1] = allfirecount[i][str(2*j)]+allfirecount[i][str(2*j-1)]-clusters[j-1]
        clusters = clusters[front[i]:-end[i]]
        simples = simples[front[i]:-end[i]]
        allclusters.append(clusters)
        allsimples.append(simples)
    avclusters = np.zeros(366)
    avsimples = np.zeros(366)
    for i in range(0, len(allclusters)-1):
        avclusters += allclusters[i]
        avsimples += allsimples[i]
    avclusters = avclusters/(len(allclustercount)-1)
    avsimples = avsimples/(len(allclustercount)-1)
    fig, ax = plt.subplots(figsize=(20,10))
    ax.plot(days, allclusters[(len(allclustercount)-1)], 'r', label='2020 Complex')
    ax.plot(days, allsimples[(len(allclustercount)-1)], color='orange', label='2020 Simple')
    #ax.plot(days, avclusters, 'k', label='Complex Five Year Average')
    #ax.plot(days, avsimples, 'g', label='Simple Five Year Average')
    ax.set_xticks(positions)
    ax.set_xticks(hals, minor=True)
    ax.set_xticklabels([])
    ax.set_xticklabels(labels, minor=True)
    ax.tick_params(axis='x', which='minor', length=0)
    plt.title('Simple and Complex Fires', fontsize=20)
    plt.ylabel('Number of Fires', fontsize=14)
    plt.legend(loc='upper right')
    plt.savefig(filepath+'/Plots/typeplot.pdf', bbox_inches='tight')
    plt.close()
"""   
    
def getFireTypePlot(allclustercount, allfirecount, filepath):
    clusters = []
    simples = []
    days = np.arange(0, 366, 1)
    for i in range(0, len(allclustercount)):
        c = np.zeros(len(allclustercount[i]))
        s = np.zeros(len(allclustercount[i]))
        for j in range(0, len(allclustercount[i])):
            c[j] = allclustercount[i][str(j+1)]
            s[j] = allfirecount[i][str(j+1)]-allclustercount[i][str(j+1)]
        clusters.append(c)
        simples.append(s)
    fig, ax = plt.subplots(figsize=(20,10))
    ax.plot(days, clusters[5][front[5]:-end[5]], color='red', label='Complex')
    ax.plot(days, simples[5][front[5]:-end[5]], color='orange', label='Simple')
    #ax.plot(days, allclusters[0], 'k', label='2015')
    #ax.plot(days, allclusters[1], 'k', label='2016')
    #ax.plot(days, allclusters[2], 'k', label='2017')
    #ax.plot(days, allclusters[3], 'k', label='2018')
    #ax.plot(days, allclusters[4], 'k', label='2019')
    #ax.plot(days, allclusters[5], 'k', label='2020')
    ax.set_xticks(positions)
    ax.set_xticks(hals, minor=True)
    ax.set_xticklabels([])
    ax.set_xticklabels(labels, minor=True)
    ax.tick_params(axis='x', which='minor', length=0)
    plt.title('Number of Complex Fires', fontsize=20)
    plt.ylabel('Number of Complex Fires', fontsize=14)
    plt.legend(loc='upper right')
    plt.savefig(filepath+'/Plots/typeplot.pdf', bbox_inches='tight')
    plt.close()
    
"""
def getSimplePlot(allclustercount, allfirecount, filepath):
    allclusters = []
    allsimples = []
    days = np.arange(0, 366, 1)
    for i in range(0, len(allclustercount)):
        clusters = np.zeros(len(allclustercount[i])//2)
        simples = np.zeros(len(allfirecount[i])//2)
        for j in range(1, (len(allclustercount[i])//2)+1):
            try:
                clusters[j-1] = allclustercount[i][2*j]+allclustercount[i][2*j-1]
                simples[j-1] = allfirecount[i][2*j]+allfirecount[i][2*j-1]-clusters[j-1]
            except KeyError:
                clusters[j-1] = allclustercount[i][str(2*j)]+allclustercount[i][str(2*j-1)]
                simples[j-1] = allfirecount[i][str(2*j)]+allfirecount[i][str(2*j-1)]-clusters[j-1]
        clusters = clusters[front[i]:-end[i]]
        simples = simples[front[i]:-end[i]]
        allclusters.append(clusters)
        allsimples.append(simples)
    avclusters = np.zeros(366)
    avsimples = np.zeros(366)
    for i in range(0, len(allclusters)-1):
        avclusters += allclusters[i]
        avsimples += allsimples[i]
    avclusters = avclusters/(len(allclustercount)-1)
    avsimples = avsimples/(len(allclustercount)-1)
    fig, ax = plt.subplots(figsize=(20,10))
    ax.plot(days, allsimples[(len(allclustercount)-1)], color='orange', label='2020')
    ax.plot(days, avsimples, 'k', label='Five Year Average')
    ax.set_xticks(positions)
    ax.set_xticks(hals, minor=True)
    ax.set_xticklabels([])
    ax.set_xticklabels(labels, minor=True)
    ax.tick_params(axis='x', which='minor', length=0)
    plt.title('Simple Fires', fontsize=20)
    plt.ylabel('Number of Fires', fontsize=14)
    plt.legend(loc='upper right')
    plt.savefig(filepath+'/Plots/simpleplot.pdf', bbox_inches='tight')
    plt.close()
    
    
def getComplexPlot(allclustercount, allfirecount, filepath):
    allclusters = []
    allsimples = []
    days = np.arange(0, 366, 1)
    for i in range(0, len(allclustercount)):
        clusters = np.zeros(len(allclustercount[i])//2)
        simples = np.zeros(len(allfirecount[i])//2)
        for j in range(1, (len(allclustercount[i])//2)+1):
            try:
                clusters[j-1] = allclustercount[i][2*j]+allclustercount[i][2*j-1]
                simples[j-1] = allfirecount[i][2*j]+allfirecount[i][2*j-1]-clusters[j-1]
            except KeyError:
                clusters[j-1] = allclustercount[i][str(2*j)]+allclustercount[i][str(2*j-1)]
                simples[j-1] = allfirecount[i][str(2*j)]+allfirecount[i][str(2*j-1)]-clusters[j-1]
        clusters = clusters[front[i]:-end[i]]
        simples = simples[front[i]:-end[i]]
        allclusters.append(clusters)
        allsimples.append(simples)
    avclusters = np.zeros(366)
    avsimples = np.zeros(366)
    for i in range(0, len(allclusters)-1):
        avclusters += allclusters[i]
        avsimples += allsimples[i]
    avclusters = avclusters/(len(allclustercount)-1)
    avsimples = avsimples/(len(allclustercount)-1)
    fig, ax = plt.subplots(figsize=(20,10))
    ax.plot(days, allclusters[(len(allclustercount)-1)], 'r', label='2020')
    ax.plot(days, avclusters, 'k', label='Complex Five Year Average')
    ax.set_xticks(positions)
    ax.set_xticks(hals, minor=True)
    ax.set_xticklabels([])
    ax.set_xticklabels(labels, minor=True)
    ax.tick_params(axis='x', which='minor', length=0)
    plt.title('Complex Fires', fontsize=20)
    plt.ylabel('Number of Fires', fontsize=14)
    plt.legend(loc='upper right')
    plt.savefig(filepath+'/Plots/complexplot.pdf', bbox_inches='tight')
    plt.close()
    return allclusters

    
def getFireTypeFilledPlot(allclustercount, allfirecount, filepath):
    allfires = []
    allsimples = []
    days = np.arange(0, 366, 1)
    for i in range(0, len(allclustercount)):
        fires = np.zeros(len(allclustercount[i])//2)
        simples = np.zeros(len(allfirecount[i])//2)
        for j in range(1, (len(allclustercount[i])//2)+1):
            try:
                fires[j-1] = allfirecount[i][2*j]+allfirecount[i][2*j-1]
                simples[j-1] = (allfirecount[i][2*j]+allfirecount[i][2*j-1])-(allclustercount[i][2*j]+allclustercount[i][2*j-1])
            except KeyError:
                fires[j-1] = allfirecount[i][str(2*j)]+allfirecount[i][str(2*j-1)]
                simples[j-1] = (allfirecount[i][str(2*j)]+allfirecount[i][str(2*j-1)])-(allclustercount[i][str(2*j)]+allclustercount[i][str(2*j-1)])
        fires = fires[front[i]:-end[i]]
        simples = simples[front[i]:-end[i]]
        allfires.append(fires)
        allsimples.append(simples)
    fig, ax = plt.subplots(figsize=(20,10))
    #ax.plot(days, allfires[(len(allclustercount)-1)], 'r')
    #ax.plot(days, allsimples[(len(allclustercount)-1)], color='orange')
    plt.fill_between(days, allfires[(len(allclustercount)-1)], color='red', label='Complex')
    plt.fill_between(days, allsimples[(len(allclustercount)-1)], color='orange', label='Simple')
    ax.set_xticks(positions)
    ax.set_xticks(hals, minor=True)
    ax.set_xticklabels([])
    ax.set_xticklabels(labels, minor=True)
    ax.tick_params(axis='x', which='minor', length=0)
    plt.title('Simple and Complex Fires', fontsize=20)
    plt.ylabel('Number of Fires', fontsize=14)
    plt.legend(loc='upper right')
    plt.savefig(filepath+'/Plots/filledplot.pdf', bbox_inches='tight')
    plt.close()
"""

def getFireTypeFilledPlot(allclustercount, allfirecount, filepath):
    clusters = []
    simples = []
    days = np.arange(0, 366, 1)
    for i in range(0, len(allclustercount)):
        c = np.zeros(len(allclustercount[i]))
        s = np.zeros(len(allclustercount[i]))
        for j in range(0, len(allclustercount[i])):
            c[j] = allfirecount[i][str(j+1)]
            s[j] = allfirecount[i][str(j+1)]-allclustercount[i][str(j+1)]
        clusters.append(c)
        simples.append(s)
    fig, ax = plt.subplots(figsize=(20,10))
    plt.fill_between(days, clusters[5][front[5]:-end[5]], color='red', label='Complex', alpha=0.75)
    plt.fill_between(days, simples[5][front[5]:-end[5]], color='orange', label='Simple', alpha=0.5)
    ax.set_xticks(positions)
    ax.set_xticks(hals, minor=True)
    ax.set_xticklabels([])
    ax.set_xticklabels(labels, minor=True)
    ax.tick_params(axis='x', which='minor', length=0)
    plt.title('Number of Complex Fires', fontsize=20)
    plt.ylabel('Number of Complex Fires', fontsize=14)
    plt.legend(loc='upper right')
    plt.savefig(filepath+'/Plots/filledtypeplot.pdf', bbox_inches='tight')
    plt.close()
    
    
def plotLines(flts, filepath):
    fig, ax = plt.subplots(figsize=(8,5))
    y = 0
    for i in range(front[5], len(flts)-end[5]):
        for j in flts[i]:
            if len(j) == 0:
                ys = np.zeros(1)
                ys += y     
                a = np.arange(i, i+1, 1)
            else:
                ys = np.zeros(len(j))
                ys += y     
                a = np.arange(i, i+len(j), 1)
            ax.plot(a, ys, 'k')
            y += 1
    ax.set_xticks(positions)
    ax.set_xticks(hals, minor=True)
    ax.set_xticklabels([])
    ax.set_xticklabels(labels, minor=True)
    ax.tick_params(axis='x', which='minor', length=0)
    #plt.title('Fire group lifetimes', fontsize=20, fontweight='bold')
    plt.ylabel('Cumulative number of fire group', fontsize=14)
    plt.axvspan(21+aug-(d1-d0).days, sep-(d1-d0).days, color='b', alpha=0.1, lw=0)
    plt.savefig(filepath+'/Plots/longgrouplinesplot.pdf', bbox_inches='tight')
    plt.close()
    
    
def plotAugLines(flts, allfiresets, filepath):
    fig, ax = plt.subplots(figsize=(20,10))
    y = 0
    for i in range(aug, octo):
        for j in flts[i]:
            if len(j) == 0:
                ys = np.zeros(len(j)+1)
                ys += y     
                a = np.arange(i, i+len(j)+1, 1)
            else:
                ys = np.zeros(len(j))
                ys += y     
                a = np.arange(i, i+len(j), 1)
            ax.plot(a, ys, 'k')
            y += 1
    ax.set_xticks(netpositions)
    ax.set_xticks(nethals, minor=True)
    ax.set_xticklabels([])
    ax.set_xticklabels(netlabels, minor=True)
    ax.tick_params(axis='x', which='minor', length=0)
    plt.title('Number of complex fires', fontsize=20)
    plt.ylabel('Number of Complex Fires', fontsize=14)
    plt.savefig(filepath+'/Plots/auglinesplot.pdf', bbox_inches='tight')
    plt.close()
    
    
def getVCountPlot(vdata):
    rawdates = []
    for i in range(1811173, 2149064):
        rawdates.append(vdata['Date'][i])
    dates = matplotlib.dates.date2num(rawdates)
    dates = dates.tolist()
    count = np.zeros(366)
    for i in range(0, 366):
        count[i] = dates.count(i+18262)
    days = np.arange(0, 366, 1)
    fig, ax = plt.subplots(figsize=(20,10))
    ax.plot(days, count, 'k')
    ax.set_xticks(positions)
    ax.set_xticks(hals, minor=True)
    ax.set_xticklabels([])
    ax.set_xticklabels(labels, minor=True)
    ax.tick_params(axis='x', which='minor', length=0)
    plt.title('Daily Lightning Strikes', fontsize=20)
    plt.ylabel('Number of Lightning Strike', fontsize=14)
    plt.savefig('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Vaisala/countplot.pdf', bbox_inches='tight')
    plt.close()


def getAreaRollAvLightningPlot(allareacount, vdata, filepath):
    days = np.arange(0, 366, 1)
    fig, ax1 = plt.subplots(figsize=(20,10))
    rawdates = []
    for i in range(1811173, 2149064):
        rawdates.append(vdata['Date'][i])
    dates = matplotlib.dates.date2num(rawdates)
    dates = dates.tolist()
    count = np.zeros(366)
    for i in range(0, 366):
        count[i] = dates.count(i+18262)
    ax1.bar(days, count, color='blue', label='Daily Lightning Strikes')
    ax2 = ax1.twinx()
    a = allareacount[5][3][front[5]:-end[5]]
    ax2.plot(days, a, color='red', label='Total fire area')
    rollav = np.zeros(len(a)-14)
    for i in range(7, len(a)-7):
        av = 0
        for j in range(1, 8):
            av += a[i-j]+a[i+j]
        rollav[i-7] = (av+a[i])/15
    ax2.plot(days[7:-7], rollav, color='black', label='15 day rolling average')
    fiveav = np.zeros(len(allareacount[0][0]))
    for i in range(0, len(allareacount[0])-1):
        #ax.plot(days, allareacount[i][3][front[i]:-end[i]], color='blue')
        a = np.array(allareacount[i][3])
        fiveav += a
    fiveav = fiveav/5
    fiveav = fiveav[front[0]:-end[0]]
    ax1.set_xticks(positions)
    ax1.set_xticks(hals, minor=True)
    ax1.set_xticklabels([])
    ax1.set_xticklabels(labels, minor=True)
    ax1.tick_params(axis='x', which='minor', length=0)
    plt.title('Total Fire Area', fontsize=20)
    ax1.set_ylabel('Number of Lightning Strikes', color='black', fontsize=14)
    ax2.set_ylabel('Area of fires', color='black', fontsize=14)
    plt.legend(loc='upper right')
    colors = {'Daily Lightning Strikes':'blue', 'Total fire area':'red', '15 day rolling average':'black'}         
    elabels = list(colors.keys())
    handles = [plt.Rectangle((0,0),1,0, color=colors[label]) for label in elabels]
    plt.legend(handles, elabels)
    fig.tight_layout()
    plt.savefig(filepath+'/Plots/arearollavlightningplot.pdf', bbox_inches='tight')
    plt.close()
    
    
def getFiresLightningPlot(allfiresets, vdata, filepath):
    days = np.arange(0, 366, 1)
    fig, ax1 = plt.subplots(figsize=(20,10))
    rawdates = []
    for i in range(1811173, 2149064):
        if vdata['Tag'][i] == 'G':
            rawdates.append(vdata['Date'][i])
    dates = matplotlib.dates.date2num(rawdates)
    dates = dates.tolist()
    count = np.zeros(366)
    for i in range(0, 366):
        count[i] = dates.count(i+18262)
    ax1.bar(days, count, color='blue', label='Daily Lightning Strikes')
    ax2 = ax1.twinx()
    a = allfiresets[5][front[5]:-end[5]]
    fires = np.zeros(len(a))
    for i in range(0, 366):
        fires[i] = len(a[i])
    ax2.plot(days, fires, color='red', label='Total fire area')
    rollav = np.zeros(len(a)-14)
    for i in range(7, len(a)-7):
        av = 0
        for j in range(1, 8):
            av += fires[i-j]+fires[i+j]
        rollav[i-7] = (av+fires[i])/15
    ax2.plot(days[7:-7], rollav, color='black', label='15 day rolling average')
    ax1.set_xticks(positions)
    ax1.set_xticks(hals, minor=True)
    ax1.set_xticklabels([])
    ax1.set_xticklabels(labels, minor=True)
    ax1.tick_params(axis='x', which='minor', length=0)
    plt.title('Number of daily fires', fontsize=20)
    ax1.set_ylabel('Number of Lightning Strikes', color='black', fontsize=14)
    ax2.set_ylabel('Number of fires', color='black', fontsize=14)
    plt.legend(loc='upper right')
    colors = {'Daily Lightning Strikes':'blue', 'Total fire area':'red', '15 day rolling average':'black'}         
    elabels = list(colors.keys())
    handles = [plt.Rectangle((0,0),1,0, color=colors[label]) for label in elabels]
    plt.legend(handles, elabels)
    fig.tight_layout()
    plt.savefig(filepath+'/Plots/firelightningplot.pdf', bbox_inches='tight')
    plt.close()


def getGCLightningPlot(vdata, filepath):
    days = np.arange(0, 366, 1)
    fig, ax = plt.subplots(figsize=(20,10))
    rawdates = []
    crawdates = []
    for i in range(1811173, 2149064):
        if vdata['Tag'][i] == 'G':
            rawdates.append(vdata['Date'][i])
        else:
            crawdates.append(vdata['Date'][i])
    dates = matplotlib.dates.date2num(rawdates)
    dates = dates.tolist()
    count = np.zeros(366)
    cdates = matplotlib.dates.date2num(crawdates)
    cdates = cdates.tolist()
    ccount = np.zeros(366)
    for i in range(0, 366):
        count[i] = dates.count(i+18262)
        ccount[i] = cdates.count(i+18262)
    ax.bar(days, count, color='red', label='Ground strikes')
    ax.plot(days, ccount, color='blue', label='Cloud strikes')
    ax.set_xticks(positions)
    ax.set_xticks(hals, minor=True)
    ax.set_xticklabels([])
    ax.set_xticklabels(labels, minor=True)
    ax.tick_params(axis='x', which='minor', length=0)
    plt.title('Total Fire Area', fontsize=20)
    plt.ylabel('Number of Lightning Strikes', color='black', fontsize=14)
    plt.legend()
    fig.tight_layout()
    plt.savefig(filepath+'/Plots/gclightningplot.pdf', bbox_inches='tight')
    plt.close()
    

def getFiresDerivPlot(allfiresets, vdata, filepath):
    days = np.arange(0, 366, 1)
    fig, ax1 = plt.subplots(figsize=(20,10))
    rawdates = []
    for i in range(1811173, 2149064):
        if vdata['Tag'][i] == 'G':
            rawdates.append(vdata['Date'][i])
    dates = matplotlib.dates.date2num(rawdates)
    dates = dates.tolist()
    count = np.zeros(366)
    for i in range(0, 366):
        count[i] = dates.count(i+18262)
    ax1.bar(days, count, color='blue', label='Daily Lightning Strikes')
    ax2 = ax1.twinx()
    a = allfiresets[5][front[5]:-end[5]]
    fires = np.zeros(len(a))
    for i in range(1, 366):
        fires[i] = len(a[i])-len(a[i-1])
    ax2.plot(days, fires, color='red', label='Total fire area')
    rollav = np.zeros(len(a)-14)
    for i in range(7, len(a)-7):
        av = 0
        for j in range(1, 8):
            av += fires[i-j]+fires[i+j]
        rollav[i-7] = (av+fires[i])/15
    ax2.plot(days[7:-7], rollav, color='black', label='15 day rolling average')
    rollav = np.zeros(len(a)-6)
    for i in range(3, len(a)-3):
        av = 0
        for j in range(1, 4):
            av += fires[i-j]+fires[i+j]
        rollav[i-3] = (av+fires[i])/7
    ax2.plot(days[3:-3], rollav, color='green', label='15 day rolling average')
    ax1.set_xticks(positions)
    ax1.set_xticks(hals, minor=True)
    ax1.set_xticklabels([])
    ax1.set_xticklabels(labels, minor=True)
    ax1.tick_params(axis='x', which='minor', length=0)
    plt.title('Number of daily fires', fontsize=20)
    ax1.set_ylabel('Number of Lightning Strikes', color='black', fontsize=14)
    ax2.set_ylabel('Number of fires', color='black', fontsize=14)
    plt.legend(loc='upper right')
    colors = {'Daily Lightning Strikes':'blue', 'Total fire area':'red', '15 day rolling average':'black', '7 day rolling average':'green'}         
    elabels = list(colors.keys())
    handles = [plt.Rectangle((0,0),1,0, color=colors[label]) for label in elabels]
    plt.legend(handles, elabels)
    fig.tight_layout()
    plt.savefig(filepath+'/Plots/firederivplot.pdf', bbox_inches='tight')
    plt.close()
    
    
def plotLinesLightning(lifetimes, vdata, filepath):
    days = np.arange(0, 366, 1)
    fig, ax1 = plt.subplots(figsize=(20,10))
    rawdates = []
    for i in range(1811173, 2149064):
        if vdata['Tag'][i] == 'G':
            rawdates.append(vdata['Date'][i])
    dates = matplotlib.dates.date2num(rawdates)
    dates = dates.tolist()
    count = np.zeros(366)
    for i in range(0, 366):
        count[i] = dates.count(i+18262)
    ax1.bar(days, count, color='blue', label='Daily Lightning Strikes')
    ax2 = ax1.twinx()
    y = 0
    for i in range(front[5], len(lifetimes)-end[5]):
        for j in lifetimes[i]:
            ys = np.zeros(len(j))
            ys += y
            a = np.arange(i, i+len(j), 1)
            ax2.plot(a, ys, 'k')
            y += 1
    ax1.set_xticks(positions)
    ax1.set_xticks(hals, minor=True)
    ax1.set_xticklabels([])
    ax1.set_xticklabels(labels, minor=True)
    ax1.tick_params(axis='x', which='minor', length=0)
    plt.title('Number of Complex Fires', fontsize=20)
    plt.ylabel('Number of Complex Fires', fontsize=14)
    plt.axvspan(21+aug-(d1-d0).days, sep-(d1-d0).days, color='b', alpha=0.1, lw=0)
    #plt.legend(loc='upper right')
    plt.savefig(filepath+'/Plots/lineslightningplot.pdf', bbox_inches='tight')
    plt.close()
    
    
def getNetworkPlot(allfirecount, allfiresets, vdata, filepath):
    n = nx.Graph()
    nodes = {}
    t = 0
    for i in range(aug, octo+1):
        #l = allfirecount[5][str(i+1)]
        #s = 0 + 10*(l/2)
        s = 0
        for j in range(0, allfirecount[5][str(i+1)]):
            nodes[t] = (i, s)
            t += 1
            s -= len(allfiresets[5][i][j])**0.5
    n.add_nodes_from(nodes.keys())
    
    for p, q in nodes.items():
        n.nodes[p]['nodes'] = q
        
    def checkAcross(line, testset):
        x = 0    
        a = []
        def checkLine(line, x):
            if not set(line[x]).isdisjoint(testset):
                a.append(x)
            else:
                try:
                    a.append(x)
                    x += 1
                    checkLine(line, x)
                except IndexError:
                    a.append(x)
                    a.append(x+1)
            return a
        a = checkLine(line, x)
        
        if len(a) > len(line):
            a = -1
        else:
            a = max(a)
        return a
        
    def getEdges(line, testset):
        d = []
        def fullCheckAcross(line, testset):
            a = checkAcross(line, testset)
            if a != -1:
                d.append(a)
                line[a] = {-1}
                a = fullCheckAcross(line, testset)
            else:
                d.append(a)
            return d
        fullCheckAcross(line, testset)
        d.remove(-1)
        return d

    daycounter = aug
    firecounter = 0
    totalcount = 0
    for i in range(aug, octo):
        totalcount += allfirecount[5][str(daycounter+1)]
        day = allfiresets[5][i]
        nextday = allfiresets[5][i+1]
        for j in day:
            testset = set(j)
            line = nextday[:]
            e = getEdges(line, testset)
            for edge in e:
                n.add_edge(firecounter, totalcount+edge)
            firecounter += 1
        daycounter += 1
    sizes = []
    for i in range(aug, octo+1):
        for j in allfiresets[5][i]:
            sizes.append(len(j)*0.1)
    connections = np.zeros(len(nodes))
    for i in range(0, len(nodes)):
        for j in range(0, len(nodes)):
            if i<j:
                connections[i] += n.number_of_edges(i, j)
    fig, axs = plt.subplots(figsize=(12,5))
    nd = nx.draw_networkx_nodes(n, nodes, node_size=sizes, ax=axs, node_color=connections, cmap = plt.cm.hot)
    for i in range(0, len(nodes)):
        for j in range(0, len(nodes)):
            if i!=j and sizes[i] < 3 and sizes[j] < 3:
                try:
                    n.remove_edge(i, j)
                except:
                    pass
    nx.draw_networkx_edges(n, nodes, ax=axs, width=0.15)
    """
    days = np.arange(0, 366, 1)
    rawdates = []
    for i in range(0, len(vdata)):
        rawdates.append(vdata['Date'][i])
    dates = matplotlib.dates.date2num(rawdates)
    dates = dates.tolist()
    count = np.zeros(366)
    for i in range(0, 366):
        count[i] = dates.count(i+18262)
    axs[1].bar(days[aug:octo+1], count[aug:octo+1], color='blue', label='Daily Lightning Strikes')
    """
    axs.set_xticks(netpositions)
    axs.set_xticks(nethals, minor=True)
    axs.set_xticklabels([])
    axs.set_xticklabels(netlabels, minor=True, fontsize=14)
    axs.tick_params(left=False, bottom=True, labelleft=False, labelbottom=True, axis='x', which='minor', length=0)
    #axs.set_title('Map of fires across August and September', fontsize=20, fontweight='bold')
    """
    axs[1].set_xticks(netpositions)
    axs[1].set_xticks(nethals, minor=True)
    axs[1].set_xticklabels([])
    axs[1].set_xticklabels(netlabels, minor=True)
    axs[1].tick_params(left=False, bottom=True, labelleft=False, labelbottom=True, axis='x', which='minor', length=0)
    axs[1].set_title('Number of ground lightning strikes', fontweight='bold')
    """
    cbaxes = fig.add_axes([0.185, 0.225, 0.2, 0.01])
    cbar = plt.colorbar(nd, orientation='horizontal', cax=cbaxes)
    #cbar.outline.set_visible(False)
    cbar.set_label('Number of connections with following day', fontsize=8)
    axs.yaxis.grid(False)
    #plt.arrow(aug+19, -0.10, 0, -0.5, length_includes_head=True, head_width=0.8, head_length=0.2)
    plt.savefig(filepath+'/Plots/networkplot.pdf', bbox_inches='tight')
    plt.close()
    
"""  
def testPlot(allfirecount, allfiresets, filepath):
    days = np.arange(0, 366, 1)
    fig, ax = plt.subplots(figsize=(20,10))
    fires = np.zeros(len(allfirecount[5]))
    for i in range(0, len(fires)):
        fires[i] = allfirecount[5][str(i+1)]
    ax.plot(days, fires[front[5]:-end[5]], color='red', label='count')
    fires = np.zeros(len(allfiresets[5]))
    for i in range(0, len(fires)):
        fires[i] = len(allfiresets[5][i])
    ax.plot(days, fires[front[5]:-end[5]], color='black', label='sets')
    ax.set_xticks(positions)
    ax.set_xticks(hals, minor=True)
    ax.set_xticklabels([])
    ax.set_xticklabels(labels, minor=True)
    ax.tick_params(axis='x', which='minor', length=0)
    plt.title('Number of Fires', fontsize=20)
    plt.ylabel('Area [km$^2$]', fontsize=14)
    plt.legend(loc='upper right')
    plt.savefig(filepath+'/Plots/testplot.pdf', bbox_inches='tight')
    plt.close()
"""


def getLightningYearsPlot(vdata, filepath):
    years = ['2016-01-01', '2017-01-01', '2018-01-01', '2019-01-01', '2020-01-01']
    y = matplotlib.dates.date2num(years)
    y = y.tolist()
    days = np.arange(0, 366, 1)
    fig, axs = plt.subplots(2, figsize=(8,5))
    alldates = []
    for i in vdata:
        rawdates = []
        df = pd.read_csv(i, delimiter='\s+')
        for j in range(0, len(df)):
            rawdates.append(df['Date'][j])
        dates = matplotlib.dates.date2num(rawdates)
        dates = dates.tolist()
        alldates.append(dates)
    
    allcounts = []
    for i in range(0, len(vdata)):
        count = np.zeros(366)
        for j in range(0, len(count)):
            count[j] = alldates[i].count(j+y[i])
        allcounts.append(count)
    allweeks = []
    for i in allcounts:
        weeks = np.zeros(52)
        for j in range(0, len(weeks)):
            weeks[j] = i[7*j+0]+i[7*j+1]+i[7*j+2]+i[7*j+3]+i[7*j+4]+i[7*j+5]+i[7*j+6]
        allweeks.append(weeks)
    weekset = np.arange(0, 366, 7)
    weekset = weekset[:-1]
    for i in range(0, len(vdata)-1):
        ax = axs[0]
        ax.bar(weekset, allweeks[i], color='blue', width=7, alpha=0.25)
        #ax.set_ylim([0,35000])
        ax.set_xticks(positions)
        ax.set_xticks(hals, minor=True)
        ax.set_xticklabels([])
        ax.set_xticklabels(labels, minor=True)
        ax.tick_params(axis='x', which='minor', length=0)
    axs[0].set_title('2016-2019')
    i = 4
    ax = axs[1]
    ax.bar(weekset, allweeks[i], color='blue', width=7, alpha=0.5)
    #ax.set_ylim([0,35000])
    ax.set_xticks(positions)
    ax.set_xticks(hals, minor=True)
    ax.set_xticklabels([])
    ax.set_xticklabels(labels, minor=True)
    ax.tick_params(axis='x', which='minor', length=0)
    ax.set_title(str(2016+i))
    fig.text(0, 0.5, 'Number of ground strikes', va='center', rotation='vertical')
    fig.tight_layout()
    plt.savefig(filepath+'/Plots/lightningyearsplot.pdf', bbox_inches='tight')
    plt.close()
    
    
def getWildfiredataPlot(wildfiredata, filepath):
    labels = []
    for i in range(0, 21):
        labels.append(str(2000+i))
    labels.append('')
    positions = []
    for i in range(0, 22):
        positions.append(12*i)
    hals = []
    for i in range(0, 22):
        hals.append(6+(12*i))
    months = np.arange(0, len(wildfiredata), 1)
    acresburned  = np.zeros(len(wildfiredata))
    numberoffires = np.zeros(len(wildfiredata))
    abpf = np.zeros(len(wildfiredata))
    for i in range(0, len(acresburned)):
        acresburned[i] = wildfiredata['Acres Burned'][i]/1000000
        numberoffires[i] = wildfiredata['Number of Fires'][i]
        abpf[i] = wildfiredata['Acres Burned per Fire'][i]
    fig, axs = plt.subplots(3, figsize=(20,10))
    for i in range(0, 3):
        axs[i].set_xticks(positions)
        axs[i].set_xticks(hals, minor=True)
        axs[i].set_xticklabels([])
        axs[i].set_xticklabels(labels, minor=True)
    axs[0].bar(months, acresburned, color='blue')
    axs[0].set_title('Number of Acres Burned (millions)')
    axs[1].bar(months, numberoffires, color='blue')
    axs[1].set_title('Number of Fires')
    axs[2].bar(months, abpf, color='blue')
    axs[2].set_title('Acres Burned per Fire')
    fig.tight_layout()
    plt.savefig(filepath+'/Plots/wildfireplot.pdf', bbox_inches='tight')
    plt.close()


def getDailyGrowthPlot(alldailygrowth, filepath):
    days = np.arange(0, 366, 1)
    growth = np.asarray(alldailygrowth[5])[front[5]:-end[5]]
    fig, ax = plt.subplots(figsize=(20,10))
    ax.plot(days, growth, color='red', label='Daily increase in fire area')
    ax.set_xticks(positions)
    ax.set_xticks(hals, minor=True)
    ax.set_xticklabels([])
    ax.set_xticklabels(labels, minor=True)
    ax.tick_params(axis='x', which='minor', length=0)
    plt.title('Daily increase in fire area', fontsize=20)
    plt.ylabel('Increase in fire area', color='black', fontsize=14)
    plt.legend()
    fig.tight_layout()
    plt.savefig(filepath+'/Plots/growthplot.pdf', bbox_inches='tight')
    plt.close()
    

def getRegressionPlots(alldailygrowth, vdata, avtemps, maxtemps, mintemps, preci, evaps, filepath):
    standardgrowth = preprocessing.scale(alldailygrowth[5][front[5]:-end[5]])
    rawdates = []
    for i in range(0, len(vdata)):
        rawdates.append(vdata['Date'][i])
    dates = matplotlib.dates.date2num(rawdates)
    dates = dates.tolist()
    count = np.zeros(366)
    for i in range(0, 366):
        count[i] = dates.count(i+18262)
    weeklycount = np.zeros(366)
    for i in range(0, 7):
        weeklycount[i] = count[i]
    for i in range(7, len(count)):
        weeklycount[i] = np.sum(count[i-7:i])
    standardcount = preprocessing.scale(weeklycount)
    rlightning = pearsonr(standardcount, standardgrowth)
    ml, cl = np.polyfit(standardcount, standardgrowth, 1)
    standardtemp = preprocessing.scale(avtemps)
    rtemp = pearsonr(standardtemp, standardgrowth)
    mt, ct = np.polyfit(standardtemp, standardgrowth, 1)
    standardmax = preprocessing.scale(maxtemps)
    rmax = pearsonr(standardmax, standardgrowth)
    mmax, cmax = np.polyfit(standardmax, standardgrowth, 1)
    standardmin = preprocessing.scale(mintemps)
    rmin = pearsonr(standardmin, standardgrowth)
    mmin, cmin = np.polyfit(standardmin, standardgrowth, 1)
    standardp = preprocessing.scale(preci)
    rp = pearsonr(standardp, standardgrowth)
    mp, cp = np.polyfit(standardp, standardgrowth, 1)
    standardevap = preprocessing.scale(evaps)
    revap = pearsonr(standardevap, standardgrowth,)
    mevap, cevap = np.polyfit(standardevap, standardgrowth, 1)
    fig, axs = plt.subplots(2, 3, figsize=(20, 10))
    axs[0][0].scatter(standardcount, standardgrowth, s=1)
    axs[0][0].plot(standardcount, standardcount*ml+cl, 'r')
    axs[0][0].set_xlabel('Rolling weekly sum of lightning strikes (standardised)')
    axs[0][0].set_ylabel('Daily fire growth (standardised)')
    axs[0][0].set_title('Daily growth and weekly lightning strikes, r = '+str(round(rlightning[0], 2)), fontsize=12)
    axs[0][1].scatter(standardtemp, standardgrowth, s=1)
    axs[0][1].plot(standardtemp, standardtemp*mt+ct, 'r')
    axs[0][1].set_xlabel('Average daily temperature (standardised)')
    axs[0][1].set_ylabel('Daily fire growth (standardised)')
    axs[0][1].set_title('Daily growth and average temperature, r = '+str(round(rtemp[0], 2)), fontsize=12)
    axs[0][2].scatter(standardmax, standardgrowth, s=1)
    axs[0][2].plot(standardmax, standardmax*mmax+cmax, 'r')
    axs[0][2].set_xlabel('Average maximum daily temperature (standardised)')
    axs[0][2].set_ylabel('Daily fire growth (standardised)')
    axs[0][2].set_title('Daily growth and maximum temperature, r = '+str(round(rmax[0], 2)), fontsize=12)
    axs[1][0].scatter(standardmin, standardgrowth, s=1)
    axs[1][0].plot(standardmin, standardmin*mmin+cmin, 'r')
    axs[1][0].set_xlabel('Average minimum daily temperature (standardised)')
    axs[1][0].set_ylabel('Daily fire growth (standardised)')
    axs[1][0].set_title('Daily growth and minimum temperature, r = '+str(round(rmin[0], 2)), fontsize=12)
    axs[1][1].scatter(standardp, standardgrowth, s=1)
    axs[1][1].plot(standardp, standardp*mp+cp, 'r')
    axs[1][1].set_xlabel('Average daily precipitation (standardised)')
    axs[1][1].set_ylabel('Daily fire growth (standardised)')
    axs[1][1].set_title('Daily growth and average precipitation, r = '+str(round(rp[0], 2)), fontsize=12)
    axs[1][2].scatter(standardevap, standardgrowth, s=1)
    axs[1][2].plot(standardevap, standardevap*mevap+cevap, 'r')
    axs[1][2].set_xlabel('Average daily evaporation (standardised)')
    axs[1][2].set_ylabel('Daily fire growth (standardised)')
    axs[1][2].set_title('Daily growth and average evaporation, r = '+str(round(revap[0], 2)), fontsize=12)
    fig.suptitle('California State Variables', fontsize=20, fontweight='bold')
    plt.savefig(filepath+'/Plots/regressionplot.pdf', bbox_inches='tight')
    plt.close()
    
    
def getSonomaRegressionPlots(weeklygrowth, weeklycount, weeklyavt, weeklymaxt, weeklymint, filepath):
    standardgrowth = preprocessing.scale(weeklygrowth)
    standardcount = preprocessing.scale(weeklycount)
    rlightning = pearsonr(standardcount, standardgrowth)
    ml, cl = np.polyfit(standardcount, standardgrowth, 1)
    standardavt = preprocessing.scale(weeklyavt)
    ravt = pearsonr(standardavt, standardgrowth)
    mavt, cavt = np.polyfit(standardavt, standardgrowth, 1)
    standardmaxt = preprocessing.scale(weeklymaxt)
    rmax = pearsonr(standardmaxt, standardgrowth)
    mmax, cmax = np.polyfit(standardmaxt, standardgrowth, 1)
    standardmint = preprocessing.scale(weeklymint)
    rmin = pearsonr(standardmint, standardgrowth)
    mmin, cmin = np.polyfit(standardmint, standardgrowth, 1)
    fig, axs = plt.subplots(2, 2, figsize=(20, 10))
    axs[0][0].scatter(standardcount, standardgrowth, s=1)
    axs[0][0].plot(standardcount, standardcount*ml+cl, 'r')
    axs[0][0].set_xlabel('Rolling weekly sum of lightning strikes (standardised)')
    axs[0][0].set_ylabel('Daily fire growth (standardised)')
    axs[0][0].set_title('Daily growth and weekly lightning strikes, r = '+str(round(rlightning[0], 2)), fontsize=12)
    axs[0][1].scatter(standardavt, standardgrowth, s=1)
    axs[0][1].plot(standardavt, standardavt*mavt+cavt, 'r')
    axs[0][1].set_xlabel('Weekly average temperature (standardised)')
    axs[0][1].set_ylabel('Daily fire growth (standardised)')
    axs[0][1].set_title('Daily growth and weekly average temperature, r = '+str(round(ravt[0], 2)), fontsize=12)
    axs[1][0].scatter(standardmaxt, standardgrowth, s=1)
    axs[1][0].plot(standardmaxt, standardmaxt*mmax+cmax, 'r')
    axs[1][0].set_xlabel('Weekly maximum temperature (standardised)')
    axs[1][0].set_ylabel('Daily fire growth (standardised)')
    axs[1][0].set_title('Daily growth and weekly maximum temperature, r = '+str(round(rmax[0], 2)), fontsize=12)
    axs[1][1].scatter(standardmint, standardgrowth, s=1)
    axs[1][1].plot(standardmint, standardmint*mmin+cmin, 'r')
    axs[1][1].set_xlabel('Weekly minimum temperature (standardised)')
    axs[1][1].set_ylabel('Daily fire growth (standardised)')
    axs[1][1].set_title('Daily growth and weekly minimum temperature, r = '+str(round(rmin[0], 2)), fontsize=12)
    fig.suptitle('Sonoma County Variables', fontsize=20, fontweight='bold')
    plt.savefig(filepath+'/Plots/sonomaregressionplot.pdf', bbox_inches='tight')
    plt.close()


def getPCAPlot(final_df, filepath):
    pc1 = final_df[str(final_df.keys()[1])].to_numpy()
    pc2 = final_df[str(final_df.keys()[2])].to_numpy()
    name = final_df[str(final_df.keys()[6])].to_numpy()
    absgrowth = final_df[str(final_df.keys()[4])].to_numpy()
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list('', ['blue', 'red'])
    fig, ax = plt.subplots(figsize=(8,5))
    ax.scatter(pc1, pc2, c=absgrowth, cmap=cmap)
    #for i, txt in enumerate(name):
        #ax.annotate(txt, (pc1[i]+0.025, pc2[i]+0.025), fontsize=8)
    ax.set_xlabel('PC1', fontsize=12, fontweight='bold')
    ax.set_ylabel('PC2', fontsize=12, fontweight='bold')
    #plt.title('Principal Component Analysis of meteorological factors', fontsize=20, fontweight='bold')
    #ax.legend()
    plt.savefig(filepath+'/Plots/PCAplot.pdf', bbox_inches='tight')
    plt.close()


def getScreePlot(ratio, filepath):
    x = [1, 2]
    fig, ax = plt.subplots(figsize=(20,10))
    ax.bar(x, ratio)
    plt.savefig(filepath+'/Plots/screeplot.pdf', bbox_inches='tight')
    plt.close()


def getNOAAPlotsJASTemp(dfs, filepath):
    days = np.arange(0, 366, 1)
    fig, axs = plt.subplots(len(dfs), figsize=(20,10))
    for i in range(0, len(dfs)):
        tmax = dfs[i]['TMAX'].to_numpy()
        tmin = dfs[i]['TMIN'].to_numpy()
        tavg = dfs[i]['TAVG'].to_numpy()
        axs[i].plot(days[jul:octo], tmax, color='red')
        axs[i].plot(days[jul:octo], tmin, color='blue')
        axs[i].plot(days[jul:octo], tavg, color='green')
        axs[i].set_xticks(noaapositions)
        axs[i].set_xticks(noaahals, minor=True)
        axs[i].set_xticklabels([])
        axs[i].set_xticklabels(noaalabels, minor=True)
        axs[i].set_ylabel('C')
        axs[i].set_ylim(0, 40)
        axs[i].set_yticks([0, 10, 20, 30, 40])
        axs[i].set_title(dfs[i]['Date'][0][0:4])
    fig.suptitle('NOAA temperature data', fontsize=20, fontweight='bold')
    fig.tight_layout()
    plt.savefig(filepath+'/Plots/sonomanoaatemp.pdf', bbox_inches='tight')
    plt.close()
    

def getNOAAPlotsJASTempAvs(dfs, filepath):
    days = np.arange(0, 366, 1)
    fig, axs = plt.subplots(3, figsize=(8,5))
    tmax = np.zeros(len(dfs[0]))
    tmin = np.zeros(len(dfs[0]))
    tavg = np.zeros(len(dfs[0]))
    for i in range(0, len(dfs)-1):
        tmax += dfs[i]['TMAX'].to_numpy()
        tmin += dfs[i]['TMIN'].to_numpy()
        tavg += dfs[i]['TAVG'].to_numpy()
    tmax /= 5
    tmin /= 5
    tavg /= 5
    axs[0].plot(days[jul:octo], dfs[5]['TMAX'].to_numpy(), label='2020', color='red')
    axs[1].plot(days[jul:octo], dfs[5]['TMIN'].to_numpy(), label='2020', color='blue')
    axs[2].plot(days[jul:octo], dfs[5]['TAVG'].to_numpy(), label='2020', color=green)
    axs[0].plot(days[jul:octo], tmax, label='5 year average', color='black', linestyle='dashed')
    axs[1].plot(days[jul:octo], tmin, label='5 year average', color='black', linestyle='dashed')
    axs[2].plot(days[jul:octo], tavg, label='5 year average', color='black', linestyle='dashed')
    for i in range(0, 3):
        axs[i].set_xticks(noaapositions)
        axs[i].set_xticks(noaahals, minor=True)
        axs[i].set_xticklabels([])
        axs[i].set_xticklabels(noaalabels, minor=True)
        axs[i].set_ylabel('Temperature ($^\circ$C)')
        axs[i].legend(loc='upper right', fontsize=7.75)
    axs[0].set_title('Maximum temperature', fontweight='bold')
    axs[1].set_title('Minimum temperature', fontweight='bold')
    axs[2].set_title('Average temperature', fontweight='bold')
    #fig.suptitle('NOAA temperature data for Sonoma county', fontsize=20, fontweight='bold')
    fig.tight_layout()
    plt.savefig(filepath+'/Plots/noaatempavs.pdf', bbox_inches='tight')
    plt.close()
    
    
def getNOAAPlotsJASOthers(dfs, filepath):
    days = np.arange(0, 366, 1)
    fig, axs = plt.subplots(3, figsize=(8,5))
    awnd = np.zeros(len(dfs[0]))
    evap = np.zeros(len(dfs[0]))
    prcp = np.zeros(len(dfs[0]))
    for i in range(0, len(dfs)-1):
        awnd += dfs[i]['AWND'].to_numpy()
        prcp += dfs[i]['PRCP'].to_numpy()
        evap += dfs[i]['EVAP'].to_numpy()
    awnd /= 5
    evap /= 5
    prcp /= 5
    axs[0].bar(days[jul:octo], dfs[5]['AWND'].to_numpy(), label='2020', color='red')
    axs[1].bar(days[jul:octo], dfs[5]['PRCP'].to_numpy(), label='2020', color='blue')
    axs[2].bar(days[jul:octo], dfs[5]['EVAP'].to_numpy(), label='2020', color=green)
    axs[0].plot(days[jul:octo], awnd, label='5 year average', color='black', linestyle='dashed')
    axs[1].plot(days[jul:octo], prcp, label='5 year average', color='black', linestyle='dashed')
    axs[2].plot(days[jul:octo], evap, label='5 years average', color='black', linestyle='dashed')
    for i in range(0, 3):
        axs[i].set_xticks(noaapositions)
        axs[i].set_xticks(noaahals, minor=True)
        axs[i].set_xticklabels([])
        axs[i].set_xticklabels(noaalabels, minor=True)
        axs[i].legend(loc='upper left')
    axs[0].set_ylim(0, 8)
    axs[0].set_title('Average wind speed', fontweight='bold')
    axs[1].set_title('Precipitation', fontweight='bold')
    axs[0].set_ylabel('Wind speed (m/s)')
    axs[1].set_ylabel('Rainfall (mm)')
    axs[2].set_title('Evaporation', fontweight='bold')
    axs[2].set_ylabel('Evaporation (mm)')
    #fig.suptitle('Other NOAA data for Sonoma county', fontsize=20, fontweight='bold')
    fig.tight_layout()
    plt.savefig(filepath+'/Plots/noaaothers.pdf', bbox_inches='tight')
    plt.close()
        

def getCumulativeGroupPlot(alllifetimes, filepath):
    days = np.arange(0, 366, 1)
    fig, ax = plt.subplots(figsize=(8,5))
    sample = []
    avcount = np.zeros(366)
    for i in range(0, len(alllifetimes)-1):
        count = np.zeros(366)
        c = 0
        for j in range(0, len(alllifetimes[i])):
            c += len(alllifetimes[i][j])
            count[j] = c
        sample.append(count[-1])
        avcount += count
        ax.plot(days, count, color='black')
        x = 0
        if i == 0:
            x += 100
        if i == 1:
            x -= 65
        if i == 2:
            x -= 25
        if i == 3:
            x -= 85
        if i == 4:
            x -= 165
        ax.text(days[365]+3, count[365]+x, str(2015+i))
    avcount /= 5
    print('Av = '+str(avcount[365]))
    ax.plot(days, avcount, color=green)
    ax.text(days[365]+3, avcount[365]-50, 'Mean')
    count = np.zeros(366)
    c = 0
    for j in range(0, len(alllifetimes[5])):
        c += len(alllifetimes[5][j])
        count[j] = c
    sample.append(count[-1])
    ax.plot(days, count, color='red')
    print('2020 = '+str(count[365]))
    ax.text(days[365]+3, count[365]-50, str(2020))
    ax.set_xticks(positions)
    ax.set_xticks(hals, minor=True)
    ax.set_xticklabels([])
    ax.set_xticklabels(labels, minor=True)
    ax.tick_params(axis='x', which='minor', length=0)
    ax.set_xlim(-10, 395)
    #plt.title('Cumulative fire count', fontsize=20, fontweight='bold')
    plt.ylabel('Number of fire groups', fontsize=14)
    plt.savefig(filepath+'/Plots/cumulativegroupplot.pdf', bbox_inches='tight')
    plt.close()
    return sample









