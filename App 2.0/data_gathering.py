# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 11:23:15 2022

@author: Joao
"""
# Status: Reviewed

# Data frame extract and concatenate module

import extract_function as ex
import concatenate_df as co
import numpy as np
import turbulence_parameters as tu
import time_process as tp
import pandas as pd

# Data gathering Function
# The function data_gathering outputs a pandas data frame containing the variables of interest of a series of consecutive dates defined by the user for 1 sonic in 1 tower

def data_gathering (dates_def, z1, z2, x, y):
    '''Takes dates to retrieve data (np array of int), start date (int), end date (int), tower code name (str), sonic height(int), Returns data frame with sonic data for that period (pandas DataFrame)'''
    n = 0
    m = 0
    
    if z1 == z2:
        
        dfc = ex.extract(z1, x, y, n)
    
    else:
        for z in dates_def:
            if m == 1:
                df = ex.extract(z, x, y, n)
                dfc = co.concatenate(dfc, df)
                
            if m == 0:
                
                dfc = ex.extract(z, x, y, n)
                m = 1
            n +=1
    return dfc

'''
dates_def = np.array([20170610])
z1 = z2 = 20170610
x = 'tnw01'
y = 10
k = 4

dfc = data_gathering(dates_def, z1, z2, x, y)


uu, vv, ww = tu.var_k(dfc, k)
tke_arr = tu.tke_k(dfc, k)
ti_arr = tu.ti_k(dfc, k)
tih_arr = tu.tih_k(dfc, k)

dfc = tp.period_adjust(z1, z2, dfc, k)
df_covar = dfc.iloc[:,10:]
uv = dfc.iloc[:,10].to_numpy()
uw = dfc.iloc[:,11].to_numpy()
vw = dfc.iloc[:,12].to_numpy()

dfc = dfc.iloc[:,:7]
dfc = tu.var_append(dfc, uu, vv, ww)
dfc = tu.covar_append(dfc, uv, uw, vw)
dfc = tu.turb_append(dfc, tke_arr, ti_arr, tih_arr)


#'''