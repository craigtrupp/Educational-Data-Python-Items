####################################################
# Numpy Full
#
# How to ...
#   - use the np.full() function
#   - create Numpy arrays that are filled
#     with the same value in every cell
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
np.full(shape = 3, fill_value = 7)


# WITHOUT SHAPE PARAMETER
np.full(3, fill_value = 7)



#====================================
# CREATE 2D ARRAY WITH SPECIFIC SHAPE
#====================================

np.full(shape = (2,3), fill_value = 7)





#=========================
# CREATE ARRAY 
#  WITH SPECIFIC DATA TYPE
#=========================

np.full(shape = 3, fill_value = 7, dtype = float)


# check data type
np.full(shape = 3, fill_value = 7, dtype = float).dtype




#END