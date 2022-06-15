# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 10:35:30 2022

@author: Joao
"""
import pandas as pd
# Concatenate 2 data frames of 1 sonic

def concatenate (df1, df2):
    
    global dfc1
    
    frames = [df1]
    frames.append(df2)
    result = pd.concat(frames)
    dfc1 = result.copy()
    
            
    return dfc1


'''
def concatenate (df, dfc1, dates_def, m):
    
    global dfc2
    for z in dates_def:
        if m == 1:
            frames.append(df)
            result = pd.concat(frames)
            dfc1 = result.copy()
            frames = [dfc1]
            
        if m == 0:
            dfc1 = df.copy()
            frames = [dfc1]
            m = 1
    dfc2 = dfc1.copy()
    return dfc2
'''