# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 15:20:19 2022

@author: Joao
"""

# Test sheet 2

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



t_name = tl.t_n

# Array with tower heights

height = tl.h

# Ask for input of tower code name, the code will not continue until a valid code name is given

a1 = 0
a2 = 0
a3 = 0

print("Type 1 tower code name and press enter.\nYou will be asked for a new tower code name until you type[end]")

while a3 != 1:
    a1 = 0
    j = 0
    x = input("Tower name code:")
    for a in t_name:
        
        if x == 'end':
            a3 = 1
            a1 = 1
            break
        
        if x == a:
            
            if a2 == 1:
                x_arr = np.append(x_arr, x)
                j_arr = np.append(j_arr, j)
                
            if a2 == 0:
                x_arr = np.array(x)
                j_arr = np.array(j)
                x0 = x
                j0 = j
                a2 = 1
              
            a1 = 1
            break
        j = j + 1
    if a1 != 1:
        print("Code name incorrect")
        
    continue

# At this point we have the dates defined by the user and the towers 

# Ask for input of sonic height, the code will not continue until a valid code name is given

a2 = 0
a3 = 0

print("Type 1 sonic height and press enter.\nYou will be asked for a new sonic height until you type[end]")

while a3 != 1:
    i = 0
    a1 = 0
    y = input("Sonic height:")
    for a in height:
        
        
        if y == 'end':
            a3 = 1
            a1 = 1
            break
        
        if y == a:
            
            if a2 == 1:
                y_arr = np.append(y_arr, y)
                i_arr = np.append(i_arr, i)
                
            if a2 == 0:
                y_arr = np.array(y)
                i_arr = np.array(i)
                y0 = y
                i0 = i
                a2 = 1
              
            a1 = 1
            break
        i = i + 1
    if a1 != 1:
        print("Sonic height incorrect")
        
    continue


# At this point we have the dates defined by the user, the towers and the sonics heights


'''----- PART 7 ----------'''

print("Gathering data and exporting")

# Just to explain user what is happening
#Loop through towers (if there was a incorrect use of the mode and only one tower was selected, it will work nevertheless) 

if x_arr.size > 1:
    i = 0
    for x in x_arr:
        
        j = j_arr.item(i)
        
        # Create an array with the sonics heights available for that tower

        tl.sonics_available_name(j)
        hei = tl.hei.copy()
        
        i += 1
        
        # Loop through all the sonics and call the extraction module and concatenate the data in order, using time as index, in each one of them
        for y in hei:
            
            if y_arr.size > 1:
                
                for y1 in y_arr:
                    
                    y1 = int(y1)
                    
                    if y1 == y:
                        
                        dg.data_gathering(dates_def, z1, z2, x, y)
                        
                        dfc = dg.dfc3.copy()
                        

                        '''----- PART 8 ----------'''
                        # If time period is different from 5 min, retrieves a data frame with the mean variables values, according to the time period selected

                        if k>1:
                            tp.period_adjust(z1, z2, dfc, k)
                            dfc = tp.dfm.copy()        
                        
                        '''----- PART 9 ----------'''
                        # If the user asked for a specific time period of the day (ex: from 11h to 17h) this function updates the df to fulfill that order.
                        
                        if z3 != 0 or z4 != 24:
                            tp.section_time(dfc, z1, z2, z3, z4, k, dates_def)
                            dfc = tp.dfnew.copy()
                        

                        '''----- PART 10 ----------'''
                        
                        se.save_export(dfc, x, y, z1, z2, z3, z4, k)

                        # When converting the df to a np array the file is loosing the info on the time variable (used as index in the df)
                        # Possible solution is create a new df whith  the time series as a column, as well as index
           
                    
            else:
                y1 = int(y0)
                i1 = i0
                
                if y1 == y:
                    
                    dg.data_gathering(dates_def, z1, z2, x, y)
                    
                    dfc = dg.dfc3.copy()
                    

                    '''----- PART 8 ----------'''
                    # If time period is different from 5 min, retrieves a data frame with the mean variables values, according to the time period selected

                    if k>1:
                        tp.period_adjust(z1, z2, dfc, k)
                        dfc = tp.dfm.copy()        
                    
                    '''----- PART 9 ----------'''
                    # If the user asked for a specific time period of the day (ex: from 11h to 17h) this function updates the df to fulfill that order.
                    
                    if z3 != 0 or z4 != 24:
                        tp.section_time(dfc, z1, z2, z3, z4, k, dates_def)
                        dfc = tp.dfnew.copy()
                    

                    '''----- PART 10 ----------'''
                    
                    se.save_export(dfc, x, y, z1, z2, z3, z4, k)

                    # When converting the df to a np array the file is loosing the info on the time variable (used as index in the df)
                    # Possible solution is create a new df whith  the time series as a column, as well as index
       
else:
    x = x0
    j1 = j0
    
    # Create an array with the sonics heights available for that tower

    tl.sonics_available_name(j1)
    hei = tl.hei.copy()
    
    # Loop through all the sonics and call the extraction module and concatenate the data in order, using time as index, in each one of them
    for y in hei:
        
        
        if y_arr.size > 1:
            
            for y1 in y_arr:
                
                y1 = int(y1)
                
                if y1 == y:
                    
                    dg.data_gathering(dates_def, z1, z2, x, y)
                    
                    dfc = dg.dfc3.copy()
                    

                    '''----- PART 8 ----------'''
                    # If time period is different from 5 min, retrieves a data frame with the mean variables values, according to the time period selected

                    if k>1:
                        tp.period_adjust(z1, z2, dfc, k)
                        dfc = tp.dfm.copy()        
                    
                    '''----- PART 9 ----------'''
                    # If the user asked for a specific time period of the day (ex: from 11h to 17h) this function updates the df to fulfill that order.
                    
                    if z3 != 0 or z4 != 24:
                        tp.section_time(dfc, z1, z2, z3, z4, k, dates_def)
                        dfc = tp.dfnew.copy()
                    

                    '''----- PART 10 ----------'''
                    
                    se.save_export(dfc, x, y, z1, z2, z3, z4, k)

                    # When converting the df to a np array the file is loosing the info on the time variable (used as index in the df)
                    # Possible solution is create a new df whith  the time series as a column, as well as index
       
                
        else:
            y1 = int(y0)
            i1 = i0
            
            if y1 == y:
                
                dg.data_gathering(dates_def, z1, z2, x, y)
                
                dfc = dg.dfc3.copy()
                

                '''----- PART 8 ----------'''
                # If time period is different from 5 min, retrieves a data frame with the mean variables values, according to the time period selected

                if k>1:
                    tp.period_adjust(z1, z2, dfc, k)
                    dfc = tp.dfm.copy()        
                
                '''----- PART 9 ----------'''
                # If the user asked for a specific time period of the day (ex: from 11h to 17h) this function updates the df to fulfill that order.
                
                if z3 != 0 or z4 != 24:
                    tp.section_time(dfc, z1, z2, z3, z4, k, dates_def)
                    dfc = tp.dfnew.copy()
                

                '''----- PART 10 ----------'''
                
                se.save_export(dfc, x, y, z1, z2, z3, z4, k)

                # When converting the df to a np array the file is loosing the info on the time variable (used as index in the df)
                # Possible solution is create a new df whith  the time series as a column, as well as index
   






'''
height = tl.h
t_name = tl.t_n

# Ask for input of tower code name, the code will not continue until a valid code name is given


a2 = 0
a3 = 0

print("Type 1 sonic height and press enter.\nYou will be asked for a new sonic height until you type[end]")

while a3 != 1:
    i = 0
    a1 = 0
    y = input("Sonic height:")
    for a in height:
        
        
        if y == 'end':
            a3 = 1
            
            break
        
        if y == a:
            
            if a2 == 1:
                y_arr = np.append(y_arr, y)
                i_arr = np.append(i_arr, i)
                
            if a2 == 0:
                y_arr = np.array(y)
                i_arr = np.array(i)
                y0 = y
                i0 = i
                a2 = 1
              
            a1 = 1
            break
        i = i + 1
        if a1 != 1:
            print("Sonic height incorrect")
            break
        
    continue
'''

'''
if y_arr.size > 1:
    j = 0
    for y in y_arr:
        
        
        print(y)
        #print(j_arr[i])
        
        i = i_arr.item(j)
        print(i)
        j += 1
else:
    y = y0
    i = i0
'''
'''
i = 0 

to = t_name.copy()

t = 0
j = 0
while j < 50:
    if tl.m[i,j] == 1:
    
        to[t] = t_name[j]
        t += 1
    
    j = j + 1
    continue

tow = to[0:t]
'''
'''
j = 0
    
he = np.empty([11], dtype=int)

v = 0
i = 0
while i < 11:
    if tl.m[i,j] == 1:
    
        he[v] = height[i]
        v += 1
    
    i = i + 1
    continue



hei = he[0:v]
'''
'''
x = 'tnw01'
x1 = 'tnw02'
x2 = 'tnw03'
x3 = 'tnw04'
x4 = 'tnw05'


x_arr = np.array(x)
x_arr = np.append(x_arr, x1)
'''
