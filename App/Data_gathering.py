# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 11:23:15 2022

@author: Joao
"""

# The function data_gathering outputs a pandas data frame containing the variables of interest of a series of consecutive dates defined by the user for 1 sonic in 1 tower
# This function uses the extract and concatenate functions to obtain the desired result

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