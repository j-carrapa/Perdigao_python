# -*- coding: utf-8 -*-
"""
Created on Fri May 27 15:29:56 2022

@author: Joao
"""

# Time period adjust

'''----- PART 4 ----------'''
# - Ask for the period time of the sample, multiples of 5 min: 5, 10, 15, 20, 30min or 1h

import pandas as pd
import numpy as np
import extract_function as ex
import Concatenate_DF as co

'''

period_val = input("Type one of the options for time period in min:\n5, 10, 15, 20, 30 or 60:")

period_conv = int(period_val)/5

k = period_conv

#'''
'''
#dfc
z1 = 20170601
z2 = 20170603
n = 3
k=2
#'''

'''
n = z2 - z1 +1
t = (288*n)/k

ex.extract_start_time(z1, k)
starting_time = ex.start

ex.extract_end_time(z2, k)
ending_time = ex.end

time_range = pd.date_range(start= starting_time, end= ending_time, periods= t)
dfmean = pd.DataFrame(0, columns= ['basetime', 'time', 'u','v', 'w', 'vh', 'dir','uu', 'vv', 'ww', 'uv', 'uw', 'vw'], index = time_range) 

dt = np.arange(0, 288*n)
#'''

#'''

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




def section_time (dfc, z1, z2, z3, z4, k, dates_def):
    
    n = z2 - z1 +1
    h = z4 - z3
    le = ((12*h)/k)
    n0 = 0
    
    dt = np.arange(0, le)

    for a in dates_def:
        
        ex.extract_start_time(a, k, z3)
        starting_time = ex.start

        ex.extract_end_time(a, k, z4)
        ending_time = ex.end

        time_range = pd.date_range(start= starting_time, end= ending_time, periods= le)
        dfn = pd.DataFrame(0, columns= ['basetime', 'time', 'u','v', 'w', 'vh', 'dir','uu', 'vv', 'ww', 'uv', 'uw', 'vw'], index = time_range)

        
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
            
            
            dfn.iloc[i] = b, t, u, v, w, vh, di, uu, vv, ww, uv, uw, vw
        
        
        if n0 == 0:
            df = dfn.copy()
        else:
            co.concatenate(df, dfn)
            df = co.dfc1.copy()
        
        n0 += 1
        
    
    global dfnew
    dfnew = df.copy()
    return dfnew


#'''        

'''
n = z2 - z1 +1
h = z4 - z3
le = ((12*h)/k)
n0 = 0


dt = np.arange(0, le)

for a in dates_def:
    
    ex.extract_start_time(a, k, z3)
    starting_time = ex.start

    ex.extract_end_time(a, k, z4)
    ending_time = ex.end

    time_range = pd.date_range(start= starting_time, end= ending_time, periods= le)
    dfn = pd.DataFrame(0, columns= ['basetime', 'time', 'u','v', 'w', 'vh', 'dir','uu', 'vv', 'ww', 'uv', 'uw', 'vw'], index = time_range)

    
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
        
        
        dfn.iloc[i] = b, t, u, v, w, vh, di, uu, vv, ww, uv, uw, vw
    
    
    if n0 == 0:
        df = dfn.copy()
    else:
        co.concatenate(df, dfn)
        df = co.dfc1.copy()
    
    n0 += 1
    
#'''
       
        
        
        
'''    
    time_range = pd.date_range(start= starting_time, end= ending_time, periods= t)
    dfmean = pd.DataFrame(0, columns= ['basetime', 'time', 'u','v', 'w', 'vh', 'dir','uu', 'vv', 'ww', 'uv', 'uw', 'vw'], index = time_range) 

'''


'''

# Creating an empty pandas dataframe
starting_time = data.variables['time'].units[14:29]+ '2:30'
ending_time = data.variables['time'].units[14:25]+ '23:57:30'
time_range = pd.date_range(start= starting_time, end= ending_time, periods= 288)

df = pd.DataFrame(0, columns= ['basetime', 'time', 'u','v', 'w', 'vh', 'dir','uu', 'vv', 'ww', 'uv', 'uw', 'vw'], index = time_range)
df1 = pd.DataFrame(0, columns= ['basetime', 'time', 'u','v', 'w', 'vh', 'dir','uu', 'vv', 'ww', 'uv', 'uw', 'vw'], index = time_range)
df2 = pd.DataFrame(0, columns= ['basetime', 'time', 'u','v', 'w', 'vh', 'dir','uu', 'vv', 'ww', 'uv', 'uw', 'vw'], index = time_range)
dfmean = pd.DataFrame(0, columns= ['basetime', 'time', 'u','v', 'w', 'vh', 'dir','uu', 'vv', 'ww', 'uv', 'uw', 'vw'], index = time_range)




# Create a numpy array with the size of the time variable

dt = np.arange(0, data.variables['time'].size)





if period_conv == 2:
    p = 1
    for time_index in dt:
        df.iloc[time_index] = basetime[time_index], reltime[time_index] + 86400*n, u[time_index], v[time_index], w[time_index], spd[time_index], direc[time_index], uu[time_index], vv[time_index], ww[time_index], uv[time_index], uw[time_index], vw[time_index]
        if p//2 == 1:
            df1.iloc[time_index] = basetime[time_index], reltime[time_index] + 86400*n, u[time_index], v[time_index], w[time_index], spd[time_index], direc[time_index], uu[time_index], vv[time_index], ww[time_index], uv[time_index], uw[time_index], vw[time_index]
            p += 1
        if p//2 == 0:
            df2.iloc[time_index] = basetime[time_index], reltime[time_index] + 86400*n, u[time_index], v[time_index], w[time_index], spd[time_index], direc[time_index], uu[time_index], vv[time_index], ww[time_index], uv[time_index], uw[time_index], vw[time_index]
            p += 1
            dfmean.iloc[time_index] = df1[time_index,0], (df1[time_index,1] + df1[time_index,1])/2 + 86400*n#, u[time_index], v[time_index], w[time_index], spd[time_index], direc[time_index], uu[time_index], vv[time_index], ww[time_index], uv[time_index], uw[time_index], vw[time_index]
            




if period_conv == 2:
    while i < 288:
        dfmean
        
#'''