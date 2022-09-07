####################################################
# FILTER
#
# How to ...
#   - use the .filter() method
#   - retrieve specific columns from a dataframe
#   - retrieve single columns
#   - retrieve multiple columns
#   - retrieve columns based on regular expressions
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
import pandas as pd



#============
# IMPORT DATA
#============
supercars = pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/supercars.csv')



#-----------------
# DATA INSPECTION
#-----------------

# get first few records
supercars.head()
supercars.columns



# get dimenstions
supercars.shape  # number of rows and columns




#----------------------------------------------------
# "FILTER" the dataframe to retrieve specific columns
#----------------------------------------------------

# get the names of the supercars dataframe
supercars.columns


# FILTER to retrieve one column
supercars.filter(['make'])


# Retrieve multiple columns
supercars.filter(['make','year'])



# The order of the variable selection matters
supercars.filter(['year','make'])



#--------------------------
# RETRIEVE COLUMNS BY REGEX
#--------------------------

# Retrieve columns that start with 'm' or 'd'
supercars.filter(regex = '^m')
supercars.filter(regex = '^d')



# Retrieve columns that contain an 'a'
supercars.filter(regex = 'a')


#EOF