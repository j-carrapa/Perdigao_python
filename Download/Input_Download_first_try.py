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

''' 18 May
Updates log
change the heights list from the XXXm format to the XXX format
Define print statements of what processes are occuring (ex: Downloading...)
There was an error when the start date was the same of the end date. It is now solved
Updated the time stamp in the second column of the data frame, to assure that the time variable is continuous when passing from one day to another




'''



'''----- PARTE 1 ----------'''

# The array 'dates' will contain all the dates of the days with available data

dates = np.array([20161129, 20161201, 20161202, 20161205], dtype='i4')


i = 7


while i<10:
    s = '2016120'+ str(i)
    temp = np.array(s, dtype='i4')
    dates = np.append(dates, [temp])
    i = i+1

dates = np.append(dates, [20161210])

# Array with the dates of the days with available data for the months of November and Dezember of 2016

dates_16 = dates

# Filling the 'dates' array with the remaining dates of the year 2017

j = 1
i = 16

# Array with the dates of the days with available data for the months from January until July of 2017

# 1- January, 3- March, 5- May months with 31 days
# 2- February - 29 days
# 4- April, 6- June

while j<7:
    if j == 1 or j == 3 or j == 5:
        while i < 10:
            s = '20170' + str(j)+'0'+ str(i)
            temp = np.array(s, dtype='i4')
            dates = np.append(dates, [temp])
            i = i+1
        else:
            while i <32:
                s = '20170' + str(j)+ str(i)
                temp = np.array(s, dtype='i4')
                dates = np.append(dates, [temp])
                i = i+1
            else:
                i=1
        
    if j == 2:
        while i <10:
            s = '20170' + str(j)+ '0' + str(i)
            temp = np.array(s, dtype='i4')
            dates = np.append(dates, [temp])
            i = i+1
        else:
            while i <29:
                s = '20170' + str(j)+ str(i)
                temp = np.array(s, dtype='i4')
                dates = np.append(dates, [temp])
                i = i+1
            else:
                i = 1
    if j == 4 or j == 6:
        while i <10:
            s = '20170' + str(j)+ '0' + str(i)
            temp = np.array(s, dtype='i4')
            dates = np.append(dates, [temp])
            i = i+1
        else:
            while i < 31:
                s = '20170' + str(j)+ str(i)
                temp = np.array(s, dtype='i4')
                dates = np.append(dates, [temp])
                i = i+1
            else:
                i = 1
    j = j+1

else:
    dates = np.append(dates, [20170701])


dates_tot = dates


'''----- PART 2 ----------'''

# define an array that contains the dates defined by the user



# Ask for input of time period

a4 = 0

while a4 != 1:
    z = input("Select start date with the format, YYYYMMDD:")
    z = int(z)
    for c in dates_tot:
        if z == c:
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
    w = input("Select end date with the format, YYYYMMDD:")
    w = int(w)
    for c in dates_tot:
        if w == c:
            if w >= z:
                a5 = 1
                break
            else:
                print("End date can not be a previous date from the starting date")
        
            
    if a5 != 1:
        print("Start date incorrect")
        print("Possible start dates:")
    continue

# using defined sart and end dates (z, w) to create an array with the defined dates
# This for cycle is showing an error (dates_def appears first for append than for creation, the fact is that the if line for the append will not ever be executed before the if line for creation). 
# Is it necessary to create an empty array first???
#dates_def = np.array(0, dtype = 'i4')

a6 = 0

for q in dates_tot:
    if a6 == 1:
        temp = np.array(q, dtype='i4')
        dates_def = np.append(dates_def, [temp])    
    if z == q:
        dates_def = np.array(z, dtype = 'i4')
        a6 = 1
    if w == q:
        a6 = 0

# the array dates_def contains all the dates defined by the user for extracting data, every position of the array contains the date of 1 day with the format YYYYMMDD

# Write an input extra function to add dates that are not sequential and to order them in dates_def array


'''----- PART 3 ----------'''

'''
# - Download the files defined by the user

print("Downloading...")

# Just to explain user what is happening

for date in dates_def:
    url = 'http://windsptds.fe.up.pt/thredds/fileServer/flux/NCAR-EOL%20Quality%20Controlled%205-minute%20ISFS%20surface%20flux%20data,%20geographic%20coordinate,%20tilt%20corrected/isfs_qc_tiltcor_'+ str(date) +'.nc'
    r = requests.get(url)
    open(str(date)+'.nc','wb').write(r.content)

'''    
 
'''----- PART 4 ----------'''
   
# Create input section on wich heights or masts will be extracted
# this part needs improvement for multiple masts/heights
    

# Array with tower name code

t_name = np.array(["tnw01", "tnw02", "tnw03", "tnw04", "tnw05", "tnw06", "tnw07", "tnw08", "tnw09", "tnw10", "tnw11", "tnw12", "tnw13", "tnw14", "tnw15", "tnw16", "tse01", "tse02", "tse04", "tse05", "tse06", "tse07", "tse08", "tse09", "tse10", "tse11", "tse12", "tse13", "rsw01", "rsw02", "rsw03", "rsw04", "rsw05", "rsw06", "rsw07", "rsw08", "rne01", "rne02", "rne03", "rne04", "rne06", "rne07", "v01", "v03", "v04", "v05", "v06", "v07", "Extreme_SW", "Extreme_NE"])

# Array with tower heights

height = np.array(["2", "4", "6", "8", "10", "20", "30", "40", "60", "80", "100"])


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


# x: tower code name
# y: height code name


# At this point we have the dates defined by the user, the tower and the height relative to one sonic


'''----- PART 5 ----------'''

print("Gathering data and exporting")

# Just to explain user what is happening

#  Call the extraction module and concatenate the data in order, using time as index

# don't know how to call it from a module, will put everything in this file

# Reading the netcd file
#fi, x and y will be given by the main input

m = 0
n = 0
fi = str(z)
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

        # Create a numpy array with the size of the time variable

        dt = np.arange(0, data.variables['time'].size)

        # Filling the empty pandas data frame with the values of the variables for each time value

        for time_index in dt:
            df.iloc[time_index] = basetime[time_index], reltime[time_index] + 86400*n, u[time_index], v[time_index], w[time_index], spd[time_index], direc[time_index], uu[time_index], vv[time_index], ww[time_index], uv[time_index], uw[time_index], vw[time_index]
            
        n = n + 1

    '''
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
    '''
except:
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

    # Create a numpy array with the size of the time variable

    dt = np.arange(0, data.variables['time'].size)

    # Filling the empty pandas data frame with the values of the variables for each time value

    for time_index in dt:
        df.iloc[time_index] = basetime[time_index], reltime[time_index], u[time_index], v[time_index], w[time_index], spd[time_index], direc[time_index], uu[time_index], vv[time_index], ww[time_index], uv[time_index], uw[time_index], vw[time_index]

    dfc = df.copy()

finally:
    print("File exported")
    
        
'''----- PART 6 ----------'''
'''
      
# Saving the Data frame into a CSV and a Excel file

dfc.to_csv('file1.csv')

dfc.to_excel('file1.xls')

# When converting the df to a np array the file is loosing the info on the time variable (used as index in the df)
# Possible solution is create a new df whith  the time series as a column, as well as index


df_np = dfc.to_numpy()
np.savetxt("file1.txt", df_np, fmt = "%.4f")
    
'''
