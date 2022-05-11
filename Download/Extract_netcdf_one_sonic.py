# -*- coding: utf-8 -*-
"""
Created on Tue May 10 23:03:34 2022

@author: João
"""


from netCDF4 import Dataset
import numpy as np
import pandas as pd


# Reading the netcd file
data = Dataset("isfs_qc_tiltcor_20170601.nc", 'r')


# escolha do mastro, falta fazer função de input
x = 'tse05'

# Neste ficheiro não existem coordenadas para algumas torres, verificar se é geral

if x != "tse05" and x != "tnw04":

    lat = data.variables['latitude_{}'.format(x)]
    lat_data = data.variables['latitude_{}'.format(x)][:]

    lon = data.variables['longitude_{}'.format(x)]
    lon_data = data.variables['longitude_{}'.format(x)][:]



# escolha do anemómetro, falta fazer função de input

y = '2m'

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

