#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 15:25:00 2022

@author: craigrupp
"""

# OOP Challenge
# =============================================================================
# for stack: Last In First Out, or LIFO (if you add the element, you put it at the end of the list. If you pop the element, you remove it from the ending).
# for queue: First In First Out, or FIFO (if you add the element, you put it at the end of the list. If you pop the element, you remove it from the beginning).
# We will implement these data structures using a Python list.
# 
# To do that, follow the steps:
# 
# Given an abstract superclass List with two methods in it: pop() and push(). pop() removes and returns the element, and push() puts the element to the data structure, but in the List they do nothing. 
# Change the constructor that initializes the public attribute data with an empty Python list.
# Create two classes Stack and Queue that inherit the superclass.
# Implement Stack: override the pop() and push() methods according to the rule LIFO.
# Implement Queue: override the pop() and push() methods according to the rule FIFO.
# Think about what happens if you try to pop an element from the empty data structure.
# Test your classes by creating and using the objects.
# =============================================================================

class List:
    data = None
    def __init__(self):
        self.data = []
    def push(self):
        pass
    def pop(self):
        pass
    
class Stack(List):
    def push(self, value):
        return self.data.append(value)
    def pop(self):
        return self.data.pop()
    
class Queue(List):
    def push(self, value):
        return self.data.append(value)
    def pop(self):
        return self.data.pop(0)



# testing
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print('Pop from stack:', stack.pop())

queue = Queue()
queue.push(10)
queue.push(20)
queue.push(30)
print('Pop from queue:', queue.pop())



[1,2,3].pop