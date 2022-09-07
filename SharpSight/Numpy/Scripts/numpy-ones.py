####################################################
# Numpy Ones
#
# How to ...
#   - use the np.ones() function
#   - create Numpy arrays with all ones
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
np.ones(shape = 5)


# WITHOUT PARAMETER
np.ones(5)



#====================================
# CREATE 2D ARRAY WITH SPECIFIC SHAPE
#====================================

np.ones(shape = (2,3))





#=========================
# CREATE ARRAY 
#  WITH SPECIFIC DATA TYPE
#=========================

np.ones(shape = 3, dtype = int)
np.ones(shape=(4,2))


# check data type
np.ones(shape = 3, dtype = int).dtype




#END