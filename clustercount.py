#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 16:34:28 2021

@author: BenButcher
"""

import cv2
import imutils

def clusterCount(bwimages):
    print('Cluster count:\n')
    clusters = dict.fromkeys(range(1, len(bwimages)))
    for i in range(0, len(bwimages)):
        centroids = []
        bwim = cv2.imread(bwimages[i])
        bwim = cv2.resize(bwim, (11990, 11990))
        
        grayim = cv2.cvtColor(bwim, cv2.COLOR_BGR2GRAY)
        (thresh, bwim) = cv2.threshold(grayim, 75, 255, cv2.THRESH_BINARY)

        contours, hier = cv2.findContours(bwim, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        count = len(contours)
        print(str(count)+' distinct fires in image '+str(i+1))
        
        img = cv2.drawContours(bwim, contours, -1, (255,255,255), 3)
        
        for n in range(0, count):
            
            
            M = cv2.moments(contours[n])
            if M['m00'] == 0:
                pass
            else:
                area = cv2.contourArea(contours[n])
                x = float(M['m10']/M['m00'])
                y = float(M['m01']/M['m00'])
                centroid = ((x, y), area)
                centroids.append(centroid)
        clusters[i+1] = centroids
        
    return clusters
            
       