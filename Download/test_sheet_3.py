# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 15:06:56 2022

@author: Joao
"""

# Test sheet  3
'''
from netCDF4 import Dataset
import numpy as np
import pandas as pd
import time
import extract_function as ex
import Turbulence_parameters as tu
import Time_period_adjust as tp
'''

# Extracting from netcdf into a pandas data frame
# Input args: fi - day code, x - tower code, y - sonic height, n - number of the day in the time series requested (if you want 2 consecutive days, in the first day n=0 and in the second day n=1)
# Output: df - dataframe containing the variables of interest for that day, tower and sonic
'''
def extract (fi, x, y, n):
    data = Dataset("{}.nc".format(fi) , 'r')
    
    # Storing the netCDF data into variables

    u = data.variables['u_{}m_{}'.format(y, x)]
    v = data.variables['v_{}m_{}'.format(y, x)]
    w = data.variables['w_{}m_{}'.format(y, x)]

    uu = data.variables['u_u__{}m_{}'.format(y, x)]
    uv = data.variables['u_v__{}m_{}'.format(y, x)]
    uw = data.variables['u_w__{}m_{}'.format(y, x)]
    vv = data.variables['v_v__{}m_{}'.format(y, x)]
    vw = data.variables['v_w__{}m_{}'.format(y, x)]
    ww = data.variables['w_w__{}m_{}'.format(y, x)]

    direc = data.variables['dir_{}m_{}'.format(y, x)]
    spd = data.variables['spd_{}m_{}'.format(y, x)]
 #   ldiag = data.variables['ldiag_{}m_{}'.format(y, x)]

    basetime = data.variables['base_time']
    reltime = data.variables['time']


    # Creating an empty pandas dataframe
    starting_time = data.variables['time'].units[14:29]+ '2:30'
    ending_time = data.variables['time'].units[14:25]+ '23:57:30'
    time_range = pd.date_range(start= starting_time, end= ending_time, periods= 288)

    global df
    
    df = pd.DataFrame(0, columns= ['basetime', 'time', 'u','v', 'w', 'vh', 'dir','uu', 'vv', 'ww', 'uv', 'uw', 'vw', 'tke'], index = time_range)

    # Create a numpy array with the size of the time variable

    dt = np.arange(0, data.variables['time'].size)

    # Filling the empty pandas data frame with the values of the variables for each time value

    i = 0
    j = 0
    j = u
    
    for time_index in dt:
        
        if i == 0:
            df.iloc[time_index] = basetime[time_index], reltime[time_index] + 86400*n, u[time_index], v[time_index], w[time_index], spd[time_index], direc[time_index], uu[time_index], vv[time_index], ww[time_index], uv[time_index], uw[time_index], vw[time_index], j[time_index]
        else:
            
            du = u-u1
            dv = v-v1
            dw = w-w1
            
            tke = (1/2)*(du*du+dv*dv+dw*dw)
            
            df.iloc[time_index] = basetime[time_index], reltime[time_index] + 86400*n, u[time_index], v[time_index], w[time_index], spd[time_index], direc[time_index], uu[time_index], vv[time_index], ww[time_index], uv[time_index], uw[time_index], vw[time_index], tke[time_index]
        
        i += 1
        u1 = u
        v1 = v
        w1 = w

        
    return df
'''

'''
fi = '20170601'
z1 = 20170601
z2 = 20170601
x = 'tnw01'
y = '10'
n = 0

ex.extract(fi, x, y, n)
dfc = ex.df
'''
'''
# dt -array from extract, if the df is from time period adjust, dt has to be adjusted too
ex.extract_2(fi, x, y)
dt = ex.dt
dts = dt.size
'''
#dt = np.arange(0, dfc.size/13, dtype=int)

'''
i = 0
for a in dt:
    
    if i == 0:
        tke = 0
        tke_arr = np.array(tke, dtype='float')
        ti = 0
        ti_arr = np.array(ti, dtype='float')
        tih = 0
        tih_arr = np.array(tih, dtype='float')

    else:
        u = dfc.iat[a,2]
        v = dfc.iat[a,3]
        w = dfc.iat[a,4]
        
        uu = dfc.iat[a,7]
        vv = dfc.iat[a,8]
        ww = dfc.iat[a,9]
        
        tke = (1/2)*(uu+vv+ww)
        ti = np.sqrt(tke*(2/3))/np.sqrt(u*u+v*v+w*w)
        tih = np.sqrt((1/3)*(uu+vv))/np.sqrt(u*u+v*v)
        
        
        temp = np.array(tke, dtype='float')
        temp2 = np.array(ti, dtype='float')
        temp3 = np.array(tih, dtype='float')
        
        tke_arr = np.append(tke_arr, [temp])
        ti_arr = np.append(ti_arr, [temp2])
        tih_arr = np.append(tih_arr, [temp3])
        
    
    i +=1
    

dfc['tke'] = tke_arr.tolist()
dfc['ti'] = ti_arr.tolist()
dfc['tih'] = tih_arr.tolist()
'''

'''
# k > 1 - tke

k = 3
i = 0
j = 0

for a in dt:
    
    u = dfc.iat[a,2]
    v = dfc.iat[a,3]
    w = dfc.iat[a,4]
    
    uu = dfc.iat[a,7]
    vv = dfc.iat[a,8]
    ww = dfc.iat[a,9]
    
    if i == 0:
        u_m1 = u*u
        uu_m2 = uu
        u_m3 = u
        
        v_m1 = v*v
        vv_m2 = vv
        v_m3 = v
        
        w_m1 = w*w
        ww_m2 = ww
        w_m3 = w
    
    if i > 0 and i < k:
        u_m1 = u_m1 + u*u
        uu_m2 = uu_m2*uu
        u_m3 = u_m3 + u
        
        v_m1 = v_m1 + v*v
        vv_m2 = vv_m2*vv
        v_m3 = v_m3 + v
        
        w_m1 = w_m1 + w*w
        ww_m2 = ww_m2*ww
        w_m3 = w_m3 + w
        
    i += 1
    
    if i == k:
        u_var = (u_m1/k)+(uu_m2/k)-(u_m3/k)*(u_m3/k)
        v_var = (v_m1/k)+(vv_m2/k)-(v_m3/k)*(v_m3/k)
        w_var = (w_m1/k)+(ww_m2/k)-(w_m3/k)*(w_m3/k)
        
        tke = (1/2)*(u_var+v_var+w_var)
        
        if j == 0:
            tke_arr = np.array(tke, dtype='float')
            
            
        if j > 0:
            
            temp = np.array(tke, dtype='float')
            
            tke_arr = np.append(tke_arr, [temp])
        j += 1
            
        i = 0


# k > 1 - ti


k = 3
i = 0
j = 0

for a in dt:
    
    u = dfc.iat[a,2]
    v = dfc.iat[a,3]
    w = dfc.iat[a,4]
    
    uu = dfc.iat[a,7]
    vv = dfc.iat[a,8]
    ww = dfc.iat[a,9]
    
    if i == 0:
        u_m1 = u*u
        uu_m2 = uu
        u_m3 = u
        
        v_m1 = v*v
        vv_m2 = vv
        v_m3 = v
        
        w_m1 = w*w
        ww_m2 = ww
        w_m3 = w
    
    if i > 0 and i < k:
        u_m1 = u_m1 + u*u
        uu_m2 = uu_m2*uu
        u_m3 = u_m3 + u
        
        v_m1 = v_m1 + v*v
        vv_m2 = vv_m2*vv
        v_m3 = v_m3 + v
        
        w_m1 = w_m1 + w*w
        ww_m2 = ww_m2*ww
        w_m3 = w_m3 + w
        
    i += 1
    
    if i == k:
        u_var = (u_m1/k)+(uu_m2/k)-(u_m3/k)*(u_m3/k)
        v_var = (v_m1/k)+(vv_m2/k)-(v_m3/k)*(v_m3/k)
        w_var = (w_m1/k)+(ww_m2/k)-(w_m3/k)*(w_m3/k)
        
        tke = (1/2)*(u_var+v_var+w_var)
        ti = np.sqrt(tke*(2/3))/(np.sqrt((u_m3/k)*(u_m3/k)+(v_m3/k)*(v_m3/k)+(w_m3/k)*(w_m3/k)))
        
        if j == 0:
            ti_arr = np.array(ti, dtype='float')
            
            
        if j > 0:
            
            temp = np.array(ti, dtype='float')
            
            ti_arr = np.append(ti_arr, [temp])
        j += 1
            
        i = 0
        


# k > 1 - tih


k = 3
i = 0
j = 0

for a in dt:
    
    u = dfc.iat[a,2]
    v = dfc.iat[a,3]
    
    
    uu = dfc.iat[a,7]
    vv = dfc.iat[a,8]
    
    
    if i == 0:
        u_m1 = u*u
        uu_m2 = uu
        u_m3 = u
        
        v_m1 = v*v
        vv_m2 = vv
        v_m3 = v
    
    if i > 0 and i < k:
        u_m1 = u_m1 + u*u
        uu_m2 = uu_m2*uu
        u_m3 = u_m3 + u
        
        v_m1 = v_m1 + v*v
        vv_m2 = vv_m2*vv
        v_m3 = v_m3 + v
        
    i += 1
    
    if i == k:
        u_var = (u_m1/k)+(uu_m2/k)-(u_m3/k)*(u_m3/k)
        v_var = (v_m1/k)+(vv_m2/k)-(v_m3/k)*(v_m3/k)
        
        tih = np.sqrt((u_var+v_var)/3)/(np.sqrt((u_m3/k)*(u_m3/k)+(v_m3/k)*(v_m3/k)))
        
        if j == 0:
            tih_arr = np.array(tih, dtype='float')
              
        if j > 0:
            
            temp = np.array(tih, dtype='float')
            
            tih_arr = np.append(tih_arr, [temp])
        j += 1
            
        i = 0
        



k = 3


tu.tke_k(dfc, k)
tke_arr = tu.tke_a.copy()


tu.ti_k(dfc, k)
ti_arr = tu.ti_a.copy()


tu.tih_k(dfc, k)
tih_arr = tu.tih_a

tp.period_adjust(z1, z2, dfc, k)
dfc = tp.dfm.copy()

tu.turb_append(dfc, tke_arr, ti_arr, tih_arr)
dfc = tu.df1.copy()
'''

# mode 1 one sonic height 1 mast

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
import Turbulence_parameters as tu
import Process_routines_compiled as pr

'''----- PART 1 ----------'''

# The array 'dates' will contain all the dates of the days with available data


# Fetching the dates arrays from the Dates_array module

dates_16 = da.d16
dates_tot = da.d

'''----- PART 2 ----------'''

#'''
# - Ask for the period time of the sample, multiples of 5 min: 5, 10, 15, 20, 30min or 1h, doesn´t accept other time periods
p0 = 0

while p0 != 1:
    period_val = input("Type one of the options for time period in min:\n5, 10, 15, 20, 30 or 60:")
    
    p = int(period_val)
    
    if p == 5 or p == 10 or p == 15 or p == 20 or p == 30 or p == 60:
        p0 = 1
        continue
    else:
        print("Invalid time period")
        continue
  

period_conv = int(period_val)/5

k = period_conv


#'''


'''----- PART 3 ----------'''

# Ask for input of which hours of the day are of interest
# z3 = start hour
# z3 = ending hour

hour_arr = np.arange(0, 25)

a7 = 0

while a7 != 1:
    z3 = input("Select start hour from 0-23:")
    z3 = int(z3)
    for c in hour_arr:
        if z3 == c and z3 != 24:
            a7 = 1
            break
    if a7 != 1:
        print("Start hour incorrect")
        print("Possible start hours:")
        print(hour_arr[0:24])
    continue

a8 = 0

while a8 != 1:
    z4 = input("Select ending hour from {}-24:".format(z3+1))
    z4 = int(z4)
    for c in hour_arr:
        if z4 == c and z4 > z3:
            a8 = 1
            break
    if a8 != 1:
        print("Ending hour incorrect")
        print("Possible ending hours:")
        print(hour_arr[z3+1:25])
    continue


'''----- PART 4 ----------'''

# define an array that contains the dates defined by the user

# Ask for input of time period

a4 = 0

while a4 != 1:
    z1 = input("Select start date with the format, YYYYMMDD:")
    z1 = int(z1)
    for c in dates_tot:
        if z1 == c:
            a4 = 1
            break
    if a4 != 1:
        print("Start date incorrect")
        print("Possible start dates:")
        print(dates_16)
        print("And every date from 16 January 2017 to 1 July 2017")
    continue

a5 = 0

while a5 != 1:
    z2 = input("Select end date with the format, YYYYMMDD:")
    z2 = int(z2)
    for c in dates_tot:
        if z2 == c:
            if z2 >= z1:
                a5 = 1
                break
            else:
                print("End date can not be a previous date from the starting date")
        
            
    if a5 != 1:
        print("Start date incorrect")
        print("Possible start dates:")
    continue

# using defined sart and end dates (z1, z2) to create an array with the defined dates
# This for cycle is showing an error (dates_def appears first for append than for creation, the fact is that the if line for the append will not ever be executed before the if line for creation). 
# Is it necessary to create an empty array first???
#dates_def = np.array(0, dtype = 'i4')

a6 = 0

for q in dates_tot:
    if a6 == 1:
        temp = np.array(q, dtype='i4')
        dates_def = np.append(dates_def, [temp])    
    if z1 == q:
        dates_def = np.array(z1, dtype = 'i4')
        a6 = 1
    if z2 == q:
        a6 = 0

# the array dates_def contains all the dates defined by the user for extracting data, every position of the array contains the date of 1 day with the format YYYYMMDD

# Write an input extra function to add dates that are not sequential and to order them in dates_def array

'''----- PART 5 ----------'''

dl.download(dates_def)

'''----- PART 6 ----------'''
   
# Create input section on wich heights or masts will be extracted
# this part needs improvement for multiple masts/heights
    

# Array with tower name code

t_name = tl.t_n
# Array with tower heights

height = tl.h

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
          
# Display which sonics heights are available for that tower


i = 0
while i < 11:
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


# x: tower code name
# y: height code name


# At this point we have the dates defined by the user, the tower and the height relative to one sonic

'''----- PARTS 7-11 ----------'''
# this function compiles every process of data gathering, calculate turbulence parameters, adjust the time of the samples, adjust the time period through the day and saving and exporting the data for 1 sonic in the designated time period.

pr.process_routines(dates_def, z1, z2, z3, z4, x, y, k)
