#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 11:40:20 2021

@author: BenButcher
"""
import pandas as pd
import numpy as np
import matplotlib.dates as md
import re
"""
df1 = pd.read_csv('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/2020first.csv', sep='\t')
df2 = pd.read_csv('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/2020second.csv', sep='\t')
df3 = pd.read_csv('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/2020third.csv', sep='\t')
df4 = pd.read_csv('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/2020fourth.csv', sep='\t')

df = pd.concat([df1, df2, df3, df4])

lat = []
long = []
date = []
names = []
tmax = []
tavg = []


i = 0

while i < len(df):
    nam = df['NAME'][i]
    a = df[df['NAME'] == nam]
    try:
        tmax.append(a.loc[a['TMAX'].idxmax()]['TMAX'])
        date.append(a.loc[a['TMAX'].idxmax()]['DATE'])
        lat.append(df['LATITUDE'][i])
        long.append(df['LONGITUDE'][i])
        names.append(nam)
    except KeyError:
        pass
    
    i += len(a)

for i in range(0, len(df)):
    if df['TAVG'][i] > 0:
        lat.append(df['LATITUDE'][i])
        long.append(df['LONGITUDE'][i])
        names.append(df['NAME'][i])
        date.append(df['DATE'][i])
        tavg.append(df['TAVG'][i])


for i in range(18262, )
d = {'Station':names, 'Date':date, 'Latitude':lat, 'Longitude':long, 'TAVG':tavg}

newdf = pd.DataFrame(data=d)
newdf.to_csv('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/tavg data.csv', sep='\t')

tavg = np.zeros(366)
tcount = np.zeros(366)
for index, row in df.iterrows():
    d = md.date2num([row['DATE']])[0]
    if row['TAVG'] == row['TAVG']:
        a = int(d-18262)
        tavg[a] += row['TAVG']
        tcount[a] += 1
avtemps = tavg/tcount

tmax = np.zeros(366)
tcount = np.zeros(366)
for index, row in df.iterrows():
    d = md.date2num([row['DATE']])[0]
    if row['TMAX'] == row['TMAX']:
        a = int(d-18262)
        tmax[a] += row['TMAX']
        tcount[a] += 1
maxtemps = tmax/tcount

tmin = np.zeros(366)
tcount = np.zeros(366)
for index, row in df.iterrows():
    d = md.date2num([row['DATE']])[0]
    if row['TMIN'] == row['TMIN']:
        a = int(d-18262)
        tmin[a] += row['TMIN']
        tcount[a] += 1
mintemps = tmin/tcount

prcp = np.zeros(366)
tcount = np.zeros(366)
for index, row in df.iterrows():
    d = md.date2num([row['DATE']])[0]
    if row['PRCP'] == row['PRCP']:
        a = int(d-18262)
        prcp[a] += row['PRCP']
        tcount[a] += 1
preci = prcp/tcount

evap = np.zeros(366)
tcount = np.zeros(366)
for index, row in df.iterrows():
    d = md.date2num([row['DATE']])[0]
    if row['EVAP'] == row['EVAP']:
        a = int(d-18262)
        evap[a] += row['EVAP']
        tcount[a] += 1
evaps = evap/tcount

df = pd.read_csv('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/napa.csv', sep='\t')

tavg = np.zeros(366)
tcount = np.zeros(366)
for index, row in df.iterrows():
    d = md.date2num([row['DATE']])[0]
    if row['TAVG'] == row['TAVG']:
        a = int(d-18262)
        tavg[a] += row['TAVG']
        tcount[a] += 1
savtemps = tavg[208:248]/tcount[208:248]
weeklyavt = np.zeros(5)
for i in range(0, 5):
    weeklyavt[i] = np.sum(savtemps[7*i:7*i+7])/7

tmax = np.zeros(366)
tcount = np.zeros(366)
for index, row in df.iterrows():
    d = md.date2num([row['DATE']])[0]
    if row['TMAX'] == row['TMAX']:
        a = int(d-18262)
        tmax[a] += row['TMAX']
        tcount[a] += 1
stmax = tmax[208:248]/tcount[208:248]
weeklymaxt = np.zeros(5)
for i in range(0, 5):
    weeklymaxt[i] = np.sum(stmax[7*i:7*i+7])/7

tmin = np.zeros(366)
tcount = np.zeros(366)
for index, row in df.iterrows():
    d = md.date2num([row['DATE']])[0]
    if row['TMIN'] == row['TMIN']:
        a = int(d-18262)
        tmin[a] += row['TMIN']
        tcount[a] += 1
stmin = tmin[208:248]/tcount[208:248]
weeklymint = np.zeros(5)
for i in range(0, 5):
    weeklymint[i] = np.sum(stmin[7*i:7*i+7])/7

prcp = np.zeros(366)
tcount = np.zeros(366)
for index, row in df.iterrows():
    d = md.date2num([row['DATE']])[0]
    if row['PRCP'] == row['PRCP']:
        a = int(d-18262)
        prcp[a] += row['TMIN']
        tcount[a] += 1
sprcp = prcp[208:248]/tcount[208:248]
weeklyprcp = np.zeros(5)
for i in range(0, 5):
    weeklyprcp[i] = np.sum(sprcp[7*i:7*i+7])/7


df5 = pd.read_csv('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/juaugsept5.csv', sep='\t')
df6 = pd.read_csv('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/juaugsept6.csv', sep='\t')
df7 = pd.read_csv('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/juaugsept7.csv', sep='\t')
df8 = pd.read_csv('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/juaugsept8.csv', sep='\t')
df9 = pd.read_csv('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/juaugsept9.csv', sep='\t')
df = pd.read_csv('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/juaugsept.csv', sep='\t')

