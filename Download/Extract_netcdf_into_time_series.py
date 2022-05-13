# -*- coding: utf-8 -*-
"""
Created on Tue May 10 10:03:27 2022

@author: João
"""


from netCDF4 import Dataset
import numpy as np
import pandas as pd


# Reading the netcd file

fi = "isfs_qc_tiltcor_20170630.nc"

data = Dataset("{}".format(fi) , 'r')

# Storing the lat and lon data into variables
lat_tnw01 = data.variables['latitude_tnw01']

lon_tnw01 = data.variables['longitude_tnw01']


# Storing the u, v, w wind speed at 10m for tse11 data into variables
u_10m_tse11 = data.variables['u_10m_tse11']
v_10m_tse11 = data.variables['v_10m_tse11']
w_10m_tse11 = data.variables['w_10m_tse11']


u_u__10m_tse11 = data.variables['u_u__10m_tse11']
u_v__10m_tse11 = data.variables['u_v__10m_tse11']
u_w__10m_tse11 = data.variables['u_w__10m_tse11']
v_v__10m_tse11 = data.variables['v_v__10m_tse11']
v_w__10m_tse11 = data.variables['v_w__10m_tse11']
w_w__10m_tse11 = data.variables['w_w__10m_tse11']

dir_10m_tse11 = data.variables['dir_10m_tse11']
spd_10m_tse11 = data.variables['spd_10m_tse11']
ldiag_10m_tse11 = data.variables['ldiag_10m_tse11']



# Creating an empty pandas dataframe
starting_time = data.variables['time'].units[14:29]+ '2:30'
ending_time = data.variables['time'].units[14:25]+ '23:57:30'
time_range = pd.date_range(start= starting_time, end= ending_time, periods= 288)

df = pd.DataFrame(0, columns= ['U Wind Speed 10m','V Wind Speed 10m', 'W Wind Speed 10m', 'u_u', 'u_v', 'u_w', 'v_v', 'v_w', 'w_w', 'dir', 'spd', 'ldiag'], index = time_range)

dt = np.arange(0, data.variables['time'].size)

for time_index in dt:
    df.iloc[time_index] = u_10m_tse11[time_index], v_10m_tse11[time_index], w_10m_tse11[time_index], u_u__10m_tse11[time_index], u_v__10m_tse11[time_index], u_w__10m_tse11[time_index], v_v__10m_tse11[time_index], v_w__10m_tse11[time_index], w_w__10m_tse11[time_index], dir_10m_tse11[time_index], spd_10m_tse11[time_index], ldiag_10m_tse11[time_index]
    
    
#vetor = np.array([u_10m_tse11[0], v_10m_tse11[0], w_10m_tse11[0]]
    

#df.iloc[0] = u_10m_tse11[0], v_10m_tse11[0], w_10m_tse11[0], u_u__10m_tse11[0], u_v__10m_tse11[0], u_w__10m_tse11[0], v_v__10m_tse11[0], v_w__10m_tse11[0], w_w__10m_tse11[0], dir_10m_tse11[0], spd_10m_tse11[0], ldiag_10m_tse11[0]       
    
#print(u_10m_tse11[0], v_10m_tse11[0], w_10m_tse11[0])


# Numpy arrays



n_u_10m_tse11 = np.array(data['u_10m_tse11'][:])
n_v_10m_tse11 = np.array(data['v_10m_tse11'][:])
n_w_10m_tse11 = np.array(data['w_10m_tse11'][:])


n_u_u__10m_tse11 = np.array(data['u_u__10m_tse11'][:])
n_u_v__10m_tse11 = np.array(data['u_v__10m_tse11'][:])
n_u_w__10m_tse11 = np.array(data['u_w__10m_tse11'][:])
n_v_v__10m_tse11 = np.array(data['v_v__10m_tse11'][:])
n_v_w__10m_tse11 = np.array(data['v_w__10m_tse11'][:])
n_w_w__10m_tse11 = np.array(data['w_w__10m_tse11'][:])

n_dir_10m_tse11 = np.array(data['dir_10m_tse11'][:])
n_spd_10m_tse11 = np.array(data['spd_10m_tse11'][:])
n_ldiag_10m_tse11 = np.array(data['ldiag_10m_tse11'][:])




# automatic array creation for defined height in defined site
'''x = '10m_tse11'

n0_variables = np.array(['u_','v_', 'w_', 'u_u__', 'u_v__', 'u_w__', 'v_v__', 'v_w__', 'w_w__', 'dir_', 'spd_', 'ldiag_'])


i=0


for var in n0_variables:
#    print(var)
    temp = var
#    print(var)
    var = temp + str(x)
    n1_var[i] = var
    i = i+1
#    print(var)'''



    
'''temp = n_variables[0]
n_variables[0] = temp + str(x)'''
#print(n_variables)

#vel=np.array(ncfile['VEL'][:])



# Saving the Data frame into a CSV and a Excel file

df.to_csv('file1.csv')

df.to_excel('file1.xls')
