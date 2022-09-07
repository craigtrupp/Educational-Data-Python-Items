####################################################
# ASSIGN
#
# How to ...
#   - use the .assign() method
#   - add new variables to a dataframe
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



#=======================================
# "Assign" a new column to the dataframe
#=======================================


#--------------------------
# ADD VARIABLE: hp_per_ton
# - i.e. horsepower per ton
#--------------------------

supercars.assign(hp_per_ton = supercars.horsepower / supercars.weight)


# INSPECT
supercars.columns


# CHECK
(supercars
 .assign(hp_per_ton = supercars.horsepower / supercars.weight)
 .filter(['horsepower', 'weight', 'hp_per_ton'])
 )



#--------------------------------------------------
# note: - using assign does not change the original
#         data frame
#       - .assign() returns a copy!
#--------------------------------------------------

supercars.columns



#----------------------------------
# To 'save' this new variable
# we need to save the new dataframe
#----------------------------------

supercars_new = supercars.assign(hp_per_ton = supercars.horsepower / supercars.weight)



#-------------------------------------------------
# Inspect
# - notice that hp_per_ton is in the new dataframe
#-------------------------------------------------

supercars_new.head()
supercars_new.columns





#EOF