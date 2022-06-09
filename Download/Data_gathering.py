# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 11:23:15 2022

@author: Joao
"""

# Data frame extract and concatenate module
# The function data_gathering outputs a pandas data frame containing the variables of interest of a series of consecutive dates defined by the user for 1 sonic in 1 tower





import extract_function as ex
import Concatenate_DF as co
import Time_period_adjust as tp
import numpy as np


def data_gathering (dates_def, z1, z2, x, y):
    
    n = 0
    m = 0
    
    global dfc3
    
    if z1 == z2:
        ex.extract(z1, x, y, n)
        dfc3 = ex.df.copy()
    
    else:
        for z in dates_def:
            if m == 1:
                ex.extract(z, x, y, n)
                co.concatenate(dfc2, ex.df)
                dfc2 = co.dfc1.copy()
                dfc3 = co.dfc1.copy()
                
            if m == 0:
                ex.extract(z, x, y, n)
                dfc2 = ex.df.copy()
                m = 1
            n +=1
    return dfc3
    



'''
# try the function for z1 = z2
z1 = 20170601
z2 = 20170603
dates_def = [20170601, 20170602, 20170603]
k = 4
z3 = 11
z4 = 17

x = 'tnw01'
y = '10'

data_gathering(dates_def, z1, z2, x, y)

dfc = dfc3.copy()

tp.period_adjust(z1, z2, dfc, k)
dfc1 = tp.dfm.copy()

tp.section_time(dfc1, z1, z2, z3, z4, k)
dfc2 = tp.dfnew.copy()

#'''
'''
h = z4 - z3
le = (12*h)/k
dt = np.arange(0, le)
'''
