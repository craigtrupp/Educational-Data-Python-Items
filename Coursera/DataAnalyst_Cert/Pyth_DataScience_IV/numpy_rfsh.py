#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 13:26:19 2022

@author: craigrupp
"""

# Create a python list

a = ["0", 1, "two", "3", 4]


# Print each element

print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

import numpy as np
print(np.__version__)

a = np.array([0, 1, 2, 3, 4])
a
type(a)
a.dtype


#Slicing Steps
arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5:2])


# Event Elements
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Enter your code here
print(arr[1::2])
print(arr[1:arr.size:2])


# Find (size, dimension, shape for b)
b = np.array([10, 20, 30, 40, 50, 60, 70])

print([b.size, b.ndim, b.shape])

# Stat Functions
a = np.array([1, -1, 1, -1])

a.mean()
a.std()
a.max()
a.min()


# Find the sum of maximum and minimum value in the given numpy array
c = np.array([-10, 201, 43, 94, 502])
# Needs copy to not mutate same list pointer
d = c.copy()
d[0] = 10
c
d
sum([c.min(), c.max()])


# Vector operations 
u = np.array([1, 0])
u

v = np.array([0, 1])
v

z = np.add(u, v)
z

u + v


arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

print(arr1+arr2, type(arr1+arr2))
print(np.subtract(arr1, arr2))
print(np.subtract(arr2, arr1))
print(np.multiply(arr1, arr2))
print(np.divide(arr1, arr2))


# Dot Product 
X = np.array([1, 2])
Y = np.array([3, 2])

np.dot(X, Y)
print(f"np dot performs a multipliation of like index values, then adds : {(X[0] * Y[0]) + (X[1] * Y[1])}")


# Create a constant to numpy array

u = np.array([1, 2, 3, -1]) 
u
print(u+1)


# =============================================================================
# A useful function for plotting mathematical functions is linspace. Linspace returns evenly spaced numbers over a specified interval.
# 
# numpy.linspace(start, stop, num = int value)
# =============================================================================
# Makeup a numpy array within [-2, 2] and 5 elements

np.linspace(-2, 2, num=5)
# Makeup a numpy array within [-2, 2] and 5 elements

np.linspace(-2, 2, num=5,dtype='int')


# Make a numpy array within [0, 2π] and 100 elements 

x = np.linspace(0, 2*np.pi, num=100)
print(x)

y = np.sin(x)
print(y)

import time 
import sys
import numpy as np 

import matplotlib.pyplot as plt
%matplotlib inline  

def Plotvec2(a,b):
    ax = plt.axes()# to generate the full window axes
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)#Add an arrow to the  a Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)#Add an arrow to the  b Axes with arrow head width 0.05, color blue and arrow head length 0.1
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)#set the xlim to left(-2), right(2)
    
Plotvec2(np.array([-1,1]), np.array([1,1]))

Plotvec2(np.array([1,1]), np.array([0,1]))


arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

x = arr1[1::2]
x
   
y = arr2[0::2]
y   


# Second Quick Overview Video/Skills Lab 
# =============================================================================
# 2D Numpy
# =============================================================================

a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
a

# Convert to Numpy
A = np.array(a)
print(A)


# Properties
print([A.size, A.ndim, A.shape])

# Access the element on the second row and third column
A[1, 2]

# Access the element on the second row and third column
A[1][2]

# Access the element on the first row and first column
A[0][0]


# Access the element on the first row and first and second columns
A[0][0:2]


# Access the element on the first and second rows and third column
A[0:2, 2]


# =============================================================================
# # Basic Operations
# =============================================================================
# Create a numpy array X
X = np.array([[1, 0], [0, 1]]) 
X

Y = np.array([[2, 1], [1, 2]]) 
Y


# Add X and Y
Z = X + Y
Z

# Multiply two new
Y = np.array([[2, 1], [1, 2]]) 
Y

# Multiply Y with 2
Z = 2 * Y
Z


# We can perform element-wise product of the array X and Y as follows:
Y = np.array([[2, 1], [1, 2]]) 
Y

X = np.array([[1, 0], [0, 1]]) 
X

Z = X * Y
Z


# We can also perform matrix multiplication with the numpy arrays <code>A</code> and <code>B</code> as follows:
A = np.array([[0, 1, 1], [1, 0, 1]])
A

B = np.array([[1, 1], [1, 1], [-1, 1]])
B

Z = np.dot(A,B)
Z


# We use the numpy attribute T to calculate the transposed matrix
C = np.array([[1,1],[2,2],[3,3]])
C
print(C.T)


1
#Quiz
X=np.array([[1,0,1],[2,2,2]]) 
out=X[0,1:3]
out


X=np.array([[1,0],[0,1]])
Y=np.array([[2,1],[1,2]]) 
Z=np.dot(X,Y)
print(Z)

# Np dot fleshed out
T = np.array([[0, 1, 1], [1, 0, 1]])
N = np.array([[1, 1], [1, 1], [-1, 1]])

print(np.dot(T, N))


# Np.Dot type multiplication
# =============================================================================
# ## First Two values use the first row in T and multiply each index in the first T row times their index at the N column (see below)
# ## The resulting array will have 2 rows and 2 columns (each value in the rows for T are multiplied by the two values in their matching index row in N)
# # First Value [0,0] : (T[0,0] = 0 * N[0,0] = 1 == 0) + (T[0,1] = 1 * N[1, 0] = 1 == 1) + (T[0,2] = 1 * N[2,0] = -1 == -1) = 0 + 1 + -1 == 0
# # Second Value [0,1] : (T[0,0]) = 0 * N[0,1] = 1 == 0) + (T[0,1] = 1 * N[1, 1] = 1 == 1) + (T[0,2] = 1 * N[2,1] = 1 == 1 ) = 0 + 1 + 1 == 2
# # Third Value [1,0] : (T[1,0] = 1 * N[0,1] = 1 == 1) + (T[1,1] = 0 * N[1,0] = 1 == 0) + (T[1,2] = 1 * N[2, 0] = -1 == -1) = 1 + 0 + -1 == 0
# # Fourth Value [1,1] : (T[1,0] = 1 * N[1, 1] = 1 == 1) + (T[1,1] = 0 * N[1,1] = 1 == 0) + (T[1,2] = 1 * N[2, 1] = 1 == 1) = 1 + 0 + 1 == 2
## [[0,2], [0, 2]]
# =============================================================================

