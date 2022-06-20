# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 10:35:30 2022

@author: Joao
"""
import pandas as pd

# Concatenate 2 data frames of 1 sonic into 1 data frame

def concatenate (df1, df2):
    
    global dfc1
    
    frames = [df1]
    frames.append(df2)
    result = pd.concat(frames)
    dfc1 = result.copy()
    
    return dfc1