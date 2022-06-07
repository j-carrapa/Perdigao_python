# -*- coding: utf-8 -*-
"""
Created on Tue May 17 15:21:41 2022

@author: Joao
"""


# Input / Download module first try


from netCDF4 import Dataset
import numpy as np
import pandas as pd
import Tower_location as tl
import requests
import Dates_array as da

''' 18 May
Updates log
change the heights list from the XXXm format to the XXX format
Define print statements of what processes are occuring (ex: Downloading...)
There was an error when the start date was the same of the end date. It is now solved
Updated the time stamp in the second column of the data frame, to assure that the time variable is continuous when passing from one day to another



20 may

Changed some variable names to avoid misunderstandings
Changed the saving and exporting code to get the files name with the following format: "[sonic height]_[tower code name]_[starting date]_[end date]"
The app can now extract and export multiple sonics
'''

'''
25 may
Create separete modules for some routines:
    Dates
    

'''


'''----- PART 1 ----------'''

# The array 'dates' will contain all the dates of the days with available data


# Fetching the dates arrays from the Dates_array module

dates_16 = da.d16
dates_tot = da.d

'''----- PART 2 ----------'''
# - Ask for the period time of the sample, multiples of 5 min: 5, 10, 15, 20, 30min or 1h

period_val = input("Type one of the options for time period in min:\n5, 10, 15, 20, 30 or 60:")

period_conv = int(period_val)/5



'''----- PART 3 ----------'''

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


'''----- PART 4 ----------'''


'''
# - Download the files defined by the user

print("Downloading...")

# Just to explain user what is happening

for date in dates_def:
    url = 'http://windsptds.fe.up.pt/thredds/fileServer/flux/NCAR-EOL%20Quality%20Controlled%205-minute%20ISFS%20surface%20flux%20data,%20geographic%20coordinate,%20tilt%20corrected/isfs_qc_tiltcor_'+ str(date) +'.nc'
    r = requests.get(url)
    open(str(date)+'.nc','wb').write(r.content)

'''    
 
'''----- PART 5 ----------'''
   
# Create input section on wich heights or masts will be extracted
# this part needs improvement for multiple masts/heights
    

# Array with tower name code

t_name = tl.t_n
# Array with tower heights

height = tl.h

# Ask for input of tower code name, the code will not continue until a valid code name is given

g1 = 0

