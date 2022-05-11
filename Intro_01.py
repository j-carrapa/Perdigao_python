# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("hello world")
a=20
b=20.0
c="grgkrokd hgko"
if 5 > 2:
    print("lalala")
n=9
#comentários
"""
this is the way of making a multiline
comment
"""
j = k, l = 2, 4
fruits = ["asd", "bid", "ghjdo"]
x, y, z = fruits
print(x)
print(y)
print(z)
print(x, a)
f = "awesome"
def func1():
    global f
    f = "fantastic"
    print("python is " + f)
    
func1()

print("python is " + f)
import random
print(random.randrange(1, 10))
s = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(s)
print(c[2])
#Loop through the letters in the word "banana":
for q in "banana":
    print(q)

#To get the length of a string, use the len() function.
print(len(c))
txt = "The best things in life are free!"
print("free" in txt)
txt = "The best things in life are free!"
print("expensive" not in txt)