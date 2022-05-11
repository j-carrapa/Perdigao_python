# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 17:18:40 2022

@author: João
"""

#strings exercises file
b = "Hello, World!"
print(b[2:5])
print(b[2:])
print(b[-5:-2])
print(b.upper())
print(b.lower())
o = " Hello, World! "
print(o.strip()) # returns "Hello, World!"
a1 = "Hello, World!"
print(a1.replace("o", "J"))
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
d = "Hello"
e = "World"
c = d + e
print(c)
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
myorder2 = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder2.format(quantity, itemno, price))
txt2 = "We are the so-called \"Vikings\" from the north."
print(txt2)
txt3 = "Hello, welcome to my world."

x = txt3.find("welcome")

print(x)
#diferença entre find e index
print(txt3.find("q"))
#print(txt3.index("q"))

#join method
myTuple = ("John", "Peter", "Vicky")

f = "#".join(myTuple)

print(f)
