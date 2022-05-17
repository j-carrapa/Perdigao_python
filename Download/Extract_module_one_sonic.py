# -*- coding: utf-8 -*-
"""
Created on Fri May 13 16:27:23 2022

@author: Joao
"""


# This module will retrive the desired data for a specific sonic, installed in a specific tower, on a specific date

from netCDF4 import Dataset
import numpy as np
import pandas as pd

#Falta comentar
# Reading the netcd file
#fi, x and y will be given by the main input

fi = "isfs_qc_tiltcor_20170601.nc"

data = Dataset("{}".format(fi) , 'r')

x = 'tnw01'
y = '10m'


# Storing the netCDF data into variables

u = data.variables['u_{}_{}'.format(y, x)]
v = data.variables['v_{}_{}'.format(y, x)]
w = data.variables['w_{}_{}'.format(y, x)]

uu = data.variables['u_u__{}_{}'.format(y, x)]
uv = data.variables['u_v__{}_{}'.format(y, x)]
uw = data.variables['u_w__{}_{}'.format(y, x)]
vv = data.variables['v_v__{}_{}'.format(y, x)]
vw = data.variables['v_w__{}_{}'.format(y, x)]
ww = data.variables['w_w__{}_{}'.format(y, x)]

direc = data.variables['dir_{}_{}'.format(y, x)]
spd = data.variables['spd_{}_{}'.format(y, x)]
ldiag = data.variables['ldiag_{}_{}'.format(y, x)]

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
    df.iloc[time_index] = basetime[time_index], reltime[time_index], u[time_index], v[time_index], w[time_index], spd[time_index], direc[time_index], uu[time_index], vv[time_index], ww[time_index], uv[time_index], uw[time_index], vw[time_index]
    