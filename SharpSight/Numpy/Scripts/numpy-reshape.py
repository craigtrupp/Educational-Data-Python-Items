#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 13:19:01 2022

@author: craigrupp
"""

import numpy as np


# =============================================================================
# CREATE 1D ARRAY - Using NP .reshape as a function of Numpy
# =============================================================================
array_1d = np.arange(start=1, stop=7)


# =============================================================================
# RESHAPE : (2,3) Using NP .reshape as a function of Numpy
# =============================================================================

array_rs = np.reshape(array_1d, (2,3))


print(array_rs)
# =============================================================================
# USE RESHAPE AS A METHOD
# =============================================================================
print(array_1d)

print(array_1d.reshape((3,2)))


# =============================================================================
# np function call requires the array to be passed, if using the reshape method, 
# it can be chained on from the variable holding the array
# =============================================================================
