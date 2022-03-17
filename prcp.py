#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 12:55:39 2021

@author: BenButcher
"""
import pandas as pd

data = pd.read_csv('https://www.ncei.noaa.gov/orders/cdo/2457813.csv')

data.to_csv(r'/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/2020.csv', index=False)

prcp = data['PRCP']

dates = data['DATE']
juls = []
augs = []
septs = []

for i in range(0, len(data)):
    if dates[i] == '2020-07':
        juls.append(i)
    if dates[i] == '2020-08':
        augs.append(i)
    if dates[i] == '2020-09':
        septs.append(i)
        
jultotal = 0
augtotal = 0
septotal = 0

for i in juls:
    p = prcp[i]
    if p == p:
        jultotal += p
        
for i in augs:
    p = prcp[i]
    if p == p:
        augtotal += p
        
for i in septs:
    p = prcp[i]
    if p == p:
        septotal += p
    
print('July: '+str(round(jultotal, 2))+'mm')
print('August: '+str(round(augtotal, 2))+'mm')
print('Septemnber: '+str(round(septotal, 2))+'mm')
    