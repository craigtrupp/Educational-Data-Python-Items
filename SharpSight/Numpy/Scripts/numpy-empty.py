####################################################
# Numpy Empty
#
# How to ...
#   - use the np.empty() function
#   - create "empty" Numpy arrays 
#     i.e., arrays with "arbitrary" values
#
#
# © Copyright Sharp Sight, Inc.
# sharpsightlabs.com
# All rights reserved
#
####################################################


#----------------
# IMPORT PACKAGES
#----------------
import numpy as np



#================
# CREATE 1D ARRAY
#================

# WITH PARAMETER
np.empty(shape = 3)


# WITHOUT PARAMETER

np.empty(3)



#====================================
# CREATE 2D ARRAY WITH SPECIFIC SHAPE
#====================================

np.empty(shape = (2,3))





#=========================
# CREATE ARRAY 
#  WITH SPECIFIC DATA TYPE
#=========================

np.empty(shape = 3, dtype = int)


# check data type
np.empty(shape = 3, dtype = int).dtype

np.empty(shape=(3,1), dtype=int)



#END