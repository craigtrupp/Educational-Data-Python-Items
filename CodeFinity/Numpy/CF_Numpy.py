#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 09:42:28 2022

@author: craigrupp
"""

# Indexing and Slicing
import numpy as np

# Creating array
arr = np.array([13,99,11,23,4,41])

# Multiply the last and the first elements
print(arr[0] * arr[-1])

# Access 2-D and 3-D Arrays

arr = np.array([[6, 5, 7, 8], [65, 2, 7, 9]])

# Getting the fourth element from the first array
fourth_element = arr[0, -1]
# Getting the first element from the second array
first_element = arr[-1, 0]
# Multiplying obtained element
result = fourth_element * first_element
print(result)

# =============================================================================
# fourth_element = arr[0, 3]
# first_element = arr[1, 0]
# Alternate non-negative indexing 
# =============================================================================


# =============================================================================
# You have such an array: [[[-4, 3, 1], [-4, 39, 8]], [[2, -4, 10], [15, 193, 8]]]
# 
# You have to access 10.
# Let's try. Use only negative indexes.
# =============================================================================
arr = np.array([[[-4, 3, 1], [-4, 39, 8]], [[2, -4, 10], [15, 193, 8]]])

# Getting such value as 10 using negative indexing and displaying it
print(arr[-1, -2, -1])

# =============================================================================
# Challenges: Get One Dimensional Array Using Slicing
# Let's look at the syntax of slicing: array[start: end: step] respectively:
# 
# start - the index from which to start slicing.
# end - the index at which the slicing ends.
# step - this parameter determines the increments between the indices.

#You have such an array [12, 5, 87, 9, 44, 12, 6, 0, -2]. You have to get such an array [87, 12, -2]. Use slicing.
# =============================================================================
import numpy as np

# Creating array
arr = np.array([12, 5, 87, 9, 44, 12, 6, 0, -2])

# Getting [87, 12, -2] using slice
print(arr[2::3])
print(arr[-7::3])


# =============================================================================
# You have such an array [[34, 6, 32, 8, 98], [6, 3, 5, 9, 4]].
# 
# You have to get such an array [[34, 6, 32, 8, 98]] using slicing.
# =============================================================================
import numpy as np

# Creating array
arr = np.array([[34, 6, 32, 8, 98], [6, 3, 5, 9, 4]])

# Getting [[34, 6, 32, 8, 98]] using slicing
print(arr[0:1,::])

# Pay attention to the nested array return, slices needed and not indexing!



# =============================================================================
# Challenge: Get One Dimensional Array Using Slice and Only Positive Indexes
# You have such an array [11, 5, 87, 1, 44, 11, 6, 0, -5]. 
# You have to get such an array [87, 11, -5]. Use slice and ONLY POSITIVE indexes.
# =============================================================================
import numpy as np

arr = np.array([11, 5, 87, 1, 44, 11, 6, 0, -5])

# Getting [87, 11, -5] using slicing with positive indexes
print(arr[2:len(arr):3])

# len trick to get to end if unknown length



# =============================================================================
# Challenge: Get One Dimensional Array Using Only Negative Indexes
# You have such an array: [54, 23, 1, 76, 8, 45, 10, 3]. 
# You have to get such an array [76, 8, 45], using array slicing. BUT use only negative indices.
# Had a little fun here and used some like index type finding to get negative start/end indexes and offset the exclusive slice
# =============================================================================

# Creating array
arr = np.array([54, 23, 1, 76, 8, 45, 10, 3])

# Getting [76, 8, 45] using slicing with negative indexes, np.where and grabbing index from returned tuple
start_slice = np.where(arr == 76)[0][0] - len(arr)
end_slice = (np.where(arr == 45)[0][0] - len(arr)) + 1
new_arr = arr[start_slice:end_slice]

# Displaying result
print(start_slice, end_slice)
print(new_arr)




















































