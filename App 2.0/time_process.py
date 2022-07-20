# -*- coding: utf-8 -*-
"""
Created on Fri May 27 15:29:56 2022

@author: Joao
"""
# Status: Reviewed

# - Falta limpar este modulo

# Time process functions

import pandas as pd
import numpy as np
import extract_function as ex
import concatenate_df as co

# - Period adjust function

def period_adjust (z1, z2, dfc, k):
    '''Takes start date (int), end date (int), 5 min period data frame (pandas Data Frame) and time period conversion value (int), Returns period adjusted data frame (pandas Data Frame)'''
    n = z2 - z1 +1
    t = (288*n)/k
    h = 0
    
    starting_time = ex.extract_start_time(z1, k, h)
    
    ending_time = ex.extract_end_time(z2, k, h)
    
    time_range = pd.date_range(start= starting_time, end= ending_time, periods= t)
    dfmean = pd.DataFrame(0, columns= ['basetime', 'time', 'u','v', 'w', 'vh', 'dir','uu', 'vv', 'ww', 'uv', 'uw', 'vw'], index = time_range) 
    dt = np.arange(0, 288*n)
    
    i = 0
    j = 0
    b_mean = 0
    rel_time_m = 0
    u_m = 0
    v_m = 0
    w_m = 0
    vh_m = 0
    dir_m = 0
    uu_m = 0
    vv_m = 0
    ww_m = 0
    uv_m = 0
    uw_m = 0
    vw_m = 0
    
    for a in dt:
            
        if i < k:
            
            basetime = dfc.iat[a, 0]
            b_mean = b_mean + basetime
            
            reltime = dfc.iat[a, 1]
            rel_time_m = rel_time_m + reltime
            
            u = dfc.iat[a, 2]
            u_m = u_m + u
            
            v = dfc.iat[a, 3]
            v_m = v_m + v
            
            w = dfc.iat[a, 4]
            w_m = w_m + w
            
            vh = dfc.iat[a, 4]
            vh_m = vh_m + vh
            
            di = dfc.iat[a, 6]
            dir_m = dir_m + di
            
            uu = dfc.iat[a, 7]
            uu_m = uu_m + uu
            
            vv = dfc.iat[a, 8]
            vv_m = vv_m + vv
            
            ww = dfc.iat[a, 9]
            ww_m = ww_m + ww
            
            uv = dfc.iat[a, 10]
            uv_m = uv_m + uv
            
            uw = dfc.iat[a, 11]
            uw_m = uw_m + uw
            
            vw = dfc.iat[a, 12]
            vw_m = vw_m + vw
            
        if i == (k-1):
            
            dfmean.iloc[j] = b_mean/k, rel_time_m/k, u_m/k, v_m/k, w_m/k, vh_m/k, dir_m/k, uu_m/k, vv_m/k, ww_m/k, uv_m/k, uw_m/k, vw_m/k         
        
        i += 1
        
        if i == k:
            
            i = 0
            
            b_mean = 0
            rel_time_m = 0
            u_m = 0
            v_m = 0
            w_m = 0
            vh_m = 0
            dir_m = 0
            uu_m = 0
            vv_m = 0
            ww_m = 0
            uv_m = 0
            uw_m = 0
            vw_m = 0
            
            j += 1
        
    return dfmean


# Function to section the data frame according to the start and end hour of mode sm = 2

def section_time_sm2 (dfc, z1, z2, z3, z4, k, dates_def):
    '''Takes time indexed data frame (pandas Data Frame), start date (int), end date (int), start hour for every day (int), end hour for every day (int), time period conversion value (int) and array with the selected dates (np array of int), Returns sectioned data frame (pandas Data Frame)'''    
    n = 0
    
    if z1 == z2:
        
        n0 = z2-z1

        a = int(((12*z3)/k))
        b = int(((12*z4)/k)+(288/k)*n0)

        df = dfc.iloc[a:b]
        
    else:
        for a in dates_def:
            
            a1 = int(((12*z3)/k)+(288/k)*n)
            b1 = int(((12*z4)/k)+(288/k)*n)
            
            df = dfc.iloc[a1:b1]
            
            if n == 0:
                
                df1 = df.copy()
            
            else:
                
                df = co.concatenate(df1, df)
                df1 = df.copy()
                
            n += 1
    
    return df


# Function to section the data frame according to the start and end hour of mode sm = 3

def section_time_sm3 (dfc, z1, z2, z3, z4, k):
    '''Takes time indexed data frame (pandas Data Frame), start date (int), end date (int), start hour (int), end hour (int) and time period conversion value (int), Returns sectioned data frame (pandas Data Frame)'''
    n0 = z2-z1

    a = int(((12*z3)/k))
    b = int(((12*z4)/k)+(288/k)*n0)

    df = dfc.iloc[a:b]
    
    return df

