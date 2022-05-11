# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 16:19:40 2022

@author: João
"""

# Try Except, User Input and String Formatting

'''The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.

Exception Handling
When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

These exceptions can be handled using the try statement:

Example
The try block will generate an exception, because x is not defined:'''

'''try:
  print(x)
except:
  print("An exception occurred")'''
  
'''Since the try block raises an error, the except block will be executed.

Without the try block, the program will crash and raise an error:

Example
This statement will raise an error, because y is not defined:'''

#print(y)

'''Many Exceptions
You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:

Example
Print one message if the try block raises a NameError and another for other errors:'''
'''
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
'''
'''Else
You can use the else keyword to define a block of code to be executed if no errors were raised:

Example
In this example, the try block does not generate any error:'''
'''
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
'''
'''Finally
The finally block, if specified, will be executed regardless if the try block raises an error or not.

Example'''
'''
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
'''
'''This can be useful to close objects and clean up resources:

Example
Try to open and write to a file that is not writable:'''

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")

'''The program can continue, without leaving the file object open.

Raise an exception
As a Python developer you can choose to throw an exception if a condition occurs.

To throw (or raise) an exception, use the raise keyword.

Example
Raise an error and stop the program if x is lower than 0:'''

#x = -1

#if x < 0:
#  raise Exception("Sorry, no numbers below zero")
'''The raise keyword is used to raise an exception.

You can define what kind of error to raise, and the text to print to the user.

Example
Raise a TypeError if x is not an integer:'''
'''
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")
'''

# User Input

'''User Input
Python allows for user input.

That means we are able to ask the user for input.

The method is a bit different in Python 3.6 than Python 2.7.

Python 3.6 uses the input() method.

Python 2.7 uses the raw_input() method.

The following example asks for the username, and when you entered the username, it gets printed on the screen:

Python 3.6'''
username = input("Enter username:")
print("Username is: " + username)

# String Formatting

'''String format()
The format() method allows you to format selected parts of a string.

Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?

To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method:

Example
Add a placeholder where you want to display the price:'''

price = 49
txt = "The price is {} dollars"
print(txt.format(price))

'''You can add parameters inside the curly brackets to specify how to convert the value:

Example
Format the price to be displayed as a number with two decimals:

txt = "The price is {:.2f} dollars"
Check out all formatting types in our String format() Reference.'''

'''Multiple Values
If you want to use more values, just add more values to the format() method:

print(txt.format(price, itemno, count))
And add more placeholders:

Example'''
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

'''Index Numbers
You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholders:

Example
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))
'''

'''Also, if you want to refer to the same value more than once, use the index number:

Example'''
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

'''Named Indexes
You can also use named indexes by entering a name inside the curly brackets {carname}, but then you must use names when you pass the parameter values txt.format(carname = "Ford"):

Example'''
myorder2 = "I have a {carname}, it is a {model}."
print(myorder2.format(carname = "Ford", model = "Mustang"))


