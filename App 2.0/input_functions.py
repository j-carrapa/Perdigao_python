# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 17:59:08 2022

@author: Joao
"""

# Status: Reviewed

import numpy as np
import dates_array
import tower_location as tl

# This module contains the input routines defined as functions

# Time period - Ask for the period time of the sample, multiples of 5 min: 5, 10, 15, 20, 30min or 1h, doesn´t accept other time periods

def input_time_period ():
    '''Takes none, returns period conversion ratio (int)'''
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
    period_conv = int(period_conv)
    
    return period_conv


# Sectioning mode - User selects if the selected days have data for the whole day, just a time interval per day or continuous data from the start hour to the end hour

def input_sectioning_mode ():
    '''Takes none, Returns sectioning mode code(int)'''
    b1 = 0
    while b1 != 1:
        
        m = input("Select day time sectioning:\n[1] Full days\n[2] Start and end hour for every day\n[3] Start hour for the first day and end hour for the last day only\nPlease select desired mode:")
        m = int(m)
        
        if m == 1:
            b1 = 1
            break
        if m == 2:
            b1 = 1
            break
        if m == 3:
            b1 = 1
            break
        else:
            print("Please select [1],[2] or [3]")
            continue
    return m


# define an array that contains the dates defined by the user - Ask for input of time period

def input_dates_defined ():
    '''Takes none, Returns array with dates defined (np array of int)'''
    dates_tot = dates_array.dates_tot_function()
    dates_16 = dates_array.dates_16_function()
    
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
    
    return dates_def


# Ask for input of which hours of the day or days are of interest for every day defined by the user

def input_hours_sm2 ():
    '''Takes none, Returns array with start and end hour (np array of int)'''
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
    
    hours = np.array([z3, z4])
    
    return hours


# Ask for input of the start hour and end hour for the time period defined by the user

def input_hours_sm3 (z1, z2):
    '''Takes none, Returns array with start and end hour (np array of int)'''
    hour_arr = np.arange(0, 25)
    
    if z1 == z2:
        
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
        
        hours = np.array([z3, z4])
        
        return hours
    
    else:
        
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
            z4 = input("Select ending hour from 1-24:")
            z4 = int(z4)
            for c in hour_arr:
                if z4 == c and z4 != 0:
                    a8 = 1
                    break
            if a8 != 1:
                print("Ending hour incorrect")
                print("Possible ending hours:")
                print(hour_arr[1:25])
            continue
        
        hours = np.array([z3, z4])
        
        return hours


# Input section to learn which towers are of interest. Can be used to get only one tower or multiple tow

def input_multiple_towers ():
    '''Takes none, Returns array with the towers names typed (np array of string)'''
    # Array with tower name code
    
    t_name = tl.towers_name()

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
                if a2 == 0:
                    print("Select at least 1 tower")
                    a1 = 1
                if a2 == 1:
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
    
    x_j_arrays = np.array([x_arr, j_arr])
    return x_j_arrays


# Input section to learn which sonic heights are of interest. Can be used to get only one sonic height or multiple sonic heights - for mode all towers multiple sonics

def input_multiple_sonic_heights():
    '''Takes none, returns array with the sonic heights names typed (np array of string)'''
    # Ask for input of sonic height, the code will not continue until a valid code name is given
    
    height = tl.sonics_height_array()
    m = tl.sonics_towers_map()

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


# Input function to learn height selection mode

def height_selection_mode ():
    '''Takes none, Returns code variable for height mode selection (int)'''
    a = 0
    while a != 1:
        hs = input("Please type height selection mode:\n[1] Selected heights for all selected towers\n[2] Select heights for each tower manually\nPlease select desired mode:")
        try:
            hs = int(hs)
        except:
            pass
        if hs == 1 or hs ==2:
            a = 1
            break
        else:
            print("Please type '1' or '2'")
            continue
    return hs


# Input section to learn which sonic heights are of interest for every tower. Can be used to get only one sonic height or multiple sonic heights - for mode chosen towers choosen sonics and chosen sonic height for all towers

def height_selection_hs1():
    '''Takes none, Returns np array with the selected heights for every tower(np array of int)'''
    height = tl.sonics_height_array()
    a2 = 0
    a3 = 0

    print("Type 1 sonic height and press enter.\nYou will be asked for a new sonic height until you type[end]")

    while a3 != 1:
        a1 = 0
        y = input("Sonic height:")
        for a in height:
            
            if y == 'end':
                a3 = 1
                a1 = 1
                break
            
            
            if y == a:
            
                try:
                    y = int(y)
                    
                    if a2 == 1:
                        y_arr = np.append(y_arr, y)
                        a1 = 1
                        
                    if a2 == 0:
                        y_arr = np.array(y)
                        y0 = y
                    
                        a1 = 1
                        a2 = 1

                    a1 = 1
          
                except:
                    pass
                
            if a1 == 1:
                break
            
            
        if a1 != 1:
            print("Sonic height incorrect")
            print("Available sonic heights:")
            print(height)
            
        continue
    
    if y_arr.size > 1:
        
        y_arr = np.sort(y_arr)

    y_arr = np.unique(y_arr)
    
    return y_arr


# Input section to learn which sonic heights are of interest for each tower. Can be used to get only one sonic height or multiple sonic heights per tower - for mode chosen towers chosen sonics

def height_selection_hs2(x_arr, j_arr):
    '''Takes x_arr and j_arr (np arrays of string), Returns 2D np array with the selected heights for each tower(np 2D array of int)'''
    if x_arr.size == 1:
        
        j = int(j_arr)
        x = x_arr[0]
        san = tl.sonics_available_name(j)
        print("Available heights for {}:".format(x))
        print(san)
        
        a2 = 0
        a4 = 0
        a5 = 0
        while a2 != 1:
            
            y = input("Tower height:")
            
            if y == 'end' and a4 == 1:
                a2 = 1
                a5 = 1
                #a4 = 0
                break
            
            try:
                y = int (y)
            except:
                pass
            
            for b in san:
                if y == b:
                    
                    if a4 == 1:
                        sn = np.append(sn, y)
                        
                    if a4 == 0:
                        sn = np.array(y)
                        a4 = 1
                        
                    
                    a5 = 1
                    break
                
            if a5 != 1:
                print("Select an appropriate height")

            continue
        
        sdf = np.array([sn])
        sdf = np.sort(sdf)
        sdf = np.unique(sdf)
        
    else:
        
        sdf = np.zeros((11,50))

        j1 = 0
        i1 = 0

        for a in x_arr:
            
            j = int(j_arr[j1])
            san = tl.sonics_available_name(j)
            print("Available heights for {}:".format(a))
            print(san)
            
            a2 = 0
            a4 = 0
            while a2 != 1:
                
                a5 = 0
                
                y = input("Tower height:")
                
                if y == 'end' and a4 == 1:
                    a2 = 1
                    a5 = 1
                    a4 = 0
                    break
                
                try:
                    y = int (y)
                except:
                    pass
                
                for b in san:
                    if y == b:
                        
                        if a4 == 1:
                            
                            sdf[i1,j1] = y
                            temp = sdf[:, j1]
                            temp = np.unique(temp)
                            temp = np.sort(temp)
                            temp = temp[1:]
                            a = temp.size
                            b = 11-a
                            while b>0:
                                temp = np.append(temp, 0)
                                b -=1
                                
                            sdf[:, j1] = temp[:]
                            
                        if a4 == 0:
                            
                            sdf[i1,j1] = y
                            a = 1
                            a4 = 1
                            
                        i1 = a
                        a5 = 1
                        break
                    
                if a5 != 1:
                    print("Select an appropriate height")

                continue 
            
            j1 += 1
            i1 = 0
    
    return sdf

