# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 08:31:55 2022

@author: João
"""

# Status: Reviewed

import data_gathering as dg
import save_export_function as se
import time_process as tp
import turbulence_parameters as tu

# From Data gathering to Export routines compiled

def process_routines (dates_def, z1, z2, z3, z4, x, y, k, sm):
    '''Takes an array with the selected dates (np array of int), start date (int), end date (int), start hour (int), end hour (int), tower code name (str), sonic height (int), time period conversion value (int) and sectioning mode variable (int), Returns none, extracts, processes, saves and exports data frames containing the interest variables of the Netcd Files'''     
    #  Call the extraction module and concatenate the data in order, using time as index
    '''----- PART 7 ----------'''

    # Reading the netcd file
    #fi, x and y will be given by the main input

    dfc = dg.data_gathering(dates_def, z1, z2, x, y)

    '''----- PART 8 and 9 ----------'''
    
    # Add turbulence parameters to the 5 min period data frame.

    if k == 1:
        
        dfc = tu.turbulence_5min(dfc)

    '''----- PART 9 ----------'''
    # If time period is different from 5 min, retrieves a data frame with the mean variables values, according to the time period selected
    # Turbulence parameters are also recalculated, simple mean of turbulence parameters is not accurate
        
    if k>1:
        
        tke_arr = tu.tke_k(dfc, k)
        ti_arr = tu.ti_k(dfc, k)
        tih_arr = tu.tih_k(dfc, k)
        
        dfc = tp.period_adjust(z1, z2, dfc, k)

        dfc = tu.turb_append(dfc, tke_arr, ti_arr, tih_arr)

    '''----- PART 10 ----------'''
    # If the user asked for a specific time period of the day (ex: from 11h to 17h) this function updates the df to fulfill that order.

    if sm == 2:
        
        dfc = tp.section_time_sm2(dfc, z1, z2, z3, z4, k, dates_def)
        
    if sm == 3:
        
        dfc = tp.section_time_sm3(dfc, z1, z2, z3, z4, k)

    '''----- PART 11 ----------'''

    se.save_export(dfc, x, y, z1, z2, z3, z4, k)

    # When converting the df to a np array the file is loosing the info on the time variable (used as index in the df)
    # Possible solution is create a new df whith  the time series as a column, as well as index
    

