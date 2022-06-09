# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 15:20:19 2022

@author: Joao
"""

# Test sheet 2

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




height = tl.h
t_name = tl.t_n

# Ask for input of tower code name, the code will not continue until a valid code name is given


    
a1 = 0
a2 = 0
a3 = 0
a4 = 0

while a3 != 1:
    while a1 != 1:
        j = 0
        x = input("Tower name code:")
        for a in t_name:
            
            if x == a:
                
                if a2 == 1:
                    x_arr = np.append(x_arr, x)
                    j_arr = np.append(j_arr, j)
                    
                if a2 == 0:
                    x_arr = np.array(x)
                    j_arr = np.array(j)
                    a2 = 1
                
                a4 = 0   
                a1 = 1
                break
            j = j + 1
        if a1 != 1:
            print("Code name incorrect")
            
        continue
    
    while a4 != 1:
        
        t_ans = input("Get other tower?\n[yes/no]:")
        
        if t_ans == 'yes':
            a4 = 1
            a1 = 0
            break
            
        if t_ans == 'no':
            a4 = 1
            a3 = 1
            break
        
        if a4 == 0:
            print("Type correct answer")
            
        
    continue
    

for x in x_arr:
    
    i = 0
    print(x)
    print(j_arr[i])
    
    #j = j_arr[i]
    #print(j)
    i += 1
    


'''
x = 'tnw01'
x1 = 'tnw02'
x2 = 'tnw03'
x3 = 'tnw04'
x4 = 'tnw05'


x_arr = np.array(x)
x_arr = np.append(x_arr, x1)
'''
