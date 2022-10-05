#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 16:46:25 2022

@author: craigrupp
"""

# =============================================================================
# OOP Refresher

# OOP has such main principles:
# inheritance
# encapsulation
# polymorphism
# =============================================================================


# =============================================================================
# Each class contains two kinds of information:
# 
# attributes: data stored in variables that describe the object (like the length of the tail, number of legs, hair color, etc.)
# methods: something that an object can do. Methods can change or not change the attributes(cat can eat and its weight increases, or cat can sleep and nothing happens).
# =============================================================================
class Dog:
  pass

# create your object
dog = Dog()
print(dog) # your object

# Basic Cat Class
class Cat:
  # attribute
  name = 'Kitty'
  # method
  def say_meow(self):
    print('Meow')

# object creating
cat = Cat()
cat.say_meow()


# Basic Class
# =============================================================================
# Each method obligatory contains parameter self: this is a reference to the current object.
# To call the method of the object, simply write it after the object's name and dot.
# To create an object, use the name of the class and ().
# =============================================================================

class Cat:
  name = 'Kitty'
  age = 2
  def sleep(self):
    print("Cat is sleeping")
  def say_meow(self):
    print('Meow')


cat = Cat()
cat.sleep()


# Use Class Method to update Attribute
class Cat:
  age = 1
  name = 'Kitty'
  def say_meow(self):
    print('Cat named', self.name, 'is', self.age, 'yrs old. Meow!')
  def set_age(self, new_age):
    self.age = new_age
    print(self.name, 'is', self.age, 'yrs old now.')

cat = Cat()
cat.say_meow()
cat.set_age(13)


# Constructor
# =============================================================================
# Constructor is a special method, which is automatically called during object creating.
# =============================================================================
# =============================================================================
# Constructor has reserved name __init__(). 
# You can pass or not pass arguments here (self is passed always). 
# =============================================================================
class Cat:
  def __init__(self, name='Kitty', hair_color = 'red'):
    self.name = name
    self.hair_color = hair_color
    
    
    
default_cat = Cat()
print(default_cat.hair_color, default_cat.name)
green_oliver = Cat('Oliver', 'green')
print(green_oliver.hair_color, green_oliver.name)    
yello_oscar = Cat(hair_color='yellow', name='Oscar')
print(yello_oscar.name, yello_oscar.hair_color)


# Another Cat
class Cat:
  def __init__(self, name='Default', age=5):
    self.name = name  
    self.age = age

littleCat = Cat('Bella', 2)
bigCat = Cat('Charlie', 12)
print("Little cat's attributes:", littleCat.name, littleCat.age)
print("Big cat's attributes:", bigCat.name, bigCat.age)






# =============================================================================
# Encapsulation
# =============================================================================
# =============================================================================
# Encapsulation provides access to the methods and attributes of the class. 
# During implementing the class as your data type, you must follow some rules to provide the correct work.
# =============================================================================
# =============================================================================
# Private : not available outside of the class
# Public : method/attribute avaialbe at any point of program (mutable)
# =============================================================================
# =============================================================================
# By default, all methods and attributes are public in the Python class. 
# To make an attribute private, add two underlines __ before the name:
# =============================================================================

# Private Cat
class Cat:
  def __init__(self, name='Kitty', age = 1):
    self.name = name
    self.__age = age
    self.__number_of_legs = 4 # this is private

cat = Cat('Maggie', 3)
print(cat.__age) # AttributeError: 'Cat' object has no attribute '__age'
print(cat._Cat__age)


# =============================================================================
# Given a class Dog. Add two private attributes weight and name and also one public attribute happy (this attribute contains either true or false in our class implementation)
# =============================================================================
class Dog:
  # set default values as: Puppy for name, 1 for weight, True for happy
  def __init__(self, name='Puppy', weight=1, happy=True):
      self.__name = name
      self.__weight = weight
      self.happy = happy




dog = Dog()
print('name:', dog._Dog__name)
print('weight:', dog._Dog__weight)
print('happy:', dog.happy)



# =============================================================================
# Get & Set 
# =============================================================================
# =============================================================================
# Get and set are methods for non-direct access to the attributes. 
# get() is a function that returns the value of the private attribute, and 
# set() sets the value. These methods are called properties.
# =============================================================================
class Cat:
  def __init__(self, name='Kitty', age = 1):
    self.name = name
    self.__age = age
    self.__children = 0 # how many children this cat has

  def get_age(self):
    return self.__age

  def set_age(self, age):
    if isinstance(age, int) and 0<=age<=30:
      self.__age = age
    else:
      print('Invalid value of attribute age')

cat = Cat('Maggie', 3)
cat.set_age(-23) # Wrong value
cat.set_age(8)
print(cat.get_age())


# Exercise
# =============================================================================
# Create get and set functions for __children attribute. 
# Consider that cat object can have at most 20 children. 
# If user is trying to set some wrong value, show the message Invalid value of attribute.
# =============================================================================

class Cat:
  def __init__(self, name='Kitty', age = 1):
    self.name = name
    self.__age = age
    self.__children = 0
    
  def get_children(self):
    return self.__children

  def set_children(self, children):
    if isinstance(children, int):
      self.__children = children
    else:
      print('Invalid value of attribute')

  
cat = Cat('Penny', 23)
# setting wrong value of attribute
cat.set_children('eight')

# setting correct value of attribute
cat.set_children(3)
print(cat.get_children())


# Attribute Annotations
# =============================================================================
# There is a special way to define properties – by using annotations starting with @ symbol.
# 
# Write @property to define get() method.
# Write @attribute.setter to define the set() method for the attribute.
# =============================================================================
class Cat:

  def __init__(self, name='Kitty', age = 1):
    self.name = name
    self.__age = age
    self.__number_of_legs = 4

  @property
  def age(self):
    return self.__age

  @age.setter
  def age(self, age):
    if isinstance(age, int) and 0<=age<=30:
      self.__age = age
    else:
      print('Invalid value of attribute age')

cat = Cat('Maggie', 3)
cat.age = -100 # Wrong value
cat.age = 5
print(cat.age)
# Set function invoked with equality, not a method call Ex : cat.age(8) = 'int' object is not callable
cat.age = 8
print(cat.age)



# Exercise
# =============================================================================
# Create getter and setter for attribute tail_length using annotations. 
# Do that exactly like in the example but for tail_length (warning message should be displayed for wrong value). 
# Consider that the value should be in the range [0, 50] cm.
# =============================================================================











