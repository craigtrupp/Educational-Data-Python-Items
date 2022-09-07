#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 10:37:39 2022

@author: craigrupp
"""

# =============================================================================
# np.reshape - this function changes the shape of an N-dimensional array in such a way that the total number of elements remains the same.
# np.transpose - this function transpose the array, that is it swaps the axis of the array.
# np.concatenate - this function creates a new array, as follows: add arrays one after another, along the axis which is given by.
# np.resize - this function is designed to resize an array. It creates a copy of the original array with the specified size.
# =============================================================================

import numpy as np

array  = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
new_array = array.reshape(4, 3)

print(new_array)

array  = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
new_array = array.reshape(2, 3, 2)

print(new_array)



# =============================================================================
# Do you know what flattening an array is? What does this mean? 
# This is a transformation of any multidimensional array to one-dimensional. 
# Flattening can be implemented using two different functions, the first of which we already know:
# 
# reshape(-1) function with an argument of -1;
# and the next one is flatten(). Let's take a look at both these functions in practice.
# =============================================================================
array = np.array([[12, 45, 78, 34, 0], [13, 5, 78, 3, 1]])
new_array = array.reshape(-1)

print(new_array)


array = np.array([[12, 45, 78, 34, 0], [13, 5, 78, 3, 1]])
new_arr = array.flatten()

print(new_array)


# =============================================================================
# Another equally important function in working with arrays is array joining. 
# Joining an arrays means making one common array from several arrays, which will contain all the elements from each array. 
# Arrays we concatenate along the axes.
# 
# If the axis = 0 (this is the default value) then this means we concatenate the array by rows.
# If the axis = 1 then this means we concatenate the array by column.
# 
# =============================================================================
array_1 = np.array([54, 6, 23, 1, 6])
array_2 = np.array([12, 67, 94, 2, 8 ])

array = np.concatenate((array_1, array_2))

print(array)
# Can't concatenate against a 1D dimension with the column (or 2D type prompt)
print(np.concatenate((array_1, array_2), axis=1))


array_1 = np.array([[0, 1, 2], [3, 4, 5]])
array_2 = np.array([[6, 7, 8], [9, 10, 11]])

array = np.concatenate((array_1, array_2), axis=1)
print(array_1,'\n', array_2)
print(array)


# =============================================================================
# You have such arrays [[12, 56, 78], [35, 1, 5]] [[8, 65, 3], [1, 2, 3]] You have to get such an array:
# 
# [[12 56 78 8 65 3] [35 1 5 1 2 3]]
# =============================================================================
arr_1 = np.array([[12, 56, 78], [35, 1, 5]])
arr_2 = np.array([[8, 65, 3], [1, 2, 3]])

# Joining array
arr = np.concatenate((arr_1, arr_2), axis=1)

print(arr)



# Searching Arrays
# =============================================================================
# Let's also focus on a very useful function that searches for some value in an array and returns its index. 
# This is a function where(). Let's see how it works in practice. 
# Let's find the indices of the elements, the values of which are equal to 7
# =============================================================================
import numpy as np

array= np.array([19, 40, 37, 4, 7, 7, -2, 5])
x = np.where(array == 7)

print(x, len(x[0]))


# =============================================================================
# You have such an array: [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8].
# 
# Find the indexes where the values are odd.
# =============================================================================

# Creating array
arr = np.array([1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 ])
# Searching the indexes where the values are odd
x = np.where(arr % 2 == 1)

print(x)
print('Odd Values in Arr')
print([arr[odd] for odd in x[0]])


# Sorting Arrays
# =============================================================================
# Now let's move on to sorting arrays. 
# Sorting an array is the allocation of array elements in an ordered sequence(the item can be sorted, for example in descending order, in ascending order, etc).
# Let's try to sort the array:
# =============================================================================
array = np.array([3, -4, 6, 0, 12, 499, -123])

print('unsorted array', array)
print('sorted array', np.sort(array))

# =============================================================================
# It's important to mention that, method sort() returns a copy of the array (original array remains unchanged).
# =============================================================================
array = np.array([[-2, 4, -12, -434, 62], [1, 4, 7, 93, 75]])
print('Unsorted array', array)
print('Sorted array', np.sort(array))



# Copying Arrays
# =============================================================================
# It is worth noting that there are many methods in the NumPy for duplicating arrays. 
# Here we will consider one of them, namely: copy().
# =============================================================================
arr = np.array([7, 43, 56, 123, 10, 3])
x = arr.copy()

arr[0] = 42

print(arr)
print(x)

# =============================================================================
# You have such an array [12, 56, 78, 65, 1, 5]. 
# You need to use the right method in order to eventually get the following arrays
# arr_1 = [11, 56, 78, 0, 1, 5] arr_2 = [12, 56, 78, 65, 1, 5]. 
# For it you have to replace element 12 with 11, and element 65 with 0
# =============================================================================


arr_1 = np.array([12, 56, 78, 65, 1, 5])
# Copying array
arr_2 = arr_1.copy()

# Replacing elements
arr_1[0] = 11
arr_1[np.where(arr_1 == 65)[0][0]] = 0

print(arr_1)
print(arr_2)






