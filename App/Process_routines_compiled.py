# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 08:31:55 2022

@author: João
"""

# From Data gathering to Export routines compiled

import Data_gathering as dg
import save_export_function as se
import Time_period_adjust as tp
import Turbulence_parameters as tu

def process_routines (dates_def, z1, z2, z3, z4, x, y, k):
    
    '''----- PART 7 ----------'''
    
    #  Call the data_gathering module that extracts and concatenate the data in order, using time as index

    dg.data_gathering(dates_def, z1, z2, x, y)

    dfc = dg.dfc3.copy()

    '''----- PART 8 and 9 ----------'''
    # Add turbulence parameters to the 5 min period data frame.
    # If pointed, retrieves a new data frame with the time period adjusted to the desired time period (ex.: 15 min)

    if k == 1:
        tu.turbulence_5min(dfc)
        dfc = tu.df.copy()

    # If time period is different from 5 min, retrieves a data frame with the mean variables values, according to the time period selected
    # Turbulence parameters are also recalculated, simple mean of turbulence parameters is not accurate
    
    if k>1:
        
        tu.tke_k(dfc, k)
        tke_arr = tu.tke_a.copy()
        tu.ti_k(dfc, k)
        ti_arr = tu.ti_a
        tu.tih_k(dfc, k)
        tih_arr = tu.tih_a.copy()
        
        tp.period_adjust(z1, z2, dfc, k)
        dfc = tp.dfm.copy()
        
        tu.turb_append(dfc, tke_arr, ti_arr, tih_arr)
        dfc = tu.df1.copy()

    '''----- PART 10 ----------'''
    
    # If the user asked for a specific time period of the day (ex: from 11h to 17h), or a specific time for begining and/or end, this function updates the df to fulfill that order.

    if z3 != 0 or z4 != 24:
        tp.section_time(dfc, z1, z2, z3, z4, k, dates_def)
        dfc = tp.dfnew.copy()

    '''----- PART 11 ----------'''

    se.save_export(dfc, x, y, z1, z2, z3, z4, k)

    # When converting the df to a np array the file is loosing the info on the time variable (used as index in the df)
    # Possible solution is create a new df whith  the time series as a column, as well as index