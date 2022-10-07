#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 09:15:01 2022

@author: craigrupp
"""

# Inheritance
# =============================================================================
# Imagine you have to create classes: Cat, Dog, and Parrot. 
# For each of them, you’ll add attributes and methods, getters and setters, 
# but then you’ll realize that the whole code is similar in different classes: same attributes name, age, number_of_legs, etc., 
# same methods eat(), sleep(), say_something(), same logic at all. 
# You can avoid creating three almost similar classes using the Inheritance principle.
# =============================================================================

# We’ll define this class later
class Animal:
  pass

# To inherit the class, use the following syntax:
class Cat(Animal):
  pass

# Child / Class Hierarchy / Multiple Classes
# =============================================================================
# The child class has all the same methods and attributes that parents have, and can have additional ones, 
# but not vice versa: the parent’s class cannot have the children's additional attributes. 
# Children's class is an extension of the parent class.
# =============================================================================
# =============================================================================
# Each class in Python can have multiple parent’s classes and/or children's classes.
# =============================================================================


# Task Inheritance
# =============================================================================
# As you know, the superclass is a base class. The Animal is a base class for Cat, Dog, and Parrot classes. 
# These classes can refer to the Animal’s methods and attributes, but only public ones. 
# Private methods and attributes of the parent class are not available in child's class.
# =============================================================================
class Animal:
  __number_of_legs = None
  max_age = None
  def __init__(self, name = None, age = None):
    self.__name = name
    self.__age = age

  def move(self):
    print('Animal is moving...')
    

# =============================================================================
# Create a class Cat which inherits the Animal class. Do the following steps without changing the superclass Animal:
# 
# Add the private attribute weight.
# Define the Cat constructor that initializes all the following private attributes: name, age, and weight.
# Define the eat() method that increases the cat's weight by 1 and prints message '{name} weight is {weight} kg no
# =============================================================================

class Cat(Animal):
    def __init__(self, name = None, age = None, weight = None):
        self.__name = name 
        self.__age = age 
        self.__weight = weight 
        
    def eat(self):
        self.__weight += 1
        print(self.__name, 'weight is', self.__weight, 'kg now')  
        


cat1 = Animal('Lisa', 12) # Animal object
cat1.move() # note that there is no eat() method for the Animal object

cat2 = Cat('Lola', 10, 5) # Cat object
cat2.move() # calling parent public method
cat2.eat() # calling particular cat method
cat1.eat() # Super (parent object) has no access to child method


# Method super()
# =============================================================================
# To call parent's class method instead of the current, in Python we use super() method
# =============================================================================
class Animal:
  def __init__(self, name):
    print('Calling Animal constructor')
    self.name = name

class Cat(Animal):
  def __init__(self, name, age):
    print('Calling Cat constructor')
    super().__init__(name)
    self.age = age

cat = Cat(name='Archie', age=12)
print(f'Created a cat with attributes: name={cat.name}, age={cat.age}')

# =============================================================================
# While creating Cat object by calling Cat(), inside the __init__ constructor of Cat class the super() method refers to the parent's class Animal. 
# So Animal constructor is called first. The object cat now has a public attribute name.

# After that, go back to the Cat constructor and initialize the age attribute.
# =============================================================================


# Task
# =============================================================================
# Try to use the super() method inside other methods. For a given class Square, implement the constructor using the super() method, 
# then use the Rectangles method area() inside the Square class
# =============================================================================

class Rectangle:
  def __init__(self, width, height):
    print('Calling Rectangle constructor')
    self.width = width
    self.height = height
  def area(self):
    return self.width * self.height

class Square(Rectangle):
  def __init__(self, length):
    print('Calling Square constructor')
    super().__init__(length, length)
    
  def area(self):
    return super().area()


fig = Square(19)
print(f'Created square with area {fig.area()}')
print(fig.height, fig.width)




# Built-in Get and Set
# =============================================================================
# Besides attributes annotations, Python provides usage of built-in methods:
# 
# __getattr__(self, name) returns the value of name attribute if it exists. Otherwise, it raises AttributeError.
# __setattr__(self, name, value) assigns the name attribute with value if it exists. Otherwise, the name attribute is created (with value value).
# =============================================================================
class Cat:
  age = 0

  def __setattr__(self, name, value):
    if name=='age': # check if this is age attribute
      # raise Error if the value is wrong
      if not (isinstance(value, int) and 0 <= value <= 30):
        raise AttributeError('Unexpected value for age')
    else: # value is okay or attribute is not 'age'
      super().__setattr__(name, value) # call standard __setattr__()

cat = Cat()
cat.age = 10 # OK
print(cat.age)
cat.name = 'Daisy' # OK
cat.age = 100 #  AttributeError
print(cat.name)
print(cat.age)


# Task
# =============================================================================
# Change the __setattr__() method but only for name and weight attributes of class Cat.
# 
# name must be only string values. Otherwise, raise AttributeError with the message 'Unexpected value for name.'.
# weight must be only int values from the range [0, 20]. Otherwise, raise AttributeError with the message 'Unexpected value for weight.'.
# Additionally, output the message name : value (name and value are parameters of the function __setattr__()) every time the method is calling, but only if errors haven't been raised
# =============================================================================


class Cat:

  def __setattr__(self, name, value):
    if name == 'name':
      if not (isinstance(value, str)):
        raise AttributeError('Unexpected value for name')
      else:
        super().__setattr__(name, value)
        print(f"{name} : {value}")
    if name == 'weight':
      if not (isinstance(value, int) and 0 <= value <= 20):
        raise AttributeError('Unexpected value for weight')
      else:
        super().__setattr__(name, value)
        print(f"{name} : {value}")



cat = Cat()

# correct values
cat.weight = 10
cat.name = 'Lilly'

# incorrect values
cat.name = True
cat.age = -7
print(cat.name, cat.weight)




# Polymorphism – a class property to modify superclass functionality
# =============================================================================
# In Python, Polymorphism lets a user define methods in the child class with the same name as in the parent class, but the implementation can be different.
# =============================================================================
class Bird:
  def say(self):
    return 'Chirp'

class Duck(Bird):
  def say(self):
    return 'Quack'

class Rooster(Bird):
  def say(self):
    return 'Cock-a-doodle-do'


# =============================================================================
# Given a superclass Bird with method say(). Create two children classes Duck and Rooster. 
# Override methods say() in such a way that the duck says 'Quack' and a roster says 'Cock-a-doodle-do'.
# =============================================================================

bird = Bird()
print('Bird says:', bird.say())
duck = Duck()
print('Duck says:', duck.say())
rooster = Rooster()
print('Rooster says:', rooster.say())

# Polymorphism task
# =============================================================================
# There is a superclass Figure which represents a parent class for geometric objects. 
# It has a single method area() that should be implemented in children's classes.
# 
# Create three children classes Triangle, Rectangle, and Circle. 
# For each one create a constructor with necessary parameters (three sides lengths for triangle, two sides lengths for rectangle, one radius length for circle) 
# and put these values into private attribute attr as a Python list.
# 
# Override the area() method inside classes to return the appropriate value for each figure type.

# Remember about data validation: check if sides lengths are positive, and for the triangle check the Sides of Triangle rule: 
# for each side, its length must be less than the total length of the other two sides.
# =============================================================================
import math

class Figure:
  def area():
    return None

# implement your classes
class Triangle(Figure):
    def __init__(self, side1, side2, side3):
        sides = [side1, side2, side3]
        self.__attr = []
        for idx, side in enumerate(sides):
            if idx == 0:
                if isinstance(side, int) and side < (sides[1] + sides[2]) and side > 0:
                    self.__attr.append(side)
                else:
                    raise AttributeError('First argument passed to Triangle Class is wrong type or greater than the other two sides combined')
                    
            if idx == 1:
                if isinstance(side, int) and side < (sides[0] + sides[2]) and side > 0:
                    self.__attr.append(side)
                else:
                    raise AttributeError('Second argument passed to Triangle Class is wrong type or greater than the other two sides combined')
                    
            if idx == 2:
                if isinstance(side, int) and side < (sides[0] + sides[1]) and side > 0:
                    self.__attr.append(side)
                else:
                    raise AttributeError('Third argument passed to Triangle Class is wrong type or greater than the other two sides combined')
    
    def area(self):
        p = sum(self.__attr) / 2
        return (p * (p - self.__attr[0]) * (p - self.__attr[1]) * (p - self.__attr[-1])) ** 0.5
            
            

class Rectangle(Figure):
    def __init__(self, side1, side2):
        sides = [side1, side2]
        self.__attr = [x for x in sides if isinstance(x, int) and x > 0]
        print(self.__attr)
        if len(self.__attr) != 2:
            raise AttributeError('Value(s) passed to function are either negative or not an integer')
    
    def area(self):
        return self.__attr[0] * self.__attr[1]

# Default argument for Circle
class Circle(Figure):
    def __init__(self, radius = 5):
        self.__attr = [x for x in [radius] if isinstance(x, int) and x > 0]
        if len(self.__attr) != 1:
            raise AttributeError('Value passed to Circle class not an integer or negative')
    
    def area(self):
        return math.pi * (self.__attr[0] ** 2)


r = Rectangle(12, 4)
print('Rectangle area:', r.area())

bad_r = Rectangle(-3, 4) # Value(s) passed to function are either negative or not an integer

t = Triangle(3, 4, 5)
print('Triangle area:', t.area())

side_too_big = Triangle(3, 5, 9) # Third argument passed to Triangle Class is wrong type or greater than the other two sides combined

c = Circle(6)
print('Circle area:', c.area())













