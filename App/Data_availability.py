# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 11:11:21 2022

@author: Joao
"""

# Mapping of data availability

from netCDF4 import Dataset
import extract_function as ex
import Download as dl
import numpy as np
import pandas as pd
import Tower_location as tl
import Dates_array as da

# This Function is used to count how many times the wind speed variable passed as an argument (var) has values between the defined interval

def wind_speed_count (var):
    
    c = 0
    for a3 in var:
        if a3 > 30 or a3 < -30:
            continue
        if a3 < 30 and a3 > -30:
            c = c+1
    
    global count
    count = c
    return count

# This Function is used to count how many times the variance variable passed as an argument (var) has values between the defined interval

def variance_count (var):
    
    c = 0
    for a3 in var:
        if a3 > 50 or a3 < -50:
            continue
        if a3 < 50 and a3 > -50:
            c = c+1
    
    global count
    count = c
    return count

# This function loops through every time period and every variable to check the data availability for the selected sonic (x, y)
# Outputs a value that represents the data availabilty for the specified sonic in the specified day (fi)

def availability_one_sonic(fi, x, y):
    
    n = 0
    m = 3
    
    try:
        ex.extract(fi, x, y, n)
        dfc = ex.df

        u = dfc[["u"]].to_numpy()
        v = dfc[["v"]].to_numpy()
        w = dfc[["w"]].to_numpy()
        vh = dfc[["vh"]].to_numpy()
        dire = dfc[["dir"]].to_numpy()
        uu = dfc[["uu"]].to_numpy()
        vv = dfc[["vv"]].to_numpy()
        ww = dfc[["ww"]].to_numpy()
        uv = dfc[["uv"]].to_numpy()
        uw = dfc[["uw"]].to_numpy()
        vw = dfc[["vw"]].to_numpy()


        wind_speed_count(u)
        uc = count
                
        wind_speed_count(v)
        vc = count

        wind_speed_count(w)
        wc = count

        wind_speed_count(vh)
        vhc = count

        dirc = 0
        for a3 in dire:
            if a3 > 360 or a3 < 0:
                continue
            if a3 < 360 and a3 > 0:
                dirc = dirc+1
                
        variance_count(uu)
        uuc = count

        variance_count(vv)
        vvc = count

        variance_count(ww)
        wwc = count

        variance_count(uv)
        uvc = count

        variance_count(uw)
        uwc = count

        variance_count(vw)
        vwc = count
        
    except KeyError:
        m = 0
        
    except:
        m = 3
        
    else:
        if uc == 288 and vc == 288 and wc == 288 and vhc == 288 and dirc == 288 and uuc == 288 and vvc == 288 and wwc == 288 and uvc == 288 and uwc == 288 and vwc == 288:
            m = 1
            
        if uc == 0 and vc == 0 and wc == 0 and vhc == 0 and dirc == 0 and uuc == 0 and vvc == 0 and wwc == 0 and uvc == 0 and uwc == 0 and vwc == 0:
            m = 0
        if (uc < 288 or vc < 288 or wc < 288 or vhc < 288 or dirc < 288 or uuc < 288 or vvc < 288 or wwc < 288 or uvc < 288 or uwc < 288 or vwc < 288) and (uc > 0 and vc > 0 and wc > 0 and vhc > 0 and dirc > 0 and uuc > 0 and vvc > 0 and wwc > 0 and uvc > 0 and uwc > 0 and vwc > 0):
            m = 2
            
        if m != 0 and m != 1 and m != 2:
            m = 3
            
    global ava
    ava = m
    return ava

# This function outputs an array with the towers that have available data for that day

def availability_towers_arr (fi):
    
    data = Dataset("{}.nc".format(fi) , 'r')

    sites = data.variables['sites']

    #print(sites)
    #print(data.variables.keys())

    t_name = tl.t_name

    i=0
    for a in data.variables.keys():
        
        b = str(a)
        
        if b[0:3] == 'lat' or b[0:3] == 'lon':
            continue
        
        if i == 0:
            
            for a2 in t_name:
                if b[-5:] == a2:
                    arr = np.array(a2)
                    i = 1
                    break
                
                if b[-3:] == a2:
                    arr = np.array(a2)
                    i = 1
                    break
        
        if i == 1:
            
            for a2 in t_name:
                if b[-5:] == a2:
                    arr = np.append(arr, [a2])
                if b[-3:] == a2:
                    arr = np.append(arr, [a2])
            
    arr = np.unique(arr)
    global ar
    ar = arr.copy()
    return ar

# This function outputs an array with all the names of the sonics and respective tower in the format: ex.: 'tnw01_2m'

def name_arr ():
    
    name_array = np.array(["tnw01_2m"])

    t_name = tl.t_name

    for x in t_name:
        
        j = np.where(t_name == x)
        j = j[0]
        
        tl.sonics_available_name(j)
        hei = tl.hei.copy()
        
        for y in hei:
            
            name = "{}_{}m".format(x, y)
            name_array = np.append(name_array, [name])
            
    name_array = name_array[1:]
    global nam
    nam = name_array.copy()
    return nam

# This function creates the data frame of the availability map with only the first column, if the '20161129' file is not present in the directory, the first line must come out of comment 

def avail_map_creation ():
    
    '''
    dl.download(dates_def)
    '''
    fi = '20161129'
    
    #Creating day array for the info for each sonic per day
    #Creating of name_array which will be the index of the data frame, with the code name of each sonic
    
    day_arr = np.zeros(168)

    name_arr()
    name_array = nam

    i = 0
    for a in name_array:
        
        if i < 149:
            
            x_a = a[0:5]
            x = str(x_a)
            
            a_s = len(a)
            
            if a_s == 8:
                
                y_a = a[-2:-1]
                y = str(y_a)
            
            if a_s == 9:
                
                y_a = a[-3:-1]
                y = str(y_a)
            
            if a_s == 10:
                
                y_a = a[-4:-1]
                y = str(y_a)
            
            availability_one_sonic(fi, x, y)
            day_arr[i] = ava
            i +=1
            continue
            
        if i >= 149:
            
            x_a = a[0:3]
            x = str(x_a)
            
            a_s = len(a)
            
            if a_s == 6:
                
                y_a = a[-2:-1]
                y = str(y_a)
            
            if a_s == 7:
                
                y_a = a[-3:-1]
                y = str(y_a)
            
            
            availability_one_sonic(fi, x, y)
            day_arr[i] = ava
            i +=1
    
    # Create the data frame
    
    df = pd.DataFrame(data=day_arr, index=name_array, columns=["20161129"])
    
    # Saving the data frame into an external file

    df.to_pickle("Availability_map.pkl")

# This function fills the availability map, using the dates_def input, the function creates new columns for data availability in the defined dates, and appends them to the existing data frame (df)
# Outputs a new availabilty map with data for more days (dates_def)

def avail_map_filling (dates_def, df):
    
    dl.download(dates_def)
    
    #Creating of name_array which will be the index of the data frame, with the code name of each sonic
    name_arr()
    name_array = nam
    
    for fi in dates_def:
        
        #Creating day array for the info for each sonic per day
        
        day_arr = np.zeros(168)

        i = 0
        for a in name_array:
            
            if i < 149:
                
                x_a = a[0:5]
                x = str(x_a)
                
                a_s = len(a)
                
                if a_s == 8:
                    
                    y_a = a[-2:-1]
                    y = str(y_a)
                
                if a_s == 9:
                    
                    y_a = a[-3:-1]
                    y = str(y_a)
                
                if a_s == 10:
                    
                    y_a = a[-4:-1]
                    y = str(y_a)
                
                availability_one_sonic(fi, x, y)
                day_arr[i] = ava
                i +=1
                continue
                
            if i >= 149:
                
                x_a = a[0:3]
                x = str(x_a)
                
                a_s = len(a)
                
                if a_s == 6:
                    
                    y_a = a[-2:-1]
                    y = str(y_a)
                
                if a_s == 7:
                    
                    y_a = a[-3:-1]
                    y = str(y_a)
                
                
                availability_one_sonic(fi, x, y)
                day_arr[i] = ava
                i +=1
            
            df['{}'.format(fi)] = day_arr.tolist()
    
    
    
    # Saving the data frame into an external file

    df.to_pickle("Availability_map.pkl")

# Avail_map_creation()
# To create a new availability map, call the avail_map_creation function and make sure the '20161129' file is present in the directory, if not, check the avail_map_creation function and take the first line out of comment 

#avail_map_creation()

# Get the availability map, might not be a completely filled version, check for the map status

df = pd.read_pickle("Availability_map.pkl")

# Code lines for filling the map, in regular PC's it is recommended to set dates_def to 10 days sets, it takes time to create the full map and it is safer that way

#dfc = df.copy()

#dfc.to_pickle("Availability_map_160.pkl")

'''
dates_tot = da.d

dates_def = dates_tot[170:]

df.to_excel('Availability_map.xls')
'''
'''
dl.download(dates_def)

avail_map_filling(dates_def, df)

df = pd.read_pickle("Availability_map.pkl")

#'''

# Code for reordering columns if anything went wrong

'''
# Reorder columns
cols = df.columns.tolist()


colu =cols[0:20] + cols[33:]+ cols[20:33]

df = df[colu]

df.to_pickle("Availability_map.pkl")
'''