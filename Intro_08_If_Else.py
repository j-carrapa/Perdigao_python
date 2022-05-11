# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 12:24:18 2022

@author: João
"""

# If Else

'''Python Conditions and If statements
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword.

Example
If statement:'''

a = 33
b = 200
if b > a:
  print("b is greater than a")
  
'''Indentation
Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.

Example
If statement, without indentation (will raise an error):

if b > a:
print("b is greater than a") # you will get an error'''

'''Elif
The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".

Example'''

c = 33
if c > a:
  print("c is greater than a")
elif a == c:
  print("a and c are equal")
  
'''Else
The else keyword catches anything which isn't caught by the preceding conditions.

Example'''

if a > b:
  print("a is greater than b")
elif a == b:
  print("a and b are equal")
else:
  print("b is greater than a")  

'''Short Hand If
If you have only one statement to execute, you can put it on the same line as the if statement.

Example
One line if statement:'''

if b > c: print("b is greater than c")

'''Short Hand If ... Else
If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:

Example
One line if else statement:'''

print("A") if a > b else print("B")

'''This technique is known as Ternary Operators, or Conditional Expressions.

You can also have multiple else statements on the same line:

Example
One line if else statement, with 3 conditions:'''

d = 330
b = 330
print("D") if d > b else print("=") if d == b else print("B")

'''And
The and keyword is a logical operator, and is used to combine conditional statements:

Example
Test if b is greater than a, AND if e is greater than a:'''

e = 500

if b > a and e > a:
  print("Both conditions are True")

'''Or
The or keyword is a logical operator, and is used to combine conditional statements:

Example
Test if a is greater than b, OR if e is greater than b:'''

if a > b or e > b:
  print("At least one of the conditions is True")

'''Nested If
You can have if statements inside if statements, this is called nested if statements.

Example'''
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

'''The pass Statement
if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

Example'''

if b > a:
  pass


