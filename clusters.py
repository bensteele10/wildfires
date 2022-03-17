#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 16:34:28 2021

@author: BenButcher
"""

import cv2
import imutils
import numpy as np

def getClusterData(bwimages):
    """Identifies clusters of fires and returns a dictionary containing fire area and coordinates of cluster centre"""
    
    firedata = {}  # initialise dictionary
    firedata['Index'] = 'centre coordinates (i, j), area[km^2]'
    firecount = {}
    dayarea = {}
    contourdata = {}
    for i in range(0, len(bwimages)):
        centroids = []
        bwim = cv2.imread(bwimages[i])
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
            area = float(cv2.contourArea(contours[n])/10)
            x = float(0.1*M['m10']/M['m00'])  # x coordinate is factored by 10
            y = float(0.1*M['m01']/M['m00'])  # y coordinate is factored by 10
            centroid = ((x, y), area)
            centroids.append(centroid)
            areas += area
        firedata[i+1] = centroids
        dayarea[i+1] = areas
        
    return contourdata, firedata, firecount, dayarea
