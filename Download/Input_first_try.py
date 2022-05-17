# -*- coding: utf-8 -*-
"""
Created on Fri May 13 16:31:43 2022

@author: João
"""

# First try of input module

from netCDF4 import Dataset
import numpy as np
import pandas as pd
import Tower_location as tl
import Download_v_01
from Download_v_01 import dates_16
from Download_v_01 import dates_tot


# Part 1 - define an array that contains the dates defined by the user


# Array with tower name code

t_name = np.array(["tnw01", "tnw02", "tnw03", "tnw04", "tnw05", "tnw06", "tnw07", "tnw08", "tnw09", "tnw10", "tnw11", "tnw12", "tnw13", "tnw14", "tnw15", "tnw16", "tse01", "tse02", "tse04", "tse05", "tse06", "tse07", "tse08", "tse09", "tse10", "tse11", "tse12", "tse13", "rsw01", "rsw02", "rsw03", "rsw04", "rsw05", "rsw06", "rsw07", "rsw08", "rne01", "rne02", "rne03", "rne04", "rne06", "rne07", "v01", "v03", "v04", "v05", "v06", "v07", "Extreme_SW", "Extreme_NE"])

# Array with tower heights

height = np.array(["2m", "4m", "6m", "8m", "10m", "20m", "30m", "40m", "60m", "80m", "100m"])

#
date_arr = dates_tot

# Ask for input of time period

a4 = 0

while a4 != 1:
    z = input("Select start date with the format, YYYYMMDD:")
    z = int(z)
    for c in date_arr:
        if z == c:
            a4 = 1
            break
    if a4 != 1:
        print("Start date incorrect")
        print("Possible start dates:")
        print(dates_16)
        print("And every date from 16 January 2017 to 1 July 2017")
    continue

a5 = 0

while a5 != 1:
    w = input("Select end date with the format, YYYYMMDD:")
    w = int(w)
    for c in date_arr:
        if w == c:
            if w >= z:
                a5 = 1
                break
            else:
                print("End date can not be a previous date from the starting date")
        
            
    if a5 != 1:
        print("Start date incorrect")
        print("Possible start dates:")
    continue

# pegar em z e w e criar um array com essas datas
#dates_def = np.array(0, dtype = 'i4')

a6 = 0

for q in date_arr:
    if z == q:
        dates_def = np.array(z, dtype = 'i4')
        a6 = 1
    if w == q:
        a6 = 0
    if a6 == 1:
        temp = np.array(q, dtype='i4')
        dates_def = np.append(dates_def, [temp])

# the array dates_def contains all the dates defined by the user for extracting data, every position of the array contains the date of 1 day with the format YYYYMMDD

# Write an input extra function to add dates that are not sequential and to order them in dates_def array





# Part 2 - Call the download module and dowload the files defined by the user

    
    
    
# Part 3 - Call the extraction module and concatenate the data in order, using time as index
'''        
i = 0

while a7 != 1:
    d = dates_def[i]

'''

        
'''


# Ask for input of tower code name, the code will not continue until a valid code name is given

a1 = 0

while a1 != 1:
    j = 0
    x = input("Tower name code:")
    for a in t_name:
        if x == a:
            a1 = 1
            break
        j = j + 1
    if a1 != 1:
        print("Code name incorrect")
        
    continue   
          
# Display which sonics heights are available for that tower


i = 0
while i < 12:
    if tl.m[i,j] == 1:
        print(height[i])
    
    i = i + 1
    continue


#  Ask for input of sonic height, the code will not continue until a valid height for the choosen tower is given


a3 = 0
while a3 != 1:
    a2 = 0
    while a2 != 1:
        i = 0
        y = input("Tower height:")
        for b in height:
            if y == b:
                a2 = 1
                break
            i = i + 1
        
        if a2 != 1:
            print("Select an appropriate height")
            
        continue 
    if tl.m[i,j] == 1:
        a3 = 1
    else:
        print("This tower doesn't have sonics for {} heihgt, select an appropriate height".format(y))
    continue

'''