csvnames = ['/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/jas5.csv',
            '/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/jas6.csv',
            '/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/jas7.csv',
            '/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/jas8.csv',
            '/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/jas9.csv',
            '/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/jas.csv']

dfnames = [df5, df6, df7, df8, df9, df]

for j in range(0, 6):
    maximumtemps = []
    minimumtemps = []
    averagetemps = []
    averagewind = []
    evaporation = []
    precipitation = []
    df = dfnames[j]
    dates = df['DATE'][:92].tolist()
    
    for i in dates:
        a = df[df['DATE'] == i]
        tmax = a['TMAX'].to_numpy()
        tmax = tmax[np.logical_not(np.isnan(tmax))]
        maximumtemps.append(np.mean(tmax))
        tmin = a['TMIN'].to_numpy()
        tmin = tmin[np.logical_not(np.isnan(tmin))]
        minimumtemps.append(np.mean(tmin))
        tavg = a['TAVG'].to_numpy()
        tavg = tavg[np.logical_not(np.isnan(tavg))]
        averagetemps.append(np.mean(tavg))
        awnd = a['AWND'].to_numpy()
        awnd = awnd[np.logical_not(np.isnan(awnd))]
        averagewind.append(np.mean(awnd))
        evap = a['EVAP'].to_numpy()
        evap = evap[np.logical_not(np.isnan(evap))]
        evaporation.append(np.mean(evap))
        prcp = a['PRCP'].to_numpy()
        prcp = prcp[np.logical_not(np.isnan(prcp))]
        precipitation.append(np.mean(prcp))
        
    data = {'Date':dates, 'TMAX':maximumtemps, 'TMIN':minimumtemps, 'TAVG':averagetemps, 'AWND':averagewind, 'EVAP':evaporation, 'PRCP':precipitation}
    
    new_df = pd.DataFrame(data)
    
    new_df.to_csv(csvnames[j], sep='\t')
    
"""

df = pd.read_csv('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/jas.csv', sep='\t')
df5 = pd.read_csv('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/jas5.csv', sep='\t')
df6 = pd.read_csv('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/jas6.csv', sep='\t')
df7 = pd.read_csv('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/jas7.csv', sep='\t')
df8 = pd.read_csv('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/jas8.csv', sep='\t')
df9 = pd.read_csv('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/jas9.csv', sep='\t')

dfs = (df5, df6, df7, df8, df9, df)

"""

df5 = pd.read_csv('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/sonomamonths15.csv', sep='\t')
df6 = pd.read_csv('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/sonomamonths16.csv', sep='\t')
df7 = pd.read_csv('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/sonomamonths17.csv', sep='\t')
df8 = pd.read_csv('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/sonomamonths18.csv', sep='\t')
df9 = pd.read_csv('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/sonomamonths19.csv', sep='\t')
df = pd.read_csv('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/sonomamonths.csv', sep='\t')

csvnames = ['/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/s5.csv',
            '/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/s6.csv',
            '/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/s7.csv',
            '/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/s8.csv',
            '/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/s9.csv',
            '/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/son.csv']

dfnames = [df5, df6, df7, df8, df9, df]

for j in range(0, 6):
    maximumtemps = []
    minimumtemps = []
    averagetemps = []
    averagewind = []
    precipitation = []
    df = dfnames[j]
    dates = df['DATE'][:92].tolist()
    
    for i in dates:
        a = df[df['DATE'] == i]
        tmax = a['TMAX'].to_numpy()
        tmax = tmax[np.logical_not(np.isnan(tmax))]
        maximumtemps.append(np.mean(tmax))
        tmin = a['TMIN'].to_numpy()
        tmin = tmin[np.logical_not(np.isnan(tmin))]
        minimumtemps.append(np.mean(tmin))
        tavg = a['TAVG'].to_numpy()
        tavg = tavg[np.logical_not(np.isnan(tavg))]
        averagetemps.append(np.mean(tavg))
        awnd = a['AWND'].to_numpy()
        awnd = awnd[np.logical_not(np.isnan(awnd))]
        averagewind.append(np.mean(awnd))
        prcp = a['PRCP'].to_numpy()
        prcp = prcp[np.logical_not(np.isnan(prcp))]
        precipitation.append(np.mean(prcp))
        
    data = {'Date':dates, 'TMAX':maximumtemps, 'TMIN':minimumtemps, 'TAVG':averagetemps, 'AWND':averagewind, 'PRCP':precipitation}
    
    new_df = pd.DataFrame(data)
    
    new_df.to_csv(csvnames[j], sep='\t')


df5 = pd.read_csv('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/s5.csv', sep='\t')
df6 = pd.read_csv('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/s6.csv', sep='\t')
df7 = pd.read_csv('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/s7.csv', sep='\t')
df8 = pd.read_csv('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/s8.csv', sep='\t')
df9 = pd.read_csv('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/s9.csv', sep='\t')
df = pd.read_csv('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/son.csv', sep='\t')

dfs = (df5, df6, df7, df8, df9, df)



tm = pd.read_csv('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/NOAA California/2020months.csv', sep='\t')

lat = []
long = []
prcp = []
dates = []

for i in range(0, len(tm)):
    date = tm['DATE'][i]
    pattern = re.compile('2020-08-\d+')
    if pattern.search(date) and tm['PRCP'][i]==tm['PRCP'][i] and tm['PRCP'][i]!=0:
        lat.append(tm['LATITUDE'][i])
        long.append(tm['LONGITUDE'][i])
        prcp.append(tm['PRCP'][i])
        dates.append(date)
        
data = {'Date':dates, 'Latitude':lat, 'Longitude':long, 'Precipitation':prcp}

new_df = pd.DataFrame(data)
"""












