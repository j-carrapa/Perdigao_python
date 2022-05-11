# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 11:50:24 2022

@author: João
"""

# Dates and Math

'''Python Dates
A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

Example
Import the datetime module and display the current date:'''

import datetime

x = datetime.datetime.now()
print(x)
'''Date Output
When we execute the code from the example above the result will be:

2022-04-22 11:49:13.542335
The date contains year, month, day, hour, minute, second, and microsecond.

The datetime module has many methods to return information about the date object.

Here are a few examples, you will learn more about them later in this chapter:

Example
Return the year and name of weekday:

import datetime

x = datetime.datetime.now()'''

print(x.year)
print(x.strftime("%A"))
'''Creating Date Objects
To create a date, we can use the datetime() class (constructor) of the datetime module.

The datetime() class requires three parameters to create a date: year, month, day.

Example
Create a date object:

import datetime'''

y = datetime.datetime(2020, 5, 17)

print(y)
'''The datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone).

The strftime() Method
The datetime object has a method for formatting date objects into readable strings.

The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:

Example
Display the name of the month:

import datetime'''

z = datetime.datetime(2018, 6, 1)

print(z.strftime("%B"))
'''A reference of all the legal format codes:

Directive	Description                           	Example	
%a      	Weekday, short version                 	Wed	
%A      	Weekday, full version                 	Wednesday	
%w      	Weekday as a number 0-6, 0 is Sunday	3	
%d      	Day of month 01-31                     	31	
%b      	Month name, short version              	Dec	
%B      	Month name, full version	            December	
%m      	Month as a number 01-12	                12	
%y      	Year, short version, without century	18	
%Y      	Year, full version                     	2018	
%H      	Hour 00-23                             	17	
%I      	Hour 00-12                             	05	
%p      	AM/PM                                  	PM	
%M      	Minute 00-59                           	41	
%S      	Second 00-59                           	08	
%f      	Microsecond 000000-999999              	548513	
%z       	UTC offset                            	+0100	
%Z      	Timezone                               	CST	
%j      	Day number of year 001-366             	365	
%U      	Week number of year, Sunday as the first day of week, 00-53        	52	
%W      	Week number of year, Monday as the first day of week, 00-53        	52	
%c      	Local version of date and time         	Mon Dec 31 17:41:00 2018	
%C      	Century                                	20	
%x      	Local version of date                  	12/31/18	
%X      	Local version of time                  	17:41:00	
%%      	A % character                          	%	
%G      	ISO 8601 year                          	2018	
%u      	ISO 8601 weekday (1-7)                 	1	
%V      	ISO 8601 weeknumber (01-53)            	01
'''

# Math

'''Python has a set of built-in math functions, including an extensive math module, that allows you to perform mathematical tasks on numbers.

Built-in Math Functions
The min() and max() functions can be used to find the lowest or highest value in an iterable:

Example'''
a = min(5, 10, 25)
b = max(5, 10, 25)

print(a)
print(b)
'''The abs() function returns the absolute (positive) value of the specified number:

Example'''
c = abs(-7.25)

print(c)
'''The pow(x, y) function returns the value of x to the power of y (xy).

Example
Return the value of 4 to the power of 3 (same as 4 * 4 * 4):'''

d = pow(4, 3)

print(d)
'''The Math Module
Python has also a built-in module called math, which extends the list of mathematical functions.

To use it, you must import the math module:'''

import math
'''When you have imported the math module, you can start using methods and constants of the module.

The math.sqrt() method for example, returns the square root of a number:

Example
import math'''

e = math.sqrt(64)

print(e)
'''The math.ceil() method rounds a number upwards to its nearest integer, and the math.floor() method rounds a number downwards to its nearest integer, and returns the result:

Example
import math'''

f = math.ceil(1.4)
g = math.floor(1.4)

print(f) # returns 2
print(g) # returns 1
'''The math.pi constant, returns the value of PI (3.14...):

Example
import math'''

h = math.pi

print(h)
'''Complete Math Module Reference
In our Math Module Reference you will find a complete reference of all methods and constants that belongs to the Math module.'''