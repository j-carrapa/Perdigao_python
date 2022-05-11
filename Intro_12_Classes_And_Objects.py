# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 19:28:40 2022

@author: João
"""

# Classes and Objects

'''Python Classes/Objects
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.

Create a Class
To create a class, use the keyword class:

Example
Create a class named MyClass, with a property named x:'''

class MyClass:
  x = 5

'''Create Object
Now we can use the class named MyClass to create objects:

Example
Create an object named p1, and print the value of x:'''

p1 = MyClass()
print(p1.x)

'''The __init__() Function
The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

To understand the meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

Example
Create a class named Person, use the __init__() function to assign values for name and age:'''

class Person2:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p2 = Person2("John", 36)

print(p2.name)
print(p2.age)

#Note: The __init__() function is called automatically every time the class is being used to create a new object.

'''Object Methods
Objects can also contain methods. Methods in objects are functions that belong to the object.

Let us create a method in the Person class:

Example
Insert a function that prints a greeting, and execute it on the p1 object:'''

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p3 = Person("John", 36)
p3.myfunc()

#Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

'''The self Parameter
The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

Example
Use the words mysillyobject and abc instead of self:'''

class Person3:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p4 = Person("John", 36)
p4.myfunc()

'''Modify Object Properties
You can modify properties on objects like this:

Example
Set the age of p1 to 40:'''

p4.age = 40

print(p4.age)

'''Delete Object Properties
You can delete properties on objects by using the del keyword:

Example
Delete the age property from the p1 object:'''

del p4.age

#print(p4.age)#só para mostrar o erro
'''Delete Objects
You can delete objects by using the del keyword:

Example
Delete the p1 object:'''

del p4

#print(p4.age)#só para mostrar o erro
'''The pass Statement
class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

Example'''
class Person4:
  pass

#Python Inheritance

'''Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.

Create a Parent Class
Any class can be a parent class, so the syntax is the same as creating any other class:

Example
Create a class named Person, with firstname and lastname properties, and a printname method:'''

class Pessoa:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Pessoa class to create an object, and then execute the printname method:

x = Pessoa("John", "Doe")
x.printname()

'''Create a Child Class
To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

Example
Create a class named Student, which will inherit the properties and methods from the Person class:'''

class Student(Pessoa):
  pass
'''Note: Use the pass keyword when you do not want to add any other properties or methods to the class.

Now the Student class has the same properties and methods as the Person class.

Example
Use the Student class to create an object, and then execute the printname method:'''

y = Student("Mike", "Olsen")
y.printname()

'''Add the __init__() Function
So far we have created a child class that inherits the properties and methods from its parent.

We want to add the __init__() function to the child class (instead of the pass keyword).

Note: The __init__() function is called automatically every time the class is being used to create a new object.

Example
Add the __init__() function to the Student class:'''

#class Student2(Pessoa):
#  def __init__(self, fname, lname):
    #add properties etc.
    
'''When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.

To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

Example'''
class Student2(Pessoa):
  def __init__(self, fname, lname):
    Pessoa.__init__(self, fname, lname)

#Now we have successfully added the __init__() function, and kept the inheritance of the parent class, and we are ready to add functionality in the __init__() function.

'''Use the super() Function
Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

Example'''
'''class Student3(Pessoa):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)'''
'''By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

Add Properties
Example
Add a property called graduationyear to the Student class:'''

class Student3(Pessoa):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019
'''In the example below, the year 2019 should be a variable, and passed into the Student class when creating student objects. To do so, add another parameter in the __init__() function:

Example
Add a year parameter, and pass the correct year when creating objects:'''

class Student4(Pessoa):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student4("Miro", "Olsen", 2019)

'''Add Methods
Example
Add a method called welcome to the Student class:'''

class Student5(Pessoa):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


z = Student5("Miro", "Olsen", 2019)

z.welcome()




