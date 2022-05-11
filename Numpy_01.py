# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 00:36:21 2022

@author: João
"""

# Numpy Introduction

'''What is NumPy?
NumPy is a Python library used for working with arrays.

It also has functions for working in domain of linear algebra, fourier transform, and matrices.

NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.

NumPy stands for Numerical Python.

Why Use NumPy?
In Python we have lists that serve the purpose of arrays, but they are slow to process.

NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.

The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.

Arrays are very frequently used in data science, where speed and resources are very important.

Data Science: is a branch of computer science where we study how to store, use and analyze data for deriving information from it.'''

'''Why is NumPy Faster Than Lists?
NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.

This behavior is called locality of reference in computer science.

This is the main reason why NumPy is faster than lists. Also it is optimized to work with latest CPU architectures.

Which Language is NumPy written in?
NumPy is a Python library and is written partially in Python, but most of the parts that require fast computation are written in C or C++.

Where is the NumPy Codebase?
The source code for NumPy is located at this github repository https://github.com/numpy/numpy

github: enables many people to work on the same codebase.'''


#NumPy Getting Started
'''Installation of NumPy
If you have Python and PIP already installed on a system, then installation of NumPy is very easy.

Install it using this command:
'''
#C:\Users\Your Name>pip install numpy
'''If this command fails, then use a python distribution that already has NumPy installed like, Anaconda, Spyder etc.

Import NumPy
Once NumPy is installed, import it in your applications by adding the import keyword:

import numpy
Now NumPy is imported and ready to use.

Example
import numpy

arr = numpy.array([1, 2, 3, 4, 5])

print(arr)
NumPy as np
NumPy is usually imported under the np alias.

alias: In Python alias are an alternate name for referring to the same thing.

Create an alias with the as keyword while importing:

import numpy as np
Now the NumPy package can be referred to as np instead of numpy.

Example
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
Checking NumPy Version
The version string is stored under __version__ attribute.

Example
import numpy as np

print(np.__version__)
'''


#Create a NumPy ndarray Object
'''NumPy is used to work with arrays. The array object in NumPy is called ndarray.

We can create a NumPy ndarray object by using the array() function.

Example'''
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))
'''type(): This built-in Python function tells us the type of the object passed to it. Like in above code it shows that arr is numpy.ndarray type.

To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray:

Example
Use a tuple to create a NumPy array:

import numpy as np
'''
arr2 = np.array((1, 2, 3, 4, 5))

print(arr2)


#Dimensions in Arrays
'''A dimension in arrays is one level of array depth (nested arrays).

nested array: are arrays that have arrays as their elements.

0-D Arrays
0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.

Example
Create a 0-D array with value 42

import numpy as np

arr = np.array(42)

print(arr)
'''

#1-D Arrays
'''An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.

These are the most common and basic arrays.

Example
Create a 1-D array containing the values 1,2,3,4,5:

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)'''


#2-D Arrays
'''An array that has 1-D arrays as its elements is called a 2-D array.

These are often used to represent matrix or 2nd order tensors.

NumPy has a whole sub module dedicated towards matrix operations called numpy.mat

Example
Create a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)'''


#3-D arrays
'''An array that has 2-D arrays (matrices) as its elements is called 3-D array.

These are often used to represent a 3rd order tensor.

Example
Create a 3-D array with two 2-D arrays, both containing two arrays with the values 1,2,3 and 4,5,6:

import numpy as np'''

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr3)


#Check Number of Dimensions?
'''NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.

Example
Check how many dimensions the arrays have:

import numpy as np'''

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


#Higher Dimensional Arrays
'''An array can have any number of dimensions.

When the array is created, you can define the number of dimensions by using the ndmin argument.

Example
Create an array with 5 dimensions and verify that it has 5 dimensions:

import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)
In this array the innermost dimension (5th dim) has 4 elements, the 4th dim has 1 element that is the vector, the 3rd dim has 1 element that is the matrix with the vector, the 2nd dim has 1 element that is 3D array and 1st dim has 1 element that is a 4D array.'''


# Array Indexing

'''Access Array Elements
Array indexing is the same as accessing an array element.

You can access an array element by referring to its index number.

The indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second has index 1 etc.

Example
Get the first element from the following array:

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0])

Example
Get the second element from the following array.

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[1])
Example
Get third and fourth elements from the following array and add them.

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[2] + arr[3])
'''

# Access 2-D Arrays
'''To access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element.

Think of 2-D arrays like a table with rows and columns, where the row represents the dimension and the index represents the column.

Example
Access the element on the first row, second column:

import numpy as np'''

arr4 = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr4[0, 1])
'''Example
Access the element on the 2nd row, 5th column:

import numpy as np'''

arr5 = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('5th element on 2nd row: ', arr5[1, 4])


# Access 3-D Arrays
'''To access elements from 3-D arrays we can use comma separated integers representing the dimensions and the index of the element.

Example
Access the third element of the second array of the first array:

import numpy as np'''

arr6 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr6[0, 1, 2])


# Negative Indexing
'''Use negative indexing to access an array from the end.

Example
Print the last element from the 2nd dim:

import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1])'''