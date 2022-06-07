# -*- coding: utf-8 -*-
"""
Created on Fri May 27 11:21:05 2022

@author: Joao
"""


# Mode 2 - All sonics in one mast

#How to import variables from the Input_Download_first_try???
# import x (tower code name)


import Tower_location as tl
import numpy as np
from netCDF4 import Dataset
#from Input_Download_first_try import x, z1, z2


# Define variables imported

#x2 = x              # selected tower
x = 'tnw01'
t = tl.t_n          # Array with tower names
h = tl.h            # Array with sonics heights

#sd = 

j = np.where(t == x)

j = j[0]

#print(tl.m[:,j])
i = 0
for b in h:

    if tl.m[i,j] == 1:
        print('e')
        y = b           #height for each loop
        
        # All the code for extracting and exporting?
    i += 1

#a = np.zeros((12))
#a = tl.m[0:12,int(j)]



#arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

#print(arr[0:2, 1:4])


# Create an array with the available heights





'''

a3 = 0
while a3 != 1:
    a2 = 0
    while a2 != 1:
        i = 0
        y = input("Tower height:")
        for b in height:
            if y == b:
                a2 = 1
                break
            i = i + 1
        
        if a2 != 1:
            print("Select an appropriate height")
            
        continue 
    if tl.m[i,j] == 1:
        a3 = 1
    else:
        print("This tower doesn't have sonics for {} heihgt, select an appropriate height".format(y))
    continue



'''

