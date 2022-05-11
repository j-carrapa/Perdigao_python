# -*- coding: utf-8 -*-
"""
Created on Mon May  9 17:02:03 2022

@author: Baba
"""

# Extract netcdf

from netCDF4 import Dataset
import numpy as np
import pandas as pd


data = Dataset("isfs_qc_tiltcor_20170630.nc", 'r')

#print(data)

#print(data.variables.keys())

sites = data.variables['sites']

#print(sites)

lat_tnw01 = data.variables['latitude_tnw01']

#print(lat_tnw01)

lon_tnw01 = data.variables['longitude_tnw01']

#print(lon_tnw01)

base_time = data.variables['base_time']

#print(base_time)

time = data.variables['time']

#print(time)

T_100m_tse04 = data.variables['T_100m_tse04']

#print(T_100m_tse04)

u_10m_tse11 = data.variables['u_10m_tse11']

#print(u_10m_tse11)

tc_10m_tse11 = data.variables['tc_10m_tse11']

#print(tc_10m_tse11)


u_u__10m_tse11 = data.variables['u_u__10m_tse11']
u_v__10m_tse11 = data.variables['u_v__10m_tse11']
u_w__10m_tse11 = data.variables['u_w__10m_tse11']
v_v__10m_tse11 = data.variables['v_v__10m_tse11']
v_w__10m_tse11 = data.variables['v_w__10m_tse11']
w_w__10m_tse11 = data.variables['w_w__10m_tse11']

dir_10m_tse11 = data.variables['dir_10m_tse11']
spd_10m_tse11 = data.variables['spd_10m_tse11']
ldiag_10m_tse11 = data.variables['ldiag_10m_tse11']

#print(ldiag_10m_tse11)

u_tc__10m_tse11 = data.variables['u_tc__10m_tse11']

#print(u_tc__10m_tse11)


'''for t in u_10m_tse11:
    print(u_10m_tse11[t])'''

# acessing the data from the variables

sites_data = data.variables['sites'][:]

#print(sites_data)

base_time_data = data.variables['base_time'][:]

#print(base_time_data)

time_data = data.variables['time'][:]

#print(time_data)


lon_data = data.variables['longitude_tnw01'][:]#o nome dentro da expressão é o da key do ficheiro

#print(lon_data)


lat_data = data.variables['latitude_tnw01'][:]

#print(lat_data)





