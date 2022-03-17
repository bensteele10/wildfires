#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 16:22:17 2021

@author: BenButcher
"""

from matplotlib import pyplot as plt
import matplotlib as mpl
from pyhdf.SD import *
import numpy as np
import earthpy.spatial as es
import gc
import sys
from PIL import Image
import re


def getAllImages(filenames, filepath):
    """Generates colour and black and white images based from hdf files"""
    
    for i in range(0, len(filenames)):  # cycles through files
        for n in range(0, 8):
            number = (8*i)+n+1
            file = filenames[i]  # selects data
            f = SD(file, SDC.READ)  # opens data
            data = f.select('FireMask')[n,:,:]  # selects fire mask
            
            # set image to display only four colours
            data = np.where(data==3, 1, data)
            data = np.where(data==4, 0, data)
            data = np.where(data==5, 2, data)
            data = np.where(data==6, 0, data)
            data = np.where(data==7, 3, data)
            data = np.where(data==8, 3, data)
            data = np.where(data==9, 3, data)
    
            cmap = mpl.colors.LinearSegmentedColormap.from_list('', ['white', '#0000A0', '#347C2C', '#E41B17'])  # sets a red, green, blue colour map
    
            # plot and save image
            plt.figure(figsize = (100,100), dpi=120)  # image needs to be 1200x1200 pixels
            fig = plt.imshow(data, cmap=cmap, interpolation='nearest', aspect='auto')
            plt.axis('off')
            fig.axes.get_xaxis().set_visible(False)
            fig.axes.get_yaxis().set_visible(False)
            plt.savefig(filepath+'/image '+str(number), bbox_inches='tight', pad_inches = 0)
            plt.close()
            print('colour '+str(number))
            
            # generates black and white images
            # sets image to display only two colours
            data = np.where(data==1, 0, data)
            data = np.where(data==2, 0, data)
            data = np.where(data==3, 1, data)
    
            cmap = mpl.colors.LinearSegmentedColormap.from_list('', ['black', 'white'])  # sets a black and white colour map
    
            # plot and save image
            plt.figure(figsize = (100,100), dpi=120)  # images needs to be 1200x1200 pixels
            fig = plt.imshow(data, cmap=cmap, interpolation='nearest')
            plt.axis('off')
            fig.axes.get_xaxis().set_visible(False)
            fig.axes.get_yaxis().set_visible(False)
            plt.savefig(filepath+'/bwimage '+str(number), bbox_inches='tight', pad_inches = 0)
            plt.close()
            print('bw '+str(number))
            
            
def getBWImages(xfiles, filepath):
    """Generates colour and black and white images based from hdf files"""
    print('Generating images...')
    cmap = mpl.colors.LinearSegmentedColormap.from_list('', ['black', 'white'])
    for i in range(0, len(xfiles)):  # cycles through files
        for n in range(0, 8):
            if xfiles[i] != '':
                number = (8*i)+n+1
                try:
                    print(number, end='\r')
                    file = xfiles[i]  # selects data
                    f = SD(file, SDC.READ)  # opens data
                    data = f.select('FireMask')[n,:,:]  # selects fire mask
                    
                    # set image to display only four colours
                    
                    
                    data = np.where(data==3, 0, data)
                    data = np.where(data==4, 0, data)
                    data = np.where(data==5, 0, data)
                    data = np.where(data==6, 0, data)
                    data = np.where(data==7, 1, data)
                    data = np.where(data==8, 1, data)
                    data = np.where(data==9, 1, data)
            
                    # plot and save image
                    plt.figure(figsize = (100,100), dpi=120)  # images needs to be 1200x1200 pixels
                    fig = plt.imshow(data, cmap=cmap, interpolation='nearest')
                    plt.axis('off')
                    fig.axes.get_xaxis().set_visible(False)
                    fig.axes.get_yaxis().set_visible(False)
                    plt.savefig(filepath+'/bwimage '+str(number), bbox_inches='tight', pad_inches = 0)
                    plt.close()
                    #print(str(round(number*100/(15*8), 2))+'%',end='\r')
                    del number, file, f, data, fig
                    gc.collect()
                except IndexError:
                    print('Index Error at '+str(number))
    print('Done')
    
    
def getColourImages(xfiles, filepath):
    """Generates colour and black and white images based from hdf files"""
    print('Generating images...')
    cmap = mpl.colors.LinearSegmentedColormap.from_list('', ['white', '#0000A0', '#347C2C', '#E41B17'])
    for i in range(0, len(xfiles)):  # cycles through files
        for n in range(0, 8):
            if xfiles[i] != '':
                number = (8*i)+n+1
                try:
                    print(number, end='\r')
                    file = xfiles[i]  # selects data
                    f = SD(file, SDC.READ)  # opens data
                    data = f.select('FireMask')[n,:,:]  # selects fire mask
                    
                    # set image to display only four colours
                    data = np.where(data==3, 1, data)
                    data = np.where(data==4, 0, data)
                    data = np.where(data==5, 2, data)
                    data = np.where(data==6, 0, data)
                    data = np.where(data==7, 3, data)
                    data = np.where(data==8, 3, data)
                    data = np.where(data==9, 3, data)
                    
                    cmap = mpl.colors.LinearSegmentedColormap.from_list('', ['white', '#0000A0', '#347C2C'])
                    
                    if 3 in data:
                        cmap = mpl.colors.LinearSegmentedColormap.from_list('', ['white', '#0000A0', '#347C2C', '#E41B17'])
                        
                    # plot and save image
                    plt.figure(figsize = (100,100), dpi=120)  # images needs to be 1200x1200 pixels
                    fig = plt.imshow(data, cmap=cmap, interpolation='nearest')
                    plt.axis('off')
                    fig.axes.get_xaxis().set_visible(False)
                    fig.axes.get_yaxis().set_visible(False)
                    plt.savefig(filepath+'/image '+str(number), bbox_inches='tight', pad_inches = 0)
                    plt.close()
                    #print(str(round(number*100/(15*8), 2))+'%',end='\r')
                    del number, file, f, data, fig
                    gc.collect()
                        
                except IndexError:
                    print('Index Error at '+str(number))
    print('Done')


def getImageLists(filenames, filepath):
    """Fills images and bwimages without generating images"""
    
    images = []
    bwimages = []
    for i in range(0, 8*len(filenames)):  # cycles through files
        images.append(filepath+'/image '+str(i+1)+'.png')
        bwimages.append(filepath+'/bwimage '+str(i+1)+'.png')
    return images, bwimages


def stitchImages(imlist, filepath):
    stitchlist = []
    for i in range(0, len(imlist)//16):
        a = imlist[8*(2*i):8*(2*i+1)]
        b = imlist[8*(2*i+1):8*(2*i+2)]
        for j in range(0, 8):
            stitchlist.append((a[j], b[j]))
    for i in range(0, len(stitchlist)):
        print('stitching... '+str(round(((i+1)/(len(imlist)/2))*100, 2))+'%', end='\r')
        images = [Image.open(x) for x in stitchlist[i]]
        widths, heights = zip(*(i.size for i in images))
        max_width = max(widths)
        total_height = sum(heights)
        new_im = Image.new('RGB', (max_width, total_height))
        y_offset = 0
        for im in images:
            new_im.paste(im, (0,y_offset))
            y_offset += im.size[0]
        new_im.save('/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/MOD14A1/2020'+'/stitch '+str(i+1)+'.png')


def getStitchList(filenames, filepath):
    stitches = []
    for i in range(0, len(filenames)*4):
        stitches.append(filepath+'/bwstitch '+str(i+1)+'.png')
    return stitches


def stitchBWImages(imlist, filepath):
    stitchlist = []
    for i in range(0, len(imlist)//16):
        a = imlist[8*(2*i):8*(2*i+1)]
        b = imlist[8*(2*i+1):8*(2*i+2)]
        for j in range(0, 8):
            stitchlist.append((a[j], b[j]))
    for i in range(0, len(stitchlist)):
        print('stitching... '+str(round(((i+1)/(len(imlist)/2))*100, 2))+'%', end='\r')
        images = [Image.open(x) for x in stitchlist[i]]
        widths, heights = zip(*(i.size for i in images))
        max_width = max(widths)
        total_height = sum(heights)
        new_im = Image.new('RGB', (max_width, total_height))
        y_offset = 0
        for im in images:
            new_im.paste(im, (0,y_offset))
            y_offset += im.size[0]
        new_im.save(filepath+'/bwstitch '+str(i+1)+'.png')
        
        
def getHeatMap(filenames, filepath):
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
    
    heat = np.zeros((2400, 1200))
    
    for i in range(0, (len(filenames)*4)):  # cycles through files
        data = getStack(filenames, i)
        data = np.where(data==3, 0, data)
        data = np.where(data==4, 0, data)
        data = np.where(data==5, 0, data)
        data = np.where(data==6, 0, data)
        data = np.where(data==7, 1, data)
        data = np.where(data==8, 1, data)
        data = np.where(data==9, 1, data)
        
        heat += data
    
    plt.figure(figsize = (100,200), dpi=120)  # image needs to be 1200x1200 pixels
    fig = plt.imshow(heat, cmap='hot', interpolation='nearest', aspect='auto')
    plt.axis('off')
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    plt.savefig(filepath+'/heatmap', bbox_inches='tight', pad_inches = 0)
    plt.close()
                

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
