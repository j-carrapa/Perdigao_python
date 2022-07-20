# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 11:23:15 2022

@author: Joao
"""
# Status: Reviewed

# Data frame extract and concatenate module

import extract_function as ex
import concatenate_df as co

# Data gathering Function
# The function data_gathering outputs a pandas data frame containing the variables of interest of a series of consecutive dates defined by the user for 1 sonic in 1 tower

def data_gathering (dates_def, z1, z2, x, y):
    '''Takes dates to retrieve data (np array of int), start date (int), end date (int), tower code name (str), sonic height(int), Returns data frame with sonic data for that period (pandas DataFrame)'''
    n = 0
    m = 0
    
    if z1 == z2:
        
        dfc = ex.extract(z1, x, y, n)
    
    else:
        for z in dates_def:
            if m == 1:
                df = ex.extract(z, x, y, n)
                dfc = co.concatenate(dfc, df)
                
            if m == 0:
                
                dfc = ex.extract(z, x, y, n)
                m = 1
            n +=1
    return dfc
    
