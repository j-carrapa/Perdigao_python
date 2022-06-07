# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 15:08:07 2022

@author: João
"""

from netCDF4 import Dataset
import numpy as np
import pandas as pd


# Extracting from netcdf into a pandas data frame
# Input args: fi - day code, x - tower code, y - sonic height, n - number of the day in the time series requested (if you want 2 consecutive days, in the first day n=0 and in the second day n=1)
# Output: df - dataframe containing the variables of interest for that day, tower and sonic

def extract (fi, x, y, n):
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
 #   ldiag = data.variables['ldiag_{}m_{}'.format(y, x)]

    basetime = data.variables['base_time']
    reltime = data.variables['time']


    # Creating an empty pandas dataframe
    starting_time = data.variables['time'].units[14:29]+ '2:30'
    ending_time = data.variables['time'].units[14:25]+ '23:57:30'
    time_range = pd.date_range(start= starting_time, end= ending_time, periods= 288)

    global df
    df = pd.DataFrame(0, columns= ['basetime', 'time', 'u','v', 'w', 'vh', 'dir','uu', 'vv', 'ww', 'uv', 'uw', 'vw'], index = time_range)

    # Create a numpy array with the size of the time variable

    dt = np.arange(0, data.variables['time'].size)

    # Filling the empty pandas data frame with the values of the variables for each time value

    for time_index in dt:
        df.iloc[time_index] = basetime[time_index], reltime[time_index] + 86400*n, u[time_index], v[time_index], w[time_index], spd[time_index], direc[time_index], uu[time_index], vv[time_index], ww[time_index], uv[time_index], uw[time_index], vw[time_index]

    return df

'''
# Checking if the function is working - Apparently it is
fi = '20170601'
y = '10'
x = 'tnw01'
n = 1

extract(fi, x, y, n)
#'''
