#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 16:34:28 2021

@author: BenButcher
"""

import cv2
import numpy as np
from pyhdf.SD import *
import re

def getFireData(filenames, stitchlist):
    """Identifies clusters of fires and returns a dictionary containing fire area and coordinates of cluster centre"""
    
    firedata = {}  # initialise dictionary
    firedata['Index'] = 'centre coordinates (i, j), area[km^2]'
    firecount = {}
    dayarea = {}
    contourdata = {}
    for i in range(0, len(stitchlist)):
        try:
            print('analysing... '+str(round(100*i/len(stitchlist), 2))+'%', end='\r')
            data = getStack(filenames, i)
            unique, counts = np.unique(data, return_counts=True)
            pixels = dict(zip(unique,  counts))
    
            if 7 in pixels.keys() or 8 in pixels.keys() or 9 in pixels.keys():
                centroids = []
                bwim = cv2.imread(stitchlist[i])
                bwim = cv2.resize(bwim, (11990, 11990))
                
                # convert to cv2 black and white image
                grayim = cv2.cvtColor(bwim, cv2.COLOR_BGR2GRAY)
                (thresh, bwim) = cv2.threshold(grayim, 75, 255, cv2.THRESH_BINARY)
        
                # find contours
                contours, hier = cv2.findContours(bwim, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
                count = len(contours)
                firecount[i+1] = count
                contourdata[i+1] = contours
                areas = 0
                
                for n in range(0, count):
                    # find centre coordinates and area of each cluster
                    M = cv2.moments(contours[n])
                    area = float(cv2.contourArea(contours[n])/100)
                    x = float(0.1*M['m10']/M['m00'])  # x coordinate is factored by 10
                    y = float(0.1*M['m01']/M['m00'])  # y coordinate is factored by 10
                    centroid = ((x, y), area)
                    centroids.append(centroid)
                    areas += area
                firedata[i+1] = centroids
                dayarea[i+1] = areas
            else:
                print('zero found')
                contourdata[i+1] = []
                firecount[i+1] = 0
                firedata[i+1] = []
                dayarea[i+1] = 0
        except:
            contourdata[i+1] = []
            firecount[i+1] = 0
            firedata[i+1] = []
            dayarea[i+1] = 0
            
    print('Done'+'\r')
        
    return contourdata, firedata, firecount, dayarea


def proximityTest(a_coords, b_coords):
    if type(a_coords)==int or type(b_coords)==int:
        return False
    else:
        lens = (len(a_coords), len(b_coords))
        for i in range(0, min(lens)):
            ax = a_coords[i][0][0]
            ay = a_coords[i][0][1]
            bx = b_coords[i][0][0]
            by = b_coords[i][0][1]
            distance = np.sqrt(((ax-bx)**2)+((ay-by)**2))
            if distance < 100:
                return True
        

def comparisonTest(a_coords, b_coords):
    comp = a_coords == b_coords
    if comp or comp.all():
        return True


def zeroTest(a_coords):
    is_all_zero = np.all((a_coords == 0))
    return is_all_zero


def commonTest(list1, list2): 
    result = False
    for x in list1:
        for y in list2:
            if x == y: 
                result = True
                return result  
    return result 
        
      
def getClusterData(contourdata, firecount):
    clusterdata = {}
    clustercount = {}
    for i in range(0, len(contourdata)):
        print('analysing '+str(round(100*i/len(contourdata), 2))+'%', end='\r')
        try:
            jlist = getClusterDataSingleImage(contourdata, i+1)
        except KeyError:
            jlist = getClusterDataSingleImage(contourdata, str(i+1))
        finlist = sortJlist(jlist)
        clusterdata[i+1] = finlist
    for j in range(0, len(clusterdata)):
        a = 0
        for k in range(0, len(clusterdata[j+1])):
            if len(clusterdata[j+1][k]) > 1:
                a += 1
        clustercount[j+1] = a
    print('Done'+'\r')
    return clusterdata, clustercount
    

def getClusterDataSingleImage(contourdata, image):
    try:
        contdata = contourdata[str(image)]
    except:
        contdata = contourdata[image]
    jlist = []
    for j in range(0, len(contdata)):
        a = contdata[j]
        klist = []
        klist.append(j+1)
        for k in range(0, len(contdata)):
            b = contdata[k]
            if zeroTest(a)==False and zeroTest(b)==False and proximityTest(a, b)==True and j!=k:
                klist.append(k+1)
                contdata[j] = 0
        jlist.append(klist)
    return jlist
 

def sortJlist(jlist):
    newjlist = []
    finlist = []
    for i in range(0, len(jlist)):
        a = jlist[i]
        for j in range(0, len(jlist)):
            b = jlist[j]
            if commonTest(a, b):
                 l = a + list(set(b) - set(a))
                 jlist[j] = []
        newjlist.append(l)
    new = list(filter(([]).__ne__, newjlist))
    for k in range(0, len(new)):
        if k != len(new)-1:
            if new[k] != new[k+1]:
                finlist.append(new[k])
        else:
            finlist.append(new[k])
    for n in range(1, len(finlist)):
        if len(finlist[n])==1 and commonTest(finlist[n], finlist[n-1]):
            finlist[n] = []
    finlist = list(filter(([]).__ne__, finlist))
    return finlist
    
    
    
def getAreaCount(filenames):
    areacount = []
    
    lcarea = np.zeros(len(filenames)*4)
    mcarea = np.zeros(len(filenames)*4)
    hcarea = np.zeros(len(filenames)*4)
    tarea = np.zeros(len(filenames)*4)
    
    for i in range(0, len(filenames)*4):
        print('counting...    '+str(round(100*i/(len(filenames)*4), 2))+'%', end='\r')
        try:
            data = getStack(filenames, i)
            unique, counts = np.unique(data, return_counts=True)
            pixels = dict(zip(unique, counts))
            try:
                lcarea[i] = pixels[7]
            except KeyError:
                lcarea[i] = 0
            try:
                mcarea[i] = pixels[8]
            except KeyError:
                mcarea[i] = 0
            try:
                hcarea[i] = pixels[9]
            except KeyError:
                hcarea[i] = 0
            tarea[i] = lcarea[i]+mcarea[i]+hcarea[i]
        except:
            print('missing at '+str(i))
            lcarea[i] = 0
            mcarea[i] = 0
            hcarea[i] = 0
            tarea[i] = 0
            
    lcarea = lcarea.tolist()
    mcarea = mcarea.tolist()
    hcarea = hcarea.tolist()
    tarea = tarea.tolist()
            
    areacount.append(lcarea)
    areacount.append(mcarea)
    areacount.append(hcarea)
    areacount.append(tarea)
    print('Done'+'\r')
    
    return areacount
            
            
def getStack(filenames, stacknumber):
    i = stacknumber//8
    n = stacknumber%8
    r = re.compile('.*h08v04')
    topfiles = list(filter(r.match, filenames))
    r = re.compile('.*h08v05')
    bottomfiles = list(filter(r.match, filenames))
    tfile = topfiles[i]  # selects data
    bfile = bottomfiles[i]
    tf = SD(tfile, SDC.READ)  # opens data
    bf = SD(bfile, SDC.READ)
    tdata = tf.select('FireMask')[n,:,:]  # selects fire mask
    bdata = bf.select('FireMask')[n,:,:]
    data = np.vstack((tdata, bdata))
    
    return data


def fireTest(n):
    if n == 7 or n == 8 or n == 9:
        result = True
    else:
        result = False
    return result

def getCumulativeCount(filenames):
    tarea = []
    t = 0
    for i in range(0, (len(filenames)*4)):
        print('counting... '+str(round(100*i/(len(filenames)*4), 2))+'%', end='\r')
        try:
            data = getStack(filenames, i)
            datap = getStack(filenames, i-1)
            (x,y) = data.shape
            for a in range(0, x):
                for b in range(0, y):
                    if fireTest(data[a][b]) == True and fireTest(datap[a][b]) == False:
                        t += 1
            tarea.append(t)
        except:
            tarea.append(t)
    print('Done'+'\r')
    return tarea
        
   
def fillAll(stack):
    slist = []
    for i in range(0, len(stack)):
        for j in range(0, len(stack[i])):
            if stack[i][j] == 1:
                s = []
                def floodFill(stack, x, y):
                    if stack[x][y] == 1:
                        stack[x][y] = 2
                        s.append(x*(stack.shape[1])+y)
                        if x > 0:
                            floodFill(stack, x-1, y)
                        if x < (len(stack)-1):
                            floodFill(stack, x+1, y)
                        if y > 0:
                            floodFill(stack, x, y-1)
                        if y < (len(stack[x])-1):
                            floodFill(stack, x, y+1)
                floodFill(stack, i, j)
                slist.append(s)
    return slist


def findSets(filenames):
    firesets = []
    for file in range(0, len(filenames)*4):
        print('finding sets...     '+str(round(file*25/len(filenames), 2))+'%', end='\r')
        try:
            data = getStack(filenames, file)
            data = np.where(data==3, 0, data)
            data = np.where(data==4, 0, data)
            data = np.where(data==5, 0, data)
            data = np.where(data==6, 0, data)
            data = np.where(data==7, 1, data)
            data = np.where(data==8, 1, data)
            data = np.where(data==9, 1, data)
            slist = fillAll(data)
            firesets.append(slist)
        except:
            firesets.append([])
    print('Done'+'\r')
    return firesets


def sortFiresets(allfiresets):
    sortedfiresets = []
    for i in allfiresets:
        sortset = []
        for j in i:
            sortset.append(sorted(j, key=len, reverse=True))
        sortedfiresets.append(sortset)
    return sortedfiresets


def listsToList(f):
    flattened_list = [y for x in f for y in x]
    return flattened_list


def firesConnected(a, b):
    if not set(a).isdisjoint(b):
        return True
    else:
        return False
    
    
def getDay(i, fs):
    f = fs[i]
    fset = listsToList(f)
    return set(fset)
            
            
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


def fullFullCheckAcross(line, testset):
    d = []
    def fullCheckAcross(line, testset):
        a = checkAcross(line, testset)
        if a != -1:
            d.append(line[a])
            line[a] = {-1}
            a = fullCheckAcross(line, testset)
        else:
            d.append(a)
        return d
    dd = fullCheckAcross(line, testset)
    dd.remove(-1)
    dset = set()
    for i in dd:
        dset = dset | set(i)
    return dset

    
def fullCheck(v, x, y):
    t = x
    r = []
    r
    try:
        testset = v[x][y]
        if testset != {-1}:
            def checkDown(v, x, t, testset):
                try:
                    a = fullFullCheckAcross(v[x+1], testset)
                    if a == set():
                        r.append(t)
                    else:
                        r.append(t)
                        t += 1
                        testset = a
                        checkDown(v, x+1, t, testset)
                except:
                    r.append(t)
                return r
            r = checkDown(v, x, t, testset)
        else:
            r = []
    except IndexError:
            r = []
    return r
            
    

def check(v, x, y):
    t = x
    r = []
    def checkDown(v, x, y, t):
        testset = set(v[x][y])
        try:
            a = checkAcross(v[x+1], testset)
            if a == -1:
                r.append(t)
            else:
                r.append(t)
                t += 1
                checkDown(v, x+1, a, t)
        except:
            r.append(t)
        return r
    r = checkDown(v, x, y, t)
    
    return r


def getLifetimes(firesets):
    lifetimes = []
    for i in range(0, len(firesets)):
        lifetime = []
        for j in range(0, len(firesets[i])):
            lifetime.append(check(firesets, i, j))
        lifetimes.append(lifetime)
    return lifetimes
                    

def anyFireOverlap(filenames):
    overlaps = []
    for i in range(0, (len(filenames)*4)-1):
        data = getStack(filenames, i)
        data = np.where(data==3, 0, data)
        data = np.where(data==4, 0, data)
        data = np.where(data==5, 0, data)
        data = np.where(data==6, 0, data)
        data = np.where(data==7, 1, data)
        data = np.where(data==8, 1, data)
        data = np.where(data==9, 1, data)
        datai = data
        data = getStack(filenames, i+1)
        data = np.where(data==3, 0, data)
        data = np.where(data==4, 0, data)
        data = np.where(data==5, 0, data)
        data = np.where(data==6, 0, data)
        data = np.where(data==7, 1, data)
        data = np.where(data==8, 1, data)
        data = np.where(data==9, 1, data)
        test = data*datai
        if test.any() == 1:
            overlaps.append(1)
        else:
            overlaps.append(0)
    return overlaps


def getFullLifetimes(firesets):
    lifetimes = []
    for i in range(0, len(firesets)):
        lifetime = []
        for j in range(0, len(firesets[i])):
            lifetime.append(fullCheck(firesets, i, j))
        lifetimes.append(lifetime)
    return lifetimes
        

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


def getAllFireCount(allfiresets):
    allfirecount = []
    for i in range(0, len(allfiresets)):
        firecount = {}
        for j in range(0, len(allfiresets[i])):
            firecount[j+1] = (len(allfiresets[i][j]))
        allfirecount.append(firecount)
    return allfirecount
            
    
def makeSquare(point):
    square = {point}
    if point%1200 != 1199:
        square = square | {point+1}
    if point%1200 != 0:
        square = square | {point-1}
    if point >= 1200:
        square = square | {point -1200}
    if point <= 2399*1200:
        square = square | {point+1200}
    if point%1200 != 1199 and point >= 1200:
        square = square | {point-1199}
    if point%1200 != 0  and point >= 1200:
        square = square | {point-1201}
    if point%1200 != 1199 and point <= 2399*1200:
        square = square | {point+1201}
    if point%1200 != 0 and point <= 2399*1200:
        square = square | {point+1199}
    square = list(square)
    square = [i for i in square if i >= 0]
    square.sort()
    return square


def getComplexFiresets(firesets):
    firesets = firesets[:]
    longfiresets = []
    for i in firesets:
        fire = []
        for j in i:
            a = set()
            points = []
            for k in j:
                square = makeSquare(k)
                points.append(square)
            for x in points:
                a = a | set(x)
            fire.append(list(a))
        longfiresets.append(fire)
    return longfiresets


def groupFires(allfiresets):
    longfiresets = getComplexFiresets(allfiresets)
    firegroups = []
    complexcount = np.zeros(len(allfiresets))
    for i in range(0, len(allfiresets)):
        fires = []
        for j in range(0, len(allfiresets[i])):
            if longfiresets[i][j] != {-1}:
                a = set(allfiresets[i][j])
                for k in range(0, len(allfiresets[i])):
                    if len(allfiresets[i][j]) != 0:
                        if j!=k and set(longfiresets[i][j])!={-1} and set(longfiresets[i][k])!={-1} and not set(longfiresets[i][j]).isdisjoint(set(longfiresets[i][k])):
                            longfiresets[i][k] = {-1}
                            a = a | set(allfiresets[i][k])
                            complexcount[i] += 1
                fires.append(list(a))
        firegroups.append(fires)
    return firegroups, complexcount
                    
                    
def getDailyGrowth(allcarea):
    alldailygrowth = []
    for i in allcarea:
        dailygrowth = []
        dailygrowth.append(0)
        for j in range(1, len(i)):
            dailygrowth.append(i[j]-i[j-1])
        alldailygrowth.append(dailygrowth)
    return alldailygrowth

    
    
    
    
    
    
    
    
    