#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 11:46:31 2021

@author: BenButcher
"""

import re
import numpy as np
import glob
import json
import codecs

def getFilenames(filepath):
    """ Collects filenames in the directory and sorts them in date order"""

    directory = filepath+'/MOD14*.hdf'
    filenames = glob.glob(directory)  # gathers hdf filenames
    filenames.sort()
    
    return filenames


def splitFilenames(filenames):
    for i in range(0, len(filenames)):
        afiles = []
        bfiles = []
        cfiles = []
        dfiles = []
        efiles = []
        ffiles = []
        gfiles = []
    for i in range(0, len(filenames)):
        if i < 15:
            afiles.append(filenames[i])
        else:
            afiles.append('')
        if 15 <= i < 30:
            bfiles.append(filenames[i])
        else:
            bfiles.append('')
        if 30 <= i < 45:
            cfiles.append(filenames[i])
        else:
            cfiles.append('')
        if 45 <= i < 60:
            dfiles.append(filenames[i])
        else:
            dfiles.append('')
        if 60 <= i < 75:
            efiles.append(filenames[i])
        else:
            efiles.append('')
        if 75 <= i < 90:
            ffiles.append(filenames[i])
        else:
            ffiles.append('')
        if 90 <= i:
            gfiles.append(filenames[i])
        else:
            gfiles.append('')
            
    return afiles, bfiles, cfiles, dfiles, efiles, ffiles, gfiles


def saveData(allfiregroups):
    #with open('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Plot Data/alldayarea', 'w') as fout:
        #json.dump(alldayarea, fout)
    #with open('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Plot Data/allfirecount', 'w') as fout:
        #json.dump(allfirecount, fout)
    #with open('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Plot Data/allfiredata', 'w') as fout:
        #json.dump(allfiredata, fout)
    #with open('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Plot Data/allcontourdata', 'w') as fout:
        #json.dump(allcontourdata, fout)
    #with open('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Plot Data/allclustercount', 'w') as fout:
        #json.dump(allclustercount, fout)
    #with open('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Plot Data/allareacount', 'w') as fout:
        #json.dump(allareacount, fout)
    #with open('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Plot Data/allclustercount', 'w') as fout:
        #json.dump(allclustercount, fout)
    #with open('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Plot Data/allclusterdata', 'w') as fout:
        #json.dump(allclusterdata, fout)
    #with open('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Plot Data/allcarea', 'w') as fout:
        #json.dump(allcarea, fout)
    #with open('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Plot Data/allfiresets', 'w') as fout:
        #json.dump(allfiresets, fout)
    #with open('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Plot Data/sortedfiresets', 'w') as fout:
        #json.dump(sortedfiresets, fout)
    #with open('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Plot Data/newfiresets', 'w') as fout:
        #json.dump(newfiresets, fout)
    #with open('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Plot Data/alllongfiresets', 'w') as fout:
        #json.dump(alllongfiresets, fout)
    with open('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Plot Data/allfiregroups', 'w') as fout:
        json.dump(allfiregroups, fout)
    #with open('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Plot Data/allgroupcount', 'w') as fout:
        #json.dump(allgroupcount, fout) 
    #with open('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Plot Data/avtemps', 'w') as fout:
        #json.dump(list(avtemps[:]), fout) 
    #with open('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Plot Data/maxtemps', 'w') as fout:
        #json.dump(list(maxtemps[:]), fout) 
    #with open('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Plot Data/mintemps', 'w') as fout:
        #json.dump(list(mintemps[:]), fout) 
    #with open('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Plot Data/precip', 'w') as fout:
        #json.dump(list(precip[:]), fout) 
    #with open('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Plot Data/evaps', 'w') as fout:
        #json.dump(list(evaps[:]), fout) 
    #with open('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Plot Data/newcount', 'w') as fout:
        #json.dump(newcount, fout) 
    #with open('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Plot Data/allcomplexcount', 'w') as fout:
        #json.dump(allcomplexcount, fout) 
      
        
def saveImageData(allcontourdata):
    for i in range(0, len(allcontourdata)):
        for j in range(0, len(allcontourdata[i])):
            try:
                if allcontourdata[i][j+1] != []:
                    for k in range(0, len(allcontourdata[i][j+1])):
                        if type(allcontourdata[i][j+1][k]) == np.ndarray:
                            a = allcontourdata[i][j+1][k]
                            allcontourdata[i][j+1][k] = a.tolist()
            except KeyError:
                if allcontourdata[i][str(j+1)] != []:
                    for k in range(0, len(allcontourdata[i][str(j+1)])):
                        if type(allcontourdata[i][str(j+1)][k]) == np.ndarray:
                            a = allcontourdata[i][str(j+1)][k]
                            allcontourdata[i][str(j+1)][k] = a.tolist()
    json.dump(allcontourdata, codecs.open('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Image Data/allcontourdata', 'w', encoding='utf-8'), separators=(',', ':'), sort_keys=True, indent=4)
        
def readPlotData():
    with open('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Plot Data/allareacount') as json_file:
        allareacount = json.load(json_file)
    with open('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Plot Data/allcarea') as json_file:
        allcarea = json.load(json_file)
    with open('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Plot Data/allclustercount') as json_file:
        allclustercount = json.load(json_file)
    with open('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Plot Data/alldayarea') as json_file:
        alldayarea = json.load(json_file)
    with open('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Plot Data/allfirecount') as json_file:
        allfirecount = json.load(json_file)
    with open('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Plot Data/allfiredata') as json_file:
        allfiredata = json.load(json_file)
    with open('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Plot Data/allcontourdata') as json_file:
        allcontourdata = json.load(json_file)
    with open('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Plot Data/allclusterdata') as json_file:
        allclusterdata = json.load(json_file)
    with open('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Plot Data/allfiresets') as json_file:
        allfiresets = json.load(json_file)
    with open('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Plot Data/sortedfiresets') as json_file:
        sortedfiresets = json.load(json_file)
    with open('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Plot Data/newfiresets') as json_file:
        newfiresets = json.load(json_file)
    with open('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Plot Data/alllongfiresets') as json_file:
        alllongfiresets = json.load(json_file)
    with open('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Plot Data/allfiregroups') as json_file:
        allfiregroups = json.load(json_file)
    with open('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Plot Data/allgroupcount') as json_file:
        allgroupcount = json.load(json_file)
    #with open('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Plot Data/wildfiredata.csv') as json_file:
        #wildfiredata = json.load(json_file)
    #with open('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Plot Data/newcount') as json_file:
        #newcount = json.load(json_file)    
    return allareacount, allcarea, allclustercount, alldayarea, allfirecount, allfiredata, allcontourdata, allclusterdata, allfiresets, sortedfiresets, newfiresets, alllongfiresets, allfiregroups, allgroupcount#, newcount#, wildfiredata
    

def readImageData(datapath='/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Image Data/*'):
    datafiles = glob.glob('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/Data/Image Data/*')
    datafiles.sort()
    allcontourdata = codecs.open(datafiles[0], 'r', encoding='utf-8').read()
    json.loads(allcontourdata)
    for i in range(0, len(allcontourdata)):
        for j in range(0, len(allcontourdata[i])):
            if allcontourdata[i][j] != []:
                for k in range(0, len(allcontourdata[i][j])):
                    if type(allcontourdata[i][j][k]) == list:
                        a = allcontourdata[i][j][k]
                        allcontourdata[i][j][k] = np.array(a)
    return allcontourdata
    

def transformContourData(contourdata):
    for i in range(0, len(contourdata)):
        if len(contourdata[i+1]) != 0:
            for j in range(0, len(contourdata[i+1])):
                try:
                    contourdata[i+1][j] = contourdata[i+1][j].tolist()
                except:
                    contourdata[i+1][j] = contourdata[i+1][j]
    return contourdata


def transformClusterData(clusterdata):
    for i in range(0, len(clusterdata)):
        if len(clusterdata[i+1]) != 0:
            for j in range(0, len(clusterdata[i+1])):
                try:
                    clusterdata[i+1][j] = clusterdata[i+1][j].tolist()
                except:
                    clusterdata[i+1][j] = clusterdata[i+1][j]
    return clusterdata
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    