# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 04:56:18 2016

@author: Shivuu
"""

import sys
import copy
import time 

start_time = time.time()

with open('wordsfile.txt', 'r') as f:
    data = f.read().splitlines()

    group_dict = {}
    
##    for line in data:
##        for number in range(3,5):
##            group = []
##            if(len(line)==number):
##                group.append(line)
##                group_dict[number]=group
##    print (group_dict)

    for number in range(3,9):
        group = []
        for line in data:
            if(len(line)==number):
                group.append(line)
                group_dict[number]=group
    print (group_dict)