#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 14:46:34 2021

@author: BenButcher
"""

import glob


def getFilenames(noaapath):
    directory = noaapath+'/*.csv'
    noaafiles = glob.glob(directory)
    noaafiles.sort()
    return noaafiles