# -*- coding: utf-8 -*-
"""
Created on Fri May 27 15:29:56 2022

@author: Joao
"""

# Time period adjust

import pandas as pd
import numpy as np
import extract_function as ex
import Concatenate_DF as co

# - Ask for the period time of the sample, multiples of 5 min: 5, 10, 15, 20, 30min or 1h

# Function to retrieve a new data frame with the desired time period, and new mean values for all the variables

def period_adjust (z1, z2, dfc, k):
    
    n = z2 - z1 +1
    t = (288*n)/k
    h = 0
    
    ex.extract_start_time(z1, k, h)
    starting_time = ex.start
    
    ex.extract_end_time(z2, k, h)
    ending_time = ex.end
    
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
        
    global dfm
    dfm = dfmean.copy()  
    return dfm

# Function to slice the desired periods of the day (defined by start and end hours)

def section_time (dfc, z1, z2, z3, z4, k, dates_def):
    
    n = z2 - z1 +1
    h = z4 - z3
    le = ((12*h)/k)
    n0 = 0
    
    dt = np.arange(0, le)
    
    if z1 == z2:
        ex.extract_start_time(z1, k, z3)
        starting_time = ex.start

        ex.extract_end_time(z1, k, z4)
        ending_time = ex.end

        time_range = pd.date_range(start= starting_time, end= ending_time, periods= le)
        dfn = pd.DataFrame(0, columns= ['basetime', 'time', 'u','v', 'w', 'vh', 'dir','uu', 'vv', 'ww', 'uv', 'uw', 'vw', 'tke', 'ti', 'tih'], index = time_range)
        
        for i in dt:
            j = i + (12*z3)/k
            j = int(j)
            i = int(i)

            b = dfc.iat[j,0]
            t = dfc.iat[j,1]
            u = dfc.iat[j, 2]
            v = dfc.iat[j, 3]
            w = dfc.iat[j, 4]
            vh = dfc.iat[j, 4]
            di = dfc.iat[j, 6]
            uu = dfc.iat[j, 7]
            vv = dfc.iat[j, 8]
            ww = dfc.iat[j, 9]
            uv = dfc.iat[j, 10]
            uw = dfc.iat[j, 11]
            vw = dfc.iat[j, 12]
            tke = dfc.iat[j, 13]
            ti = dfc.iat[j, 14]
            tih = dfc.iat[j, 15]            
            
            dfn.iloc[i] = b, t, u, v, w, vh, di, uu, vv, ww, uv, uw, vw, tke, ti, tih
            
            df = dfn.copy()
        
    else:
        for a in dates_def:
            
            ex.extract_start_time(a, k, z3)
            starting_time = ex.start

            ex.extract_end_time(a, k, z4)
            ending_time = ex.end

            time_range = pd.date_range(start= starting_time, end= ending_time, periods= le)
            dfn = pd.DataFrame(0, columns= ['basetime', 'time', 'u','v', 'w', 'vh', 'dir','uu', 'vv', 'ww', 'uv', 'uw', 'vw', 'tke', 'ti', 'tih'], index = time_range)

            for i in dt:
                j = i + (12*z3)/k + (288/k)*n0
                j = int(j)
                i = int(i)
                
                b = dfc.iat[j,0]
                t = dfc.iat[j,1]
                u = dfc.iat[j, 2]
                v = dfc.iat[j, 3]
                w = dfc.iat[j, 4]
                vh = dfc.iat[j, 4]
                di = dfc.iat[j, 6]
                uu = dfc.iat[j, 7]
                vv = dfc.iat[j, 8]
                ww = dfc.iat[j, 9]
                uv = dfc.iat[j, 10]
                uw = dfc.iat[j, 11]
                vw = dfc.iat[j, 12]
                tke = dfc.iat[j, 13]
                ti = dfc.iat[j, 14]
                tih = dfc.iat[j, 15]            
                
                dfn.iloc[i] = b, t, u, v, w, vh, di, uu, vv, ww, uv, uw, vw, tke, ti, tih
            
            if n0 == 0:
                df = dfn.copy()
            else:
                co.concatenate(df, dfn)
                df = co.dfc1.copy()
            
            n0 += 1
    
    global dfnew
    dfnew = df.copy()
    return dfnew