#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 21:13:01 2021

@author: BenButcher
"""
import pandas as pd

def loadData(filepath='/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Vaisala/vtext.txt'):
    vdata = pd.read_csv(filepath, delimiter='\s+')
    return vdata

vdata = loadData()
"""
for i in range(0, len(vdata)):
        print('collating...'+str(round(i*100/len(vdata), 2))+'%', end='\r')
        if vdata['Tag'][i] == 'C':
            vdata = vdata.drop(i)

vdata.to_csv('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Vaisala/gstrikes.csv', sep='\t')
"""
date = []
time = []
lat = []
long = []
tag = []

for i in range(2000017, 2141044):
    print('collating...'+str(round((i-2000017)*100/(2141044-2000017), 2))+'%', end='\r')
    if vdata['Tag'][i] == 'G':
        date.append(vdata['Date'][i])
        time.append(vdata['Time'][i])
        lat.append(vdata['Lat'][i])
        long.append(vdata['Long'][i])
        tag.append(vdata['Tag'][i])

d = {'Date':date, 'Time':time, 'Lat':lat, 'Long':long, 'Tag':tag}
vdata = pd.DataFrame(data=d)
vdata.to_csv('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Vaisala/gstrikesaug.csv', sep='\t')