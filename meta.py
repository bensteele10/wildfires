#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 16:11:12 2021

@author: BenButcher
"""

import sys
sys.path.insert(0, '/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Code/ip')
from ip import *

"""Input MOD14A1 data filepath"""
filepath = '/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/MOD14A1/2020'

"""Gathers filenames of files from series in chronological order"""
filenames = files.getFilenames(filepath)

"""Split filenames"""
#afiles, bfiles, cfiles, dfiles, efiles, ffiles, gfiles = files.splitFilenames(filenames)

"""Input MOD14A1 data filepath"""
nfilepath = '/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/MOD14A1/2019'

"""Gathers filenames of files from series in chronological order"""
nfilenames = files.getFilenames(nfilepath)

"""Input MOD14A1 data filepath"""
efilepath = '/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/MOD14A1/2018'

"""Gathers filenames of files from series in chronological order"""
efilenames = files.getFilenames(efilepath)

"""Input MOD14A1 data filepath"""
sfilepath = '/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/MOD14A1/2017'

"""Gathers filenames of files from series in chronological order"""
sfilenames = files.getFilenames(sfilepath)

"""Input MOD14A1 data filepath"""
sixfilepath = '/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/MOD14A1/2016'

"""Gathers filenames of files from series in chronological order"""
sixfilenames = files.getFilenames(sixfilepath)

"""Input MOD14A1 data filepath"""
ffilepath = '/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/MOD14A1/2015'

"""Gathers filenames of files from series in chronological order"""
ffilenames = files.getFilenames(ffilepath)

"""Generates lists of images and black and white images"""
imlist, bwimlist = images.getImageLists(filenames, filepath)

"""Generates stitch list"""
stitchlist = images.getStitchList(filenames, filepath)

"""Generates stitch list"""
nstitchlist = images.getStitchList(nfilenames, nfilepath)

"""Generates stitch list"""
estitchlist = images.getStitchList(efilenames, efilepath)

"""Generates stitch list"""
sstitchlist = images.getStitchList(sfilenames, sfilepath)

"""Generates stitch list"""
sixstitchlist = images.getStitchList(sixfilenames, sixfilepath)

"""Generates stitch list"""
fstitchlist = images.getStitchList(ffilenames, ffilepath)

#allareacount, allcarea, allclustercount, alldayarea, allfirecount, allfiredata, allcontourdata, allclusterdata, allfiresets, sortedfiresets = files.readPlotData()

"""Generates lists of images and black and white images"""
#nimlist, nbwimlist = images.getImageLists(nfilenames, nfilepath)

"""Generates lists of images and black and white images"""
#eimlist, ebwimlist = images.getImageLists(efilenames, efilepath)

"""Generates lists of images and black and white images"""
#simlist, sbwimlist = images.getImageLists(sfilenames, sfilepath)

"""Generates lists of images and black and white images"""
#siximlist, sixbwimlist = images.getImageLists(sixfilenames, sixfilepath)

"""Generates lists of images and black and white images"""
#fimlist, fbwimlist = images.getImageLists(ffilenames, ffilepath)

"""Generates colour and black and white images"""
#images.getImages(filenames, filepath)

"""Generates black and white images only"""
#images.getBWImages(gfiles, filepath)

"""Generates colour images only"""
#images.getColourImages(dfiles, filepath)

"""Generates stitched images"""
#images.stitchBWImages(bwimlist, filepath)

"""Finds clusters of fires and returns a dictionary of area and coordinates of centre"""
#contourdata, firedata, firecount, dayarea = analysis.getFireData(filenames, stitchlist)

"""Finds clusters of fires and returns a dictionary of area and coordinates of centre"""
#ncontourdata, nfiredata, nfirecount, ndayarea = analysis.getFireData(nfilenames, nstitchlist)

"""Finds clusters of fires and returns a dictionary of area and coordinates of centre"""
#econtourdata, efiredata, efirecount, edayarea = analysis.getFireData(efilenames, estitchlist)

"""Finds clusters of fires and returns a dictionary of area and coordinates of centre"""
#scontourdata, sfiredata, sfirecount, sdayarea = analysis.getFireData(sfilenames, sstitchlist)

"""Finds clusters of fires and returns a dictionary of area and coordinates of centre"""
#sixcontourdata, sixfiredata, sixfirecount, sixdayarea = analysis.getFireData(sixfilenames, sixstitchlist)

"""Finds clusters of fires and returns a dictionary of area and coordinates of centre"""
#fcontourdata, ffiredata, ffirecount, fdayarea = analysis.getFireData(ffilenames, fstitchlist)

#allareacount, allcarea, allclustercount, alldayarea, allfirecount, allfiredata, allcontourdata = files.readPlotData()

#fcontourdata = allcontourdata[0]
#sixcontourdata = allcontourdata[1]
#scontourdata = allcontourdata[2]
#econtourdata = allcontourdata[3]
#ncontourdata = allcontourdata[4]
#contourdata = allcontourdata[5]

#ffirecount = allfirecount[0]
#sixfirecount = allfirecount[1]
#sfirecount = allfirecount[2]
#efirecount = allfirecount[3]
#nfirecount = allfirecount[4]
#firecount = allfirecount[5]

"""Finds numbers and instances of complex fire clusters"""
#clusterdata, clustercount = analysis.getClusterData(contourdata, firecount)

"""Finds numbers and instances of complex fire clusters"""
#nclusterdata, nclustercount = analysis.getClusterData(ncontourdata, nfirecount)

"""Finds numbers and instances of complex fire clusters"""
#eclusterdata, eclustercount = analysis.getClusterData(econtourdata, efirecount)

"""Finds numbers and instances of complex fire clusters"""
#sclusterdata, sclustercount = analysis.getClusterData(scontourdata, sfirecount)

"""Finds numbers and instances of complex fire clusters"""
#sixclusterdata, sixclustercount = analysis.getClusterData(sixcontourdata, sixfirecount)

"""Finds numbers and instances of complex fire clusters"""
#fclusterdata, fclustercount = analysis.getClusterData(fcontourdata, ffirecount)

"""Count areas of fire in day/year"""
#areacount = analysis.getAreaCount(filenames)

"""Count areas of fire in day/year"""
#nareacount = analysis.getAreaCount(nfilenames)

"""Count areas of fire in day/year"""
#eareacount = analysis.getAreaCount(efilenames)

"""Count areas of fire in day/year"""
#sareacount = analysis.getAreaCount(sfilenames)

"""Count areas of fire in day/year"""
#sixareacount = analysis.getAreaCount(sixfilenames)

"""Count areas of fire in day/year"""
#fareacount = analysis.getAreaCount(ffilenames)

"""Count cumulative area"""
#carea = analysis.getCumulativeCount(filenames)

"""Count cumulative area"""
#ncarea = analysis.getCumulativeCount(nfilenames)

"""Count cumulative area"""
#ecarea = analysis.getCumulativeCount(efilenames)

"""Count cumulative area"""
#scarea = analysis.getCumulativeCount(sfilenames)

"""Count cumulative area"""
#sixcarea = analysis.getCumulativeCount(sixfilenames)

"""Count cumulative area"""
#fcarea = analysis.getCumulativeCount(ffilenames)

"""Get fire sets"""
#fs = analysis.findSets(filenames)
#nfs = analysis.findSets(nfilenames)
#efs = analysis.findSets(efilenames)
#sfs = analysis.findSets(sfilenames)
#sixfs = analysis.findSets(sixfilenames)
#ffs = analysis.findSets(ffilenames)

"""Transform data"""
#contourdata = files.transformContourData(contourdata)
#ncontourdata = files.transformContourData(ncontourdata)
#econtourdata = files.transformContourData(econtourdata)
#scontourdata = files.transformContourData(scontourdata)
#sixcontourdata = files.transformContourData(sixcontourdata)
#fcontourdata = files.transformContourData(fcontourdata)

"""Get huge lists"""
#allfirecount = [ffirecount, sixfirecount, sfirecount, efirecount, nfirecount, firecount]
#alldayarea = [fdayarea, sixdayarea, sdayarea, edayarea, ndayarea, dayarea]
#allcontourdata = [fcontourdata, sixcontourdata, scontourdata, econtourdata, ncontourdata, contourdata]
#allfiredata = [ffiredata, sixfiredata, sfiredata, efiredata, nfiredata, firedata]
#allclusterdata = [fclusterdata, sixclusterdata, sclusterdata, eclusterdata, nclusterdata, clusterdata]
#allclustercount = [fclustercount, sixclustercount, sclustercount, eclustercount, nclustercount, clustercount]
#allareacount = [fareacount, sixareacount, sareacount, eareacount, nareacount, areacount]
#allcarea = [fcarea, sixcarea, scarea, ecarea, ncarea, carea]
#newfiresets = [ffs, sixfs, sfs, efs, nfs, fs]


"""Save data"""
#files.saveData(newfiresets)


"""
getAreaCountPlot(allareacount, filepath)
getAreaRollAvPlot(allareacount, filepath)
getAreaRollAvCompPlot(allareacount, filepath)
getAreaRollAvCompFilledPlot(allareacount, filepath)
getAreaRollAvSumPlot(allareacount, filepath)
getAreaCountStem(allareacount, filepath)
getAreaCountTypePlot(allareacount, filepath)
getCumulativeCountPlot(allcarea, filepath)
getMeanAreaPlot(allareacount, allfirecount, filepath)
getMeanAreaRollAvPlot(allareacount, allfirecount, filepath)
getMeanAreaRollAvCompPlot(allareacount, allfirecount, filepath)
getFiresPlot(allfirecount, filepath)
getFiresCountPlot(allfiresets, filepath)
getFiresRollAvPlot(allfirecount, filepath)
getFiresRollAvCompPlot(allfirecount, filepath)
getFireandAreaPlot(allareacount, allfirecount, filepath)
getComplexFiresPlot(allclustercount, filepath)
getFireTypePlot(allclustercount, allfirecount, filepath)
getFireTypeFilledPlot(allclustercount, allfirecount, filepath)
plotLines(flts, allfiresets, filepath)
plotAugLines(flts, allfiresets, filepath)
getVCountPlot(vdata)
getAreaRollAvLightningPlot(allareacount, vdata, filepath)
getFiresLightningPlot(allfiresets, vdata, filepath)
getGCLightningPlot(vdata, filepath)
getFiresDerivPlot(allfiresets, vdata, filepath)
plotLinesLightning(lifetimes, vdata, filepath)
getNetworkPlot(allfirecount, allfiresets, allareacount, filepath)
"""
#allareacount, allcarea, allclustercount, alldayarea, allfirecount, allfiredata, allcontourdata, allclusterdata, allfiresets, sortedfiresets = files.readPlotData()
"""
def runAllPlots():
    allareacount, allcarea, allclustercount, alldayarea, allfirecount, allfiredata, allcontourdata, allclusterdata, allfiresets = files.readPlotData()
    filepath = '/Users/BenButcher/Documents/Work/Aeronautics and Astronautics/Part 3/IP/Data/MOD14A1/2020'
    flts = analysis.getFullLifetimes(allfiresets[5])
    vdata = vaisala.loadData()
    plots.getAreaCountPlot(allareacount, filepath)
    plots.getAreaRollAvPlot(allareacount, filepath)
    plots.getAreaRollAvCompPlot(allareacount, filepath)
    plots.getAreaRollAvCompFilledPlot(allareacount, filepath)
    plots.getAreaRollAvSumPlot(allareacount, filepath)
    plots.getAreaCountStem(allareacount, filepath)
    plots.getAreaCountTypePlot(allareacount, filepath)
    plots.getCumulativeCountPlot(allcarea, filepath)
    plots.getMeanAreaPlot(allareacount, allfirecount, filepath)
    plots.getMeanAreaRollAvPlot(allareacount, allfirecount, filepath)
    plots.getMeanAreaRollAvCompPlot(allareacount, allfirecount, filepath)
    plots.getFiresPlot(allfirecount, filepath)
    plots.getFiresCountPlot(allfiresets, filepath)
    plots.getFiresRollAvPlot(allfirecount, filepath)
    plots.getFiresRollAvCompPlot(allfirecount, filepath)
    plots.getFireandAreaPlot(allareacount, allfirecount, filepath)
    plots.getComplexFiresPlot(allclustercount, filepath)
    plots.getFireTypePlot(allclustercount, allfirecount, filepath)
    plots.getFireTypeFilledPlot(allclustercount, allfirecount, filepath)
    plots.plotLines(flts, allfiresets, filepath)
    plots.plotAugLines(flts, allfiresets, filepath)
    plots.getVCountPlot(vdata)
    plots.getAreaRollAvLightningPlot(allareacount, vdata, filepath)
    plots.getFiresLightningPlot(allfiresets, vdata, filepath)
    plots.getGCLightningPlot(vdata, filepath)
    plots.getFiresDerivPlot(allfiresets, vdata, filepath)
    plots.plotLinesLightning(flts, vdata, filepath)
    #plots.getNetworkPlot(allfirecount, allfiresets, allareacount, filepath)
"""
