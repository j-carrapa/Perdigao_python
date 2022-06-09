# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 20:13:01 2022

@author: Joao
"""

# Test sheet
'''
from netCDF4 import Dataset
import numpy as np
import pandas as pd
import Tower_location as tl
import requests
import Dates_array as da
import Data_gathering as dg
import Download as dl
import save_export_function as se
import Time_period_adjust as tp
import extract_function as ex
import Concatenate_DF as co


z1 = 20170601
z2 = 20170603
dates_def = [20170601, 20170602, 20170603]
k = 4
z3 = 11
z4 = 17

x = 'tnw01'
y = '10'



dg.data_gathering(dates_def, z1, z2, x, y)
dfc = dg.dfc3.copy()


tp.period_adjust(z1, z2, dfc, k)
dfc = tp.dfm.copy()

tp.section_time(dfc, z1, z2, z3, z4, k, dates_def)
dfc = tp.dfnew.copy()
'''
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
i = 1

if i == 1:
    import Input_Download_second_try
    
else:
    print("hi")
    

'''



