# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 10:35:30 2022

@author: Joao
"""
import pandas as pd

# Status: Reviewed

# Concatenate 2 data frames of 1 sonic

def concatenate (df1, df2):
    '''Takes two data frames (pandas DataFrame), Returns concatenated data frame built from the args (pandas DataFrame)'''
    frames = [df1]
    frames.append(df2)
    result = pd.concat(frames)
    
    return result

