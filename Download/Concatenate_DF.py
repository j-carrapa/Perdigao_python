# -*- coding: utf-8 -*-
"""
Created on Tue May 17 16:55:28 2022

@author: Joao
"""

# Concatenate DataFrames

from netCDF4 import Dataset
import numpy as np
import pandas as pd

#File 1
# Reading the netcd file
#fi, x and y will be given by the main input

fi1 = "20170601.nc"

data = Dataset("{}".format(fi1) , 'r')

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

df1 = pd.DataFrame(0, columns= ['basetime', 'time', 'u','v', 'w', 'vh', 'dir','uu', 'vv', 'ww', 'uv', 'uw', 'vw'], index = time_range)

# Create a numpy array with the size of the time variable

dt = np.arange(0, data.variables['time'].size)

# Filling the empty pandas data frame with the values of the variables for each time value

for time_index in dt:
    df1.iloc[time_index] = basetime[time_index], reltime[time_index], u[time_index], v[time_index], w[time_index], spd[time_index], direc[time_index], uu[time_index], vv[time_index], ww[time_index], uv[time_index], uw[time_index], vw[time_index]




#Falta comentar
# Reading the netcd file
#fi, x and y will be given by the main input

fi2 = "20170602.nc"

data = Dataset("{}".format(fi2) , 'r')



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

df2 = pd.DataFrame(0, columns= ['basetime', 'time', 'u','v', 'w', 'vh', 'dir','uu', 'vv', 'ww', 'uv', 'uw', 'vw'], index = time_range)


# Filling the empty pandas data frame with the values of the variables for each time value

for time_index in dt:
    df2.iloc[time_index] = basetime[time_index], reltime[time_index], u[time_index], v[time_index], w[time_index], spd[time_index], direc[time_index], uu[time_index], vv[time_index], ww[time_index], uv[time_index], uw[time_index], vw[time_index]

#Falta comentar
# Reading the netcd file
#fi, x and y will be given by the main input

fi3 = "20170603.nc"

data = Dataset("{}".format(fi3) , 'r')



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

df3 = pd.DataFrame(0, columns= ['basetime', 'time', 'u','v', 'w', 'vh', 'dir','uu', 'vv', 'ww', 'uv', 'uw', 'vw'], index = time_range)


# Filling the empty pandas data frame with the values of the variables for each time value

for time_index in dt:
    df3.iloc[time_index] = basetime[time_index], reltime[time_index], u[time_index], v[time_index], w[time_index], spd[time_index], direc[time_index], uu[time_index], vv[time_index], ww[time_index], uv[time_index], uw[time_index], vw[time_index]




frames_list = [df1, df2, df3]

m=0

for z in frames_list:
          
    if m == 0:
        dfc = df1.copy()
        frames = [dfc]
        m = 1
    if m == 1:
        frames.append(z)
        result = pd.concat(frames)
        dfc = result.copy()
        frames = [dfc]

