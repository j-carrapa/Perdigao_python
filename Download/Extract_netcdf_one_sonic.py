# -*- coding: utf-8 -*-
"""
Created on Tue May 10 23:03:34 2022

@author: João
"""


from netCDF4 import Dataset
import numpy as np
import pandas as pd
import Tower_location as tl



# Reading the netcd file

fi = "isfs_qc_tiltcor_20170601.nc"

data = Dataset("{}".format(fi) , 'r')

# Array with tower name code

t_name = np.array(["tnw01", "tnw02", "tnw03", "tnw04", "tnw05", "tnw06", "tnw07", "tnw08", "tnw09", "tnw10", "tnw11", "tnw12", "tnw13", "tnw14", "tnw15", "tnw16", "tse01", "tse02", "tse04", "tse05", "tse06", "tse07", "tse08", "tse09", "tse10", "tse11", "tse12", "tse13", "rsw01", "rsw02", "rsw03", "rsw04", "rsw05", "rsw06", "rsw07", "rsw08", "rne01", "rne02", "rne03", "rne04", "rne06", "rne07", "v01", "v03", "v04", "v05", "v06", "v07", "Extreme_SW", "Extreme_NE"])


# Ask for input of tower code name, the code will not continue until a valid code name is given

a1 = 0

while a1 != 1:
    j = 0
    x = input("Tower name code:")
    for a in t_name:
        if x == a:
            a1 = 1
            break
        j = j + 1
    if a1 != 1:
        print("Code name incorrect")
        
    continue   
          


# Neste ficheiro não existem coordenadas para algumas torres, verificar se é geral

if x != "tnw04" and x != "tnw12" and x != "tnw13" and x != "tnw14" and x != "tnw15" and x != "tnw16" and x != "tse05" and x != "Extreme_SW" and x != "Extreme_NE":

    lat = data.variables['latitude_{}'.format(x)]
    lat_data = data.variables['latitude_{}'.format(x)][:]

    lon = data.variables['longitude_{}'.format(x)]
    lon_data = data.variables['longitude_{}'.format(x)][:]


# Display which sonics heights are available for that tower

height = np.array(["2m", "4m", "6m", "8m", "10m", "20m", "30m", "40m", "60m", "80m", "100m"])

i = 0
while i < 12:
    if tl.m[i,j] == 1:
        print(height[i])
    
    i = i + 1
    continue



#  Ask for input of sonic height, the code will not continue until a valid height for the choosen tower is given



a3 = 0
while a3 != 1:
    a2 = 0
    while a2 != 1:
        i = 0
        y = input("Tower height:")
        for b in height:
            if y == b:
                a2 = 1
                break
            i = i + 1
        
        if a2 != 1:
            print("Select an appropriate height")
            
        continue 
    if tl.m[i,j] == 1:
        a3 = 1
    else:
        print("This tower doesn't have sonics for {} heihgt, select an appropriate height".format(y))
    continue


'''
i = 0
while i != 1:
    y = input("Tower height:")
    for b in height:
        if y == b:
            i = 1
            break
    if i != 1:
        print("This tower doesn't have a sonic for that height")
        
    continue   
'''




# Extracção dos valores das variáveis

u = data.variables['u_{}_{}'.format(y, x)]
u_data = data.variables['u_{}_{}'.format(y, x)][:]
v = data.variables['v_{}_{}'.format(y, x)]
v_data = data.variables['v_{}_{}'.format(y, x)][:]
w = data.variables['w_{}_{}'.format(y, x)]
w_data = data.variables['w_{}_{}'.format(y, x)][:]

u_u = data.variables['u_u__{}_{}'.format(y, x)]
u_u_data = data.variables['u_u__{}_{}'.format(y, x)][:]
u_v = data.variables['u_v__{}_{}'.format(y, x)]
u_v_data = data.variables['u_v__{}_{}'.format(y, x)][:]
u_w = data.variables['u_w__{}_{}'.format(y, x)]
u_w_data = data.variables['u_w__{}_{}'.format(y, x)][:]
v_v = data.variables['v_v__{}_{}'.format(y, x)]
v_v_data = data.variables['v_v__{}_{}'.format(y, x)][:]
v_w = data.variables['v_w__{}_{}'.format(y, x)]
v_w_data = data.variables['v_w__{}_{}'.format(y, x)][:]
w_w = data.variables['w_w__{}_{}'.format(y, x)]
w_w_data = data.variables['w_w__{}_{}'.format(y, x)][:]



#não sei que variável é esta 

counts = data.variables['counts_2m_tse05']
counts_data = data.variables['counts_2m_tse05'][:]


# Barometric Pressure, Paroscientific 6000
P_2m_tse05 = data.variables['P_2m_tse05']
P_2m_tse05_data = data.variables['P_2m_tse05'][:]

# não sei que variável é esta
P_P__2m_tse05 = data.variables['P_P__2m_tse05']
P_P__2m_tse05_data = data.variables['P_P__2m_tse05'][:]



#print(data.variables.keys())

# Joining every variables of interest in one numpy array



