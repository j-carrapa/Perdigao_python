# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 14:24:48 2022

@author: João
"""

# NumPy 3


# The Difference Between Copy and View
'''The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.

The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.

The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.'''

#COPY:
    
'''Example
Make a copy, change the original array, and display both arrays:'''

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)
'''The copy SHOULD NOT be affected by the changes made to the original array.'''

# VIEW:
'''Example
Make a view, change the original array, and display both arrays:

import numpy as np

arr = np.array([1, 2, 3, 4, 5])'''
y = arr.view()
arr[0] = 42

print(arr)
print(y)

#The view SHOULD be affected by the changes made to the original array.


# Make Changes in the VIEW:
'''Example
Make a view, change the view, and display both arrays:

import numpy as np'''

arr2 = np.array([1, 2, 3, 4, 5])
z = arr.view()
z[0] = 31

print(arr2)
print(z)

'''The original array SHOULD be affected by the changes made to the view.'''

# Check if Array Owns its Data
'''As mentioned above, copies owns the data, and views does not own the data, but how can we check this?

Every NumPy array has the attribute base that returns None if the array owns the data.

Otherwise, the base  attribute refers to the original object.

Example
Print the value of the base attribute to check if an array owns it's data or not:

import numpy as np

arr = np.array([1, 2, 3, 4, 5])'''

a = arr.copy()
b = arr.view()

print(a.base)
print(b.base)
'''The copy returns None.
The view returns the original array.'''