while g1 != 1:
    
    g2 = 0
    
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


    '''----- PART 6 ----------'''

    print("Gathering data and exporting")

    # Just to explain user what is happening

    #  Call the extraction module and concatenate the data in order, using time as index

    # don't know how to call it from a module, will put everything in this file

    # Reading the netcd file
    #fi, x and y will be given by the main input

    m = 0
    n = 0
    fi = str(z1)
    data = Dataset("{}.nc".format(fi) , 'r')
    # Creating an empty pandas dataframe
    starting_time = data.variables['time'].units[14:29]+ '2:30'
    ending_time = data.variables['time'].units[14:25]+ '23:57:30'
    time_range = pd.date_range(start= starting_time, end= ending_time, periods= 288)
    dfc = pd.DataFrame(0, columns= ['basetime', 'time', 'u','v', 'w', 'vh', 'dir','uu', 'vv', 'ww', 'uv', 'uw', 'vw'], index = time_range)

    try:
        for z in dates_def:
            fi = str(z)
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
            ldiag = data.variables['ldiag_{}m_{}'.format(y, x)]

            basetime = data.variables['base_time']
            reltime = data.variables['time']


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

            # Filling the empty pandas data frame with the values of the variables for each time value
            
            for time_index in dt:
                df.iloc[time_index] = basetime[time_index], reltime[time_index] + 86400*n, u[time_index], v[time_index], w[time_index], spd[time_index], direc[time_index], uu[time_index], vv[time_index], ww[time_index], uv[time_index], uw[time_index], vw[time_index]
            '''
            if period_conv == 2:
                p = 1
                for time_index in dt:
                    df.iloc[time_index] = basetime[time_index], reltime[time_index] + 86400*n, u[time_index], v[time_index], w[time_index], spd[time_index], direc[time_index], uu[time_index], vv[time_index], ww[time_index], uv[time_index], uw[time_index], vw[time_index]
                    if p//2 == 0:
                        df1.iloc[time_index] = basetime[time_index], reltime[time_index] + 86400*n, u[time_index], v[time_index], w[time_index], spd[time_index], direc[time_index], uu[time_index], vv[time_index], ww[time_index], uv[time_index], uw[time_index], vw[time_index]
                        p += 1
                    if p//2 == 1:
                        df2.iloc[time_index] = basetime[time_index], reltime[time_index] + 86400*n, u[time_index], v[time_index], w[time_index], spd[time_index], direc[time_index], uu[time_index], vv[time_index], ww[time_index], uv[time_index], uw[time_index], vw[time_index]
                        p = 1
                        dfmean.iloc[time_index] = df1[time_index,0], (df1[time_index,1] + df1[time_index,1])/2 + 86400*n#, u[time_index], v[time_index], w[time_index], spd[time_index], direc[time_index], uu[time_index], vv[time_index], ww[time_index], uv[time_index], uw[time_index], vw[time_index]
            '''        

        
            n = n + 1

        
        # concatenate in one single dataframe all of the required info

            if m == 1:
                frames.append(df)
                result = pd.concat(frames)
                dfc = result.copy()
                frames = [dfc]
                
            if m == 0:
                dfc = df.copy()
                frames = [dfc]
                m = 1
        
    except:
        fi = str(z1)
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
        ldiag = data.variables['ldiag_{}m_{}'.format(y, x)]

        basetime = data.variables['base_time']
        reltime = data.variables['time']


        # Creating an empty pandas dataframe
        starting_time = data.variables['time'].units[14:29]+ '2:30'
        ending_time = data.variables['time'].units[14:25]+ '23:57:30'
        time_range = pd.date_range(start= starting_time, end= ending_time, periods= 288)

        df = pd.DataFrame(0, columns= ['basetime', 'time', 'u','v', 'w', 'vh', 'dir','uu', 'vv', 'ww', 'uv', 'uw', 'vw'], index = time_range)

        # Create a numpy array with the size of the time variable

        dt = np.arange(0, data.variables['time'].size)

        # Filling the empty pandas data frame with the values of the variables for each time value

        for time_index in dt:
            df.iloc[time_index] = basetime[time_index], reltime[time_index], u[time_index], v[time_index], w[time_index], spd[time_index], direc[time_index], uu[time_index], vv[time_index], ww[time_index], uv[time_index], uw[time_index], vw[time_index]

        dfc = df.copy()

    finally:
        print("File exported")
        
            
    '''----- PART 7 ----------'''

          
    # Saving the Data frame into a CSV and a Excel file


    if z1 == z2:
        dfc.to_csv('{}m_{}_{}.csv'.format(y,x,z1))

        dfc.to_excel('{}m_{}_{}.xls'.format(y,x,z1))

        df_np = dfc.to_numpy()
        np.savetxt("{}m_{}_{}.txt".format(y,x,z1), df_np, fmt = "%.4f")

    else:
        dfc.to_csv('{}m_{}_{}_{}.csv'.format(y,x,z1,z2))

        dfc.to_excel('{}m_{}_{}_{}.xls'.format(y,x,z1,z2))

        df_np = dfc.to_numpy()
        np.savetxt("{}m_{}_{}_{}.txt".format(y,x,z1,z2), df_np, fmt = "%.4f")


        
    # When converting the df to a np array the file is loosing the info on the time variable (used as index in the df)
    # Possible solution is create a new df whith  the time series as a column, as well as index
    
    while g2 != 1:
        g_ans = input("End of data gathering?\n[yes/no]:")
        
        if g_ans == 'no':
            g2 = 1
            continue
        if g_ans == 'yes':
            g2 = 1
            g1 = 1
            continue
        else:
            print("Type correct answer.\n[yes/no]:")
            continue
    continue







'''
Variables

s = string for helping build dates array
i = iterable for helping build dates array
j = iterable for helping build dates array
z1 = starting date from input
z2 = ending date from input
x = tower name code from input
y = sonic height code from input
a,...,a7 = iterables
m,n = iterables



'''