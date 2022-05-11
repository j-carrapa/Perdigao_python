# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 17:01:01 2022

@author: João
"""

'''import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")'''
  
#f = open("myfile.txt","x") ficheiro já criado

f= open("myfile.txt","w")
f.write("Hello! Welcome to myfile.txt\n")
f.write("This file is for testing purposes.\n")
f.write("Good Luck!")
f.close()

#open and read the file after the appending:
f = open("myfile.txt", "r")
print(f.read())
  

'''Read Lines
You can return one line by using the readline() method:

Example
Read one line of the file:'''

d = open("myfile.txt", "r")
print(d.readline())
'''By calling readline() two times, you can read the two first lines:

Example
Read two lines of the file:

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())


By looping through the lines of the file, you can read the whole file, line by line:

Example
Loop through the file line by line:'''

s = open("myfile.txt", "r")
for x in s:
  print(x)

f.close()
d.close()
s.close()