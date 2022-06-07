# -*- coding: utf-8 -*-
"""
Created on Wed May 25 09:03:00 2022

@author: Joao
"""

import numpy as np


# File containing arrays with the dates used for downloading and extracting data of the netCD fiiles

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

# Variables to be used in other modules

d16 = dates_16
d = dates_tot
