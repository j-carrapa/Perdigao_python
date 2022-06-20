# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 16:45:48 2022

@author: João
"""

'''
This module extracts, processes and exports data for 1 sonic in the dates defined by the user
'''

# mode 1 one sonic height 1 mast

from netCDF4 import Dataset
import numpy as np
import pandas as pd
import Tower_location as tl
import requests
import Dates_array as da
import Data_gathering as dg
import Download as dl
import save_export_function as se
import Time_period_adjust as tp
import Turbulence_parameters as tu
import Process_routines_compiled as pr


'''----- PART 1 ----------'''

# The array 'dates_tot' will contain all the dates of the days with available data

# Fetching the dates arrays from the Dates_array module

dates_16 = da.d16
dates_tot = da.d

'''----- PART 2 ----------'''

# - Ask for the period time of the sample, multiples of 5 min: 5, 10, 15, 20, 30min or 1h, doesn´t accept other time periods

p0 = 0

while p0 != 1:
    period_val = input("Type one of the options for time period in min:\n5, 10, 15, 20, 30 or 60:")
    
    p = int(period_val)
    
    if p == 5 or p == 10 or p == 15 or p == 20 or p == 30 or p == 60:
        p0 = 1
        continue
    else:
        print("Invalid time period")
        continue
  

period_conv = int(period_val)/5

k = period_conv

'''----- PART 3 ----------'''

# Ask for input of which hours of the day are of interest
# z3 = start hour
# z4 = ending hour

hour_arr = np.arange(0, 25)

a7 = 0

while a7 != 1:
    z3 = input("Select start hour from 0-23:")
    z3 = int(z3)
    for c in hour_arr:
        if z3 == c and z3 != 24:
            a7 = 1
            break
    if a7 != 1:
        print("Start hour incorrect")
        print("Possible start hours:")
        print(hour_arr[0:24])
    continue

a8 = 0

while a8 != 1:
    z4 = input("Select ending hour from {}-24:".format(z3+1))
    z4 = int(z4)
    for c in hour_arr:
        if z4 == c and z4 > z3:
            a8 = 1
            break
    if a8 != 1:
        print("Ending hour incorrect")
        print("Possible ending hours:")
        print(hour_arr[z3+1:25])
    continue

'''----- PART 4 ----------'''

# define an array that contains the dates defined by the user

# Ask for input of time period

a4 = 0

while a4 != 1:
    z1 = input("Select start date with the format, YYYYMMDD:")
    z1 = int(z1)
    for c in dates_tot:
        if z1 == c:
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
    z2 = input("Select end date with the format, YYYYMMDD:")
    z2 = int(z2)
    for c in dates_tot:
        if z2 == c:
            if z2 >= z1:
                a5 = 1
                break
            else:
                print("End date can not be a previous date from the starting date")
        
            
    if a5 != 1:
        print("Start date incorrect")
        print("Possible start dates:")
    continue

# using defined sart and end dates (z1, z2) to create an array with the defined dates
# This for cycle is showing an error (dates_def appears first for append than for creation, the fact is that the if line for the append will not ever be executed before the if line for creation)

a6 = 0

for q in dates_tot:
    if a6 == 1:
        temp = np.array(q, dtype='i4')
        dates_def = np.append(dates_def, [temp])    
    if z1 == q:
        dates_def = np.array(z1, dtype = 'i4')
        a6 = 1
    if z2 == q:
        a6 = 0

# the array dates_def contains all the dates defined by the user for extracting data, every position of the array contains the date of 1 day with the format YYYYMMDD

'''----- PART 5 ----------'''

# Download files matching the dates defined by the user

dl.download(dates_def)

'''----- PART 6 ----------'''
   
# Create input section on wich mast and height the sonic data will be extracted

# Array with tower name code

t_name = tl.t_n

# Array with tower heights

height = tl.h

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
while i < 11:
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

# x: tower code name
# y: height code name

# At this point we have the dates defined by the user, the tower and the height relative to one sonic

'''----- PARTS 7-11 ----------'''

print("Gathering data and exporting")

# Just to explain user what is happening

# this function compiles every process of data gathering, calculate turbulence parameters, adjust the time of the samples, adjust the time period through the day and saving and exporting the data for 1 sonic in the designated time period.

pr.process_routines(dates_def, z1, z2, z3, z4, x, y, k)