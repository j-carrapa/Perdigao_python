# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 16:03:23 2022

@author: Joao
"""

# Status: Reviewed

# To do: update save_export to allow to choose the file format of saving and exporting, ...

# Save and export module

import numpy as np

def save_export (dfc, x, y, z1, z2, z3, z4, k):
    '''Takes time indexed data frame (pandas Data Frame), tower code name (str), sonic height (int), start date (int), end date (int), start hour (int), end hour (int) and time period conversion value (int), Returns none, saves and exports files'''     
    p = k*5
    
    if z1 == z2:
        if z3 == 0 and z4 == 24:
            dfc.to_csv('{}m_{}_{}_P-{}min.csv'.format(y,x,z1,p))

            dfc.to_excel('{}m_{}_{}_P-{}min.xls'.format(y,x,z1,p))

            df_np = dfc.to_numpy()
            np.savetxt("{}m_{}_{}_P-{}min.txt".format(y,x,z1,p), df_np, fmt = "%.4f")
        else:
            dfc.to_csv('{}m_{}_{}_{}-{}h_P-{}min.csv'.format(y,x,z1,z3,z4,p))

            dfc.to_excel('{}m_{}_{}_{}-{}h_P-{}min.xls'.format(y,x,z1,z3,z4,p))

            df_np = dfc.to_numpy()
            np.savetxt("{}m_{}_{}_{}-{}h_P-{}min.txt".format(y,x,z1,z3,z4,p), df_np, fmt = "%.4f")
            
        
    else:
        if z3 == 0 and z4 == 24:
            dfc.to_csv('{}m_{}_{}_{}_P-{}min.csv'.format(y,x,z1,z2,p))

            dfc.to_excel('{}m_{}_{}_{}_P-{}min.xls'.format(y,x,z1,z2,p))

            df_np = dfc.to_numpy()
            np.savetxt("{}m_{}_{}_{}_P-{}min.txt".format(y,x,z1,z2,p), df_np, fmt = "%.4f")
        else:
            dfc.to_csv('{}m_{}_{}_{}_{}-{}h_P-{}min.csv'.format(y,x,z1,z2,z3,z4,p))

            dfc.to_excel('{}m_{}_{}_{}_{}-{}h_P-{}min.xls'.format(y,x,z1,z2,z3,z4,p))

            df_np = dfc.to_numpy()
            np.savetxt("{}m_{}_{}_{}_{}-{}h_P-{}min.txt".format(y,x,z1,z2,z3,z4,p), df_np, fmt = "%.4f")

