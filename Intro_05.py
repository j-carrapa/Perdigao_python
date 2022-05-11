# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 16:39:59 2022

@author: João
"""

# Tuple
# used to store multiple items
# a tuple is a collection which is ordered and UNCHANGEABLE - nice for security reasons

#Tuples are written with round brackets.

thistuple = ("apple", "banana", "cherry")
print(thistuple)

'''
Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

Allow duplicates
Since tuples are indexed, they can have items with the same value:'''

#tuple lenght - use len() function

print(len(thistuple))

'''Create Tuple With One Item
To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.'''

thistuple2 = ("apple",)
print(type(thistuple2))

#Tuple items can be of any data type and can contain different data types

'''The tuple() Constructor
It is also possible to use the tuple() constructor to make a tuple.'''

thistuple3 = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple3)

'''Access Tuple Items
You can access tuple items by referring to the index number, inside square brackets:'''

print(thistuple[1])

'''Negative Indexing - igual às listas
Negative indexing means start from the end.

-1 refers to the last item, -2 refers to the second last item etc.'''

'''Range of Indexes
You can specify a range of indexes by specifying where to start and where to end the range.

When specifying a range, the return value will be a new tuple with the specified items.

Example
Return the third, fourth, and fifth item:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
By leaving out the start value, the range will start at the first item:
By leaving out the end value, the range will go on to the end of the list:
 
 This example returns the items from index -4 (included) to index -1 (excluded)

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])   
 '''

'''Check if Item Exists
To determine if a specified item is present in a tuple use the in keyword:

Example
Check if "apple" is present in the tuple:'''

if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

'''Change Tuple Values
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.'''

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

'''Add Items
Since tuples are immutable, they do not have a build-in append() method, but there are other ways to add items to a tuple.

1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.'''

#Convert the tuple into a list, add "orange", and convert it back into a tuple:
    
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

'''2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:'''

#Create a new tuple with the value "orange", and add that tuple:
    
thistuple4 = ("apple", "banana", "cherry")
y2 = ("orange",)#Note: When creating a tuple with only one item, remember to include a comma after the item, otherwise it will not be identified as a tuple.
thistuple4 += y2

print(thistuple4)

'''Remove Items
Note: You cannot remove items in a tuple.

Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items:'''

#Convert the tuple into a list, remove "apple", and convert it back into a tuple:
    
thistuple5 = ("apple", "banana", "cherry")
y3 = list(thistuple5)
y3.remove("apple")
thistuple5 = tuple(y3)

# Or The del keyword can delete the tuple completely:
    
thistuple6 = ("apple", "banana", "cherry")
del thistuple6
#print(thistuple6) #this will raise an error because the tuple no longer exists

'''Unpacking a Tuple
When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

Example
Packing a tuple:

fruits = ("apple", "banana", "cherry")

But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

Example
Unpacking a tuple:'''

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

'''Using Asterisk*
If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:

Example
Assign the rest of the values as a list called "red":'''

fruits2 = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits2

print(green)
print(yellow)
print(red)

'''If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.

Example
Add a list of values the "tropic" variable:'''

(green, *tropic, red) = fruits2

print(green)
print(tropic)
print(red)


'''Loop Through a Tuple
You can loop through the tuple items by using a for loop.

Example
Iterate through the items and print the values:'''

for x in thistuple:
  print(x)

'''Loop Through the Index Numbers
You can also loop through the tuple items by referring to their index number.

Use the range() and len() functions to create a suitable iterable.

Example
Print all items by referring to their index number:'''

print() #só para deixar um espaço

for i in range(len(thistuple)):
  print(thistuple[i])
  
'''Using a While Loop
You can loop through the list items by using a while loop.

Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by refering to their indexes.

Remember to increase the index by 1 after each iteration.

Example
Print all items, using a while loop to go through all the index numbers:'''

i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
  
'''Join Two Tuples
To join two or more tuples you can use the + operator:'''

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

'''Multiply Tuples
If you want to multiply the content of a tuple a given number of times, you can use the * operator:

Example
Multiply the fruits tuple by 2:'''

mytuple = fruits * 2

print(mytuple)

'''Tuple Methods
Python has two built-in methods that you can use on tuples.

Method	Description
count() 	Returns the number of times a specified value occurs in a tuple
index() 	Searches the tuple for a specified value and returns the position of where it was found'''




