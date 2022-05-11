# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 17:29:35 2022

@author: João
"""

# Matplotlib


'''What is Matplotlib?
Matplotlib is a low level graph plotting library in python that serves as a visualization utility.

Matplotlib was created by John D. Hunter.

Matplotlib is open source and we can use it freely.

Matplotlib is mostly written in python, a few segments are written in C, Objective-C and Javascript for Platform compatibility.

Where is the Matplotlib Codebase?
The source code for Matplotlib is located at this github repository https://github.com/matplotlib/matplotlib'''


'''Installation of Matplotlib
If you have Python and PIP already installed on a system, then installation of Matplotlib is very easy.
Install it using this command:
'''
#C:\Users\Your Name>pip install matplotlib
'''If this command fails, then use a python distribution that already has Matplotlib installed,  like Anaconda, Spyder etc.

Import Matplotlib
Once Matplotlib is installed, import it in your applications by adding the import module statement:

import matplotlib
Now Matplotlib is imported and ready to use:'''

'''Checking Matplotlib Version
The version string is stored under __version__ attribute.

Example
import matplotlib

print(matplotlib.__version__)
Note: two underscore characters are used in __version__.'''


# Pyplot

'''Most of the Matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias:

import matplotlib.pyplot as plt
Now the Pyplot package can be referred to as plt.

Example
Draw a line in a diagram from position (0,0) to position (6,250):

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()
Result:


You will learn more about drawing (plotting) in the next chapters.
'''


#Plotting x and y points
'''The plot() function is used to draw points (markers) in a diagram.

By default, the plot() function draws a line from point to point.

The function takes parameters for specifying points in the diagram.

Parameter 1 is an array containing the points on the x-axis.

Parameter 2 is an array containing the points on the y-axis.

If we need to plot a line from (1, 3) to (8, 10), we have to pass two arrays [1, 8] and [3, 10] to the plot function.

Example
Draw a line in a diagram from position (1, 3) to position (8, 10):

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()
'''


