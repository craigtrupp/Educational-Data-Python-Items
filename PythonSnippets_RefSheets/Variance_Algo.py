#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 14:07:02 2022

@author: craigrupp
"""

test_set = [82,51,144,84,120,148,148,108,160,86]

def variance_stdv(lst):
    """
    Return Variance and Stdv : Variance Algorithm Outputs
    Arguments:
        lst : list of integers to pass to function
    Returns:
        Variance & Stddeviation
    """
    import math
    mean = round(sum(lst)/len(lst),2)
    squared_differences = [round((x - mean)** 2, 2) for x in lst]
    variance = round(sum(squared_differences)/(len(lst) - 1),2)
    std_dev = round(math.sqrt(variance),2)
    return mean, squared_differences, variance, std_dev;

print(variance_stdv(test_set))
