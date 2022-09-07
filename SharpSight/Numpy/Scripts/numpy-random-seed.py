###########################################
# Numpy Random Seed
#
# How to ...
#   - use the np.random.seed() function
#   - set the seed and initialize 
#     Numpy random functions
#
#
# © Copyright Sharp Sight, Inc.
# sharpsightlabs.com
# All rights reserved
#
###########################################


#----------------
# IMPORT PACKAGES
#----------------
import numpy as np



#------------------------------------------
# SET SEED AND GENERATE RANDOM INTEGERS
# - notice that the output is the same
#   every time we run the "random" function
#   with the same seed
#------------------------------------------

np.random.seed(0)
np.random.randint(size = 4, low = 1, high = 10)


# RUN CODE AGAIN
np.random.seed(0)
np.random.randint(size = 4, low = 1, high = 10)


# RUN CODE AGAIN
np.random.seed(0)
np.random.randint(size = 4, low = 1, high = 10)



#-----------------------------------------
# SET *DIFFERENT* SEED 
#  AND GENERATE RANDOM INTEGERS
# - notice that the output is *different*
#   from the previous seed
# - but the output is the same every time
#   we use the same seed
#-----------------------------------------

np.random.seed(77)
np.random.randint(size = 4, low = 1, high = 10)


# RUN CODE AGAIN
np.random.seed(77)
np.random.randint(size = 4, low = 1, high = 10)


# RUN CODE AGAIN
np.random.seed(77)
np.random.randint(size = 4, low = 1, high = 10)


# END