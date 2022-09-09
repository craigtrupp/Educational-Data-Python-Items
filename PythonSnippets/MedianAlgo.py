#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 13:04:11 2022

@author: craigrupp
"""
# Fun Python Snippet today while in the SQL course that is a Medians Algorithm 
median_arr = [1,2,3,4,5,6,7,8,9,10,11,12,13]
median_value = int(((len(median_arr) + 1) / 2))
print(median_value, median_arr[5:8], median_arr[median_value-2:median_value+1])
print([1,2,3,4,5,6,7,8,9,10,11,12,13], len([1,2,3,4,5,6,7,8,9,10,11,12,13]))
# Value needs to be turned into int and zero indexing taken into consideration (median_value - 1) to index in likely subsequent list
# Random Int Generator
import random as rd
import numpy as np
#Generate 1-100 with 13 numbers
random_ints = []
np_random_ints = []
for i in range(14):
    random_ints.append(rd.randint(1,100))
for j in range(13):
    np_random_ints.append(np.random.randint(1, 100))
print(random_ints, '\n', np_random_ints)
random_ints.sort()
random_ints
len(random_ints)

def returnMedian(lst):
    """ 
    Returns Median Value of passed list similarly to Median Algorithm for SQL query below
    Validates if passed list is odd/even 
    Function requires a list of integer numeric types
    Arguments:
        lst : list of integers to pass to function
    Returns:
        Original List, Sorted List, Median Index Value if Odd (Zero Indexing Accounted For), Median Value of Passed List
    """
    if len(lst) % 2 != 0:
        # Account for zero indexing 
        # sorted_list = lst.sort() wouldn't work as the array method returns a nonetype and mutates the list in place
        sorted_list = sorted(lst)
        median_index = int((len(lst) + 1) / 2) - 1
        return (lst, sorted_list, median_index, sorted_list[median_index])
    else:
        sorted_list = sorted(lst)
        median_first_value = int((len(sorted_list) / 2) - 1)
        median_second_value = int(len(sorted_list) / 2)
        median_value = (sorted_list[median_first_value] + sorted_list[median_second_value]) / 2
        return (lst, sorted_list, median_value)

print(returnMedian(np_random_ints))
print(returnMedian([1,2,3,4,5,6]))
print(returnMedian(random_ints))
print(returnMedian([82,51,144,84,120,148,148,108,160,86]))
# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)
cars
print([1,2,3,2,1].sort())
