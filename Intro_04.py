# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 11:38:26 2022

@author: João
"""

# Python Lists

# exemplo list
thislist = ["apple", "banana", "cherry"]
print(thislist)

#list lenght

print(len(thislist))

#A list can contain different data types:
list1 = ["abc", 34, True, 40, "male"]

#From Python's perspective, lists are defined as objects with the data type 'list':

#It is also possible to use the list() constructor when creating a new list.

thislist2 = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist2)

#List items are indexed and you can access them by referring to the index number:

print(thislist[1])

#Negative indexing means start from the end

#-1 refers to the last item, -2 refers to the second last item etc.

print(thislist[-1])

#range of indexes

thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist2[2:5])

#Note: The search will start at index 2 (included) and end at index 5 (not included).

#Remember that the first item has index 0.

#By leaving out the start value, the range will start at the first item:
#By leaving out the end value, the range will go on to the end of the list:
    
#This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
    
print(thislist2[-4:-1])

#Check if "apple" is present in the list:
    
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#Change the second item:
    
thislist[1] = "blackcurrant"
print(thislist)

#To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:

thislist2[1:3] = ["blackcurrant", "watermelon"]
print(thislist2)

#If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

thislist[1:2] = ["medronho", "watermelon"]
print(thislist)

#If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
    
thislist[1:3] = ["watermelon"]
print(thislist)

#The insert() method inserts an item at the specified index:

thislist.insert(2, "medronho")
print(thislist)

#To add an item to the end of the list, use the append() method:
    
thislist.append("orange")
print(thislist)

#To append elements from another list to the current list, use the extend() method.

tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#Add Any Iterable - The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# The remove() method removes the specified item.

thislist.remove("orange")

print(thislist)

# Nota: o remove() só removeu o primeiro item em que apareceu orange

#Remove Specified Index - The pop() method removes the specified index.

thislist.pop(1)
print(thislist)

#If you do not specify the index, the pop() method removes the last item.

# The del keyword also removes the specified index:
    
del thislist[3]
print(thislist)

#The del keyword can also delete the list completely.

del thislist

#The clear() method empties the list. The list still remains, but it has no content.

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#Loop Through a List - You can loop through the list items by using a for loop:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

'''Loop Through the Index Numbers
You can also loop through the list items by referring to their index number.

Use the range() and len() functions to create a suitable iterable.'''

for i in range(len(thislist)):
  print(thislist[i])

'''Using a While Loop
You can loop through the list items by using a while loop.

Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by refering to their indexes.

Remember to increase the index by 1 after each iteration.'''

i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

'''Looping Using List Comprehension
List Comprehension offers the shortest syntax for looping through lists:
 A short hand for loop that will print all items in a list:'''

[print(x) for x in thislist]

'''List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

Example:

Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

Without list comprehension you will have to write a for statement with a conditional test inside:'''

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#With list comprehension you can do all that with only one line of code:
    
newlist2 = [x for x in fruits if "a" in x]

print(newlist2)

'''The Syntax
newlist = ['expression' for 'item' in 'iterable' if 'condition' == True]
The return value is a new list, leaving the old list unchanged.'''

#The condition is like a filter that only accepts the items that valuate to True.

#The iterable can be any iterable object, like a list, tuple, set etc.

newlist3 = [x for x in range(10) if x <5]
print(newlist3)

#The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:
    
newlist4 = [x.upper() for x in fruits]

#The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
    
newlist5 = [x if x != "banana" else "orange" for x in fruits]
print(newlist5)

#Sort List Alphanumerically
#List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

thislist2.sort()
print(thislist2)

thislist3 = [100, 50, 65, 82, 23]
thislist3.sort()
print(thislist3)

'''Sort Descending
To sort descending, use the keyword argument reverse = True:'''

thislist2.sort(reverse = True)
print(thislist2)

'''Customize Sort Function
You can also customize your own function by using the keyword argument key = function.

The function will return a number that will be used to sort the list (the lowest number first):

Example
Sort the list based on how close the number is to 50:'''

def myfunc(n):
  return abs(n - 50)

thislist3.sort(key = myfunc)
print(thislist3)

'''Case Insensitive Sort
By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
    Case sensitive sorting can give an unexpected result:'''

thislist4 = ["banana", "Orange", "Kiwi", "cherry"]
thislist4.sort()
print(thislist4)

'''Luckily we can use built-in functions as key functions when sorting a list.

So if you want a case-insensitive sort function, use str.lower as a key function:'''

thislist4.sort(key = str.lower)
print(thislist4)

'''Reverse Order
What if you want to reverse the order of a list, regardless of the alphabet?

The reverse() method reverses the current sorting order of the elements.'''

thislist4.reverse()
print(thislist4)

'''Copy a List
You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

There are ways to make a copy, one way is to use the built-in List method copy().'''

mylist = thislist.copy()
print(mylist)

#Another way to make a copy is to use the built-in method list().

mylist2 = list(thislist)
print(mylist2)

# uma outra maneira (mais trabalhosa) é usando o list comprehension: newlist2 = [x for x in fruits] que cria uma lista igual pois não tem nenhuma condição

'''Join Two Lists
There are several ways to join, or concatenate, two or more lists in Python.

One of the easiest ways are by using the + operator.'''

list1 = ["a", "b", "c"]
list4 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Ou appending

for x in list2:
  list1.append(x)

print(list1)

#Ou extend

list4.extend(list2)
print(list4)

'''
Method	    Description
append()	Adds an element at the end of the list
clear() 	Removes all the elements from the list
copy()  	Returns a copy of the list
count() 	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index() 	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()   	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()  	Sorts the list'''

