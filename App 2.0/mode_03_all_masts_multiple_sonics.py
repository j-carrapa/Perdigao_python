# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 11:17:11 2022

@author: João
"""

# Status: Reviewed

# Mode 3 - All towers multiple sonics

'''
This module extracts, processes and exports data for all towers in selected sonic heights in the dates defined by the user
'''

import tower_location as tl
import processing_functions as pr
import input_functions as ip
import download as dl

'''----- PART 1 ----------'''

# - Ask for the period time of the sample, multiples of 5 min: 5, 10, 15, 20, 30min or 1h, doesn´t accept other time periods

k = ip.input_time_period()

'''----- PART 2 ----------'''

# define an array that contains the dates defined by the user - Ask for input of time period

dates_def = ip.input_dates_defined()

if dates_def.size > 1:
    z1 = int(dates_def[0])
    z2 = int(dates_def[-1])

else:
    z1 = int(dates_def)
    z2 = int(dates_def)
    
# z1 - Start date
# z2 - End date

# the array dates_def contains all the dates defined by the user for extracting data, every position of the array contains the date of 1 day with the format YYYYMMDD

'''----- PART 3 ----------'''

# Ask for input of which hours of the day or days are of interest
# z3 = start hour
# z4 = ending hour

# Sectioning mode - User selects if the selected days have data for the whole day (sm = 1), just a time interval per day (sm = 2) or continuous data from the start hour to the end hour (sm = 3)

sm = ip.input_sectioning_mode()

if sm == 1:
    z3 = 0
    z4 = 24
    
if sm == 2:
    
    sta_end = ip.input_hours_sm2()
    
    z3 = int(sta_end[0])
    z4 = int(sta_end[1])
    
if sm == 3:
    
    sta_end = ip.input_hours_sm3(z1, z2)
    
    z3 = int(sta_end[0])
    z4 = int(sta_end[1])

'''----- PART 4 ----------'''

# Download files matching the dates defined by the user

dl.download(dates_def)

'''----- PART 5 ----------'''

# Create input section on wich sonics heights the sonics data will be extracted
    
# input section for all heigts needed
y_arr = ip.height_selection_hs1()

# At this point we have the dates defined by the user and the sonics heights

'''----- PARTS 7-11 ----------'''

print("Gathering data and exporting")

# Just to explain user what is happening

if y_arr.size > 1:
    
    for y in y_arr:
        
        i = tl.height_index(y)
        
        # Create an array with the towers available for that sonic height

        tow = tl.tower_avaliable_name(i)
        
        # Loop through all the available towers and call the process_routines function to process and export the data in each one of them, for the designated sonic height
        for x in tow:
            
            # this function compiles every process of data gathering, calculate turbulence parameters, adjust the time of the samples, adjust the time period through the day and saving and exporting the data for 1 sonic in the designated time period.

            pr.process_routines(dates_def, z1, z2, z3, z4, x, y, k, sm)
        
else:
    
    y = int(y_arr)
    i = tl.height_index(y)
    
    # Create an array with the towers available for that sonic height

    tow = tl.tower_avaliable_name(i)
    
    # Loop through all the available towers and call the process_routines function to process and export the data in each one of them, for the designated sonic height
    for x in tow:
        
        # this function compiles every process of data gathering, calculate turbulence parameters, adjust the time of the samples, adjust the time period through the day and saving and exporting the data for 1 sonic in the designated time period.

        pr.process_routines(dates_def, z1, z2, z3, z4, x, y, k, sm)
        