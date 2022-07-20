# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 15:08:07 2022

@author: João
"""
# Status: Reviewed

from netCDF4 import Dataset
import numpy as np
import pandas as pd
import time

# Extracting from netcdf into a pandas data frame
# Input args: fi - day code, x - tower code, y - sonic height, n - number of the day in the time series requested (if you want 2 consecutive days, in the first day n=0 and in the second day n=1)
# Output: df - dataframe containing the variables of interest for that day, tower and sonic

def extract (fi, x, y, n):
    '''Takes fi - day code (int), x - tower code name (str), y - sonic height (int) and n - number that increments by 1 for consecutive days starting in zero (int), Returns data frame with the extracted variables (pandas DataFrame)'''
    # n is used to garantee continuous data in the time stamp variable 'time'
    data = Dataset("{}.nc".format(fi) , 'r')
    
    # Storing the netCDF data into variables

    u = data.variables['u_{}m_{}'.format(y, x)]
    v = data.variables['v_{}m_{}'.format(y, x)]
    w = data.variables['w_{}m_{}'.format(y, x)]

    uu = data.variables['u_u__{}m_{}'.format(y, x)]
    uv = data.variables['u_v__{}m_{}'.format(y, x)]
    uw = data.variables['u_w__{}m_{}'.format(y, x)]
    vv = data.variables['v_v__{}m_{}'.format(y, x)]
    vw = data.variables['v_w__{}m_{}'.format(y, x)]
    ww = data.variables['w_w__{}m_{}'.format(y, x)]

    direc = data.variables['dir_{}m_{}'.format(y, x)]
    spd = data.variables['spd_{}m_{}'.format(y, x)]

    basetime = data.variables['base_time']
    reltime = data.variables['time']

    # Creating an empty pandas dataframe
    starting_time = data.variables['time'].units[14:29]+ '2:30'
    ending_time = data.variables['time'].units[14:25]+ '23:57:30'
    time_range = pd.date_range(start= starting_time, end= ending_time, periods= 288)
    
    df = pd.DataFrame(0, columns= ['basetime', 'time', 'u','v', 'w', 'vh', 'dir','uu', 'vv', 'ww', 'uv', 'uw', 'vw'], index = time_range)

    # Create a numpy array with the size of the time variable

    dt = np.arange(0, data.variables['time'].size)

    # Filling the empty pandas data frame with the values of the variables for each time value

    for time_index in dt:
        df.iloc[time_index] = basetime[time_index], reltime[time_index] + 86400*n, u[time_index], v[time_index], w[time_index], spd[time_index], direc[time_index], uu[time_index], vv[time_index], ww[time_index], uv[time_index], uw[time_index], vw[time_index]

    return df
    

#extract_2(fi, x, y)

def extract_2 (fi, x, y):
    '''Takes day code (int), tower code name (str), sonic height (int), Returns array with the size of the time variable and containing index numbers starting in zero (numpy array of int)'''
    data = Dataset("{}.nc".format(fi) , 'r')
    dt = np.arange(0, data.variables['time'].size)
    return dt
  
  
#extract_start_time(z1, k)

def extract_start_time (z1, k, h):
    '''Takes day (int), period conversion constant (int) and start hour (int), Returns first period time data (str)'''
    data = Dataset("{}.nc".format(z1) , 'r')
    
    st = 150*k + 3600*h
    stf = time.strftime('%H:%M:%S', time.gmtime(st))
    start = data.variables['time'].units[14:25]+ stf
    return start

#extract_end_time(z2, k)

def extract_end_time (z2, k, h):
    '''Takes day (int), period conversion constant (int) and start hour (int), Returns first period time data (str)'''    
    data = Dataset("{}.nc".format(z2) , 'r')
    
    en = 86400 - (150*k + (24-h)*3600)
    e = time.strftime('%H:%M:%S', time.gmtime(en))
    end = data.variables['time'].units[14:25]+ e
    return end

