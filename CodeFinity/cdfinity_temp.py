#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 16:36:35 2022

@author: craigrupp
"""

sum([1, 2, 5, 6, 10, 12, 27])/len([1, 2, 5, 6, 10, 12, 27])

# =============================================================================
# import pandas as pd
# import numpy as np
# 
# df = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/INTRO+to+Python/ds_salaries.csv', index_col = 0)
# 
# df = pd.pivot_table(df, index = ['plan','trial'],
#                        values = ['price'],
#                        aggfunc = [np.mean])
# 
# print(df)
# =============================================================================
import numpy as np
arr = np.array([[[5, 7, 8, 2], [13, 15, 16, 18]], [[5, 7, 8, 2], [13, 15, 16, 18]]])
arr.size, arr.shape

a3d = np.array([[[1,2,3,4],
                 [1,2,3,4],
                 [1,2,3,4]],
                [[1,2,3,4],
                 [1,2,3,4],
                 [1,2,3,4]]
                ])
a3d.shape


array  = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
new_array = array.reshape(4, 3)

print(new_array)

Threed_array = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
Threed_array = Threed_array.reshape(2,3,2)
Threed_array

array = np.array([[12, 45, 78, 34, 0], [13, 5, 78, 3, 1]])
new_array = array.reshape(-1)

print(new_array)

array = np.array([[12, 45, 78, 34, 0], [13, 5, 78, 3, 1]])
new_arr = array.flatten()

print(new_array)

array_1 = np.array([54, 6, 23, 1, 6])
array_2 = np.array([12, 67, 94, 2, 8 ])

array = np.concatenate((array_1, array_2))
print(array)

array_1 = np.array([[0, 1, 2], [3, 4, 5]])
array_2 = np.array([[6, 7, 8], [9, 10, 11]])

array = np.concatenate((array_1, array_2), axis=1)
print(array)
print(array_1[0,0], array_1[1, 0])


array_1 = np.array([[0, 1, 2], [3, 4, 5]])
array_2 = np.array([[6, 7, 8], [9, 10, 11]])
array = np.concatenate((array_1, array_2))
print(array, array.shape, array_1.shape, array_2.shape)


array= np.array([19, 40, 37, 4, 7, 7, -2, 5])
x = np.where(array == 7)
print(x, x[0], len(x[0]))

arr = np.array([1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 ])
# Searching the indexes where the values are odd
x = np.where(arr % 2 == 1)

print(x)
[(y, arr[y]) for y in x[0]]

array = np.array([[-2, 4, -12, -434, 62], [1, 4, 7, 93, 75]])
print('Unsorted array : ', array)
print('Sorted array : Smallest to Largest', np.sort(array))
print('Sorted array : Largest to Smallest', -np.sort(-array))


arr = np.array([7, 43, 56, 123, 10, 3])
x = arr.copy()

arr[0] = 42
print(x, arr)

print(arr)
print(x)

import pandas as pd
pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/a43d24b6-df61-4e11-9c90-5b36552b3437/wine.csv', index_col=0).head()


import numpy as np

dataset = {'animal': [np.NaN, 'Dog', np.NaN, 'Cat','Parrot', None],
'name': ['Dolly', None, 'Erin', 'Kelly', None, 'Odie']}
animal = pd.DataFrame(dataset)
# Find missing values
missing_value = animal.isna()
print(missing_value, animal.isnull())



'30 min'.find(' ')
he = '30 min'
he[:he.find(' ')]
'C148'.split(' ')
len('C148'.split(' '))

from datetime import date
bday = date(1990,2,8)
print(bday.day, bday.days)
print(bday.day)

# Importing the Seaborn 
import seaborn as sns
# Importing the matplotlib.pyplot
import matplotlib.pyplot as plt

data_list = ['apple', 'fish', 'milk', 'milk', 'apple', 'apple', 'milk', 'fish', 'fish']
sns.countplot(x=data_list)
plt.show()



