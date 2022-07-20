# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 16:24:25 2022

@author: Joao
"""

# Status: Reviewed

# Mode 2 - All sonics multiple towers

'''
This module extracts, processes and exports data for all sonics in selected towers in the dates defined by the user
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

# Input section on wich mast and height the sonic data will be extracted

x_j = ip.input_multiple_towers()

# x_arr - Contains the towers names defined by the user, j_arr - Contains the index position of the towers defined by the user

x_arr = x_j[0]
j_arr = x_j[1]


'''----- PARTS 6-10 ----------'''

print("Gathering data and exporting")

# Just to explain user what is happening

#Loop through towers (if there was a incorrect use of the mode and only one tower was selected, it will work nevertheless) 

if x_arr.size > 1:
    i = 0
    for x in x_arr:
        
        j = j_arr.item(i)
        j = int(j)
        
        # Create an array with the sonics heights available for that tower
        
        hei = tl.sonics_available_name(j)
        
        i += 1
        
        # Loop through all the sonics and call the extraction module and concatenate the data in order, using time as index, in each one of them
        for y in hei:
            
            # this function compiles every process of data gathering, calculate turbulence parameters, adjust the time of the samples, adjust the time period through the day and saving and exporting the data for 1 sonic in the designated time period.

            pr.process_routines(dates_def, z1, z2, z3, z4, x, y, k, sm)

else:
    x = str(x_arr)
    j = int(j_arr)
    
    # Create an array with the sonics heights available for that tower
    
    hei = tl.sonics_available_name(j)
    
    # Loop through all the sonics and call the extraction module and concatenate the data in order, using time as index, in each one of them
    for y in hei:
        
        
        # this function compiles every process of data gathering, calculate turbulence parameters, adjust the time of the samples, adjust the time period through the day and saving and exporting the data for 1 sonic in the designated time period.

        pr.process_routines(dates_def, z1, z2, z3, z4, x, y, k, sm)
