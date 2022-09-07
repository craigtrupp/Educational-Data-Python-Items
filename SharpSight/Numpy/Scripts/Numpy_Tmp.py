#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 14:37:07 2022

@author: craigrupp
"""

import numpy as np
print(np.array([1,2,3]))
print(type(np.array([1,2,3])))

#Set Dtype
np_float = np.array([1,2,3], dtype=float)
print(np_float)


# Popular attributes
print(np_float.size, np_float.shape, np_float.dtype, np_float.ndim)

np_int = np.array([[0,1,2], [3,4,5]])
np_shape, np_size = np_int.shape, np_int.size
print(np_shape, np_size, np_int.ndim)
print(np_int.sum(), np_int.sum(axis=1), np_int.sum(axis=0))
print(np_int.mean())
print(np_int.concat([6,7,8]))
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
print(np.concatenate((a,b)), a.shape, b.shape)
print(np.concatenate((a,b.T), axis=1))


# (3,4) np array shape
practice_np = np.array([[7,2,3,4], [5,6,14,8], [9,10,11,12]]) 
practice_np
print(practice_np.shape, practice_np.ndim, practice_np.size)
# agg func, axis=1 will do the row (or array), axis=0 will do the column (same column (array index) spot for agg summary performed on all arrays) no argument takes entire dataset
print(practice_np.mean(axis=1), practice_np.mean(), practice_np.mean(axis=0))
print(practice_np.sum(axis=1), practice_np.sum(), practice_np.sum(axis=0))
# default (axis not provided) = sort array at row index (so whole array), axis=0 will similarly sort nested column value and potentially be placed in new row
print(np.sort(practice_np), '\n\n', np.sort(practice_np, axis=0), '\n')
#print([x for x in [y for y in practice_np]])


