####################################################
# Numpy Zeros
#
# How to ...
#   - use the np.zeros() function
#   - create Numpy arrays with all zeros
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
np.zeros(shape = 3)


# WITHOUT PARAMETER
np.zeros(3)



#====================================
# CREATE 2D ARRAY WITH SPECIFIC SHAPE
#====================================

np.zeros(shape = (2,3))





#=========================
# CREATE ARRAY 
#  WITH SPECIFIC DATA TYPE
#=========================

np.zeros(shape = 3, dtype = int)
np.zeros((2,5), dtype=int)


# check data type
np.zeros(shape = 3, dtype = int).dtype




#END