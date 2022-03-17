#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 21:13:01 2021

@author: BenButcher
"""
import pandas as pd
import re
import numpy as np
import matplotlib.dates as md

def loadData(filepath='/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Vaisala/'):
    vdata = pd.read_csv(filepath, delimiter='\s+')
    return vdata

sixvdata = loadData('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Vaisala/gstrikes2016.csv')
svdata = loadData('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Vaisala/gstrikes2017.csv')
evdata = loadData('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Vaisala/gstrikes2018.csv')
nvdata = loadData('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Vaisala/gstrikes2019.csv')
vdata = loadData('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Vaisala/gstrikes2020.csv')

allvdata = [sixvdata, svdata, evdata, nvdata, vdata]
"""
for i in range(0, len(vdata)):
        print('collating...'+str(round(i*100/len(vdata), 2))+'%', end='\r')
        if vdata['Tag'][i] == 'C':
            vdata = vdata.drop(i)

vdata.to_csv('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Vaisala/gstrikes.csv', sep='\t')

date = []
time = []
lat = []
long = []
tag = []
charge = []

for i in range(0, len(vdata)):
    print('collating...'+str(round((i)*100/len(vdata), 2))+'%', end='\r')
    pattern = re.compile('2020-08-\d+')
    a = pattern.search(vdata['Date'][i])
    if vdata['Tag'][i] == 'G' and a and vdata['Charge'][i] < 0:
        date.append(vdata['Date'][i])
        time.append(vdata['Time'][i])
        lat.append(vdata['Lat'][i])
        long.append(vdata['Long'][i])
        tag.append(vdata['Tag'][i])
        charge.append(abs(vdata['Charge'][i]))

d = {'Date':date, 'Time':time, 'Lat':lat, 'Long':long, 'Charge':charge, 'Tag':tag}
vdata = pd.DataFrame(data=d)
vdata.to_csv('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Vaisala/negaug2020charge.csv', sep='\t')
"""

#df = vdata[11465:36621]

#df.to_csv('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Vaisala/sonomatime.csv', sep='\t')

df = pd.read_csv('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/QGIS/napa clipped ls.csv')

count = np.zeros(366)
for index, row in df.iterrows():
    date = row['Date']
    date = date.replace('/', '-')
    d = md.date2num([date])[0]
    a = int(d-18262)
    count[a] += 1
scount = count[208:248]
nweeklycount = np.zeros(5)
for i in range(0, 5):
    nweeklycount[i] = np.sum(scount[7*i:7*i+7])