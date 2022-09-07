##################################################
# RENAME
#
# You'll learn:
# 
# - How to rename columns of a dataframe
#
# © Copyright Sharp Sight, Inc.
# sharpsightlabs.com
# All rights reserved
#
##################################################



#----------------
# IMPORT PACKAGES
#----------------
import pandas as pd



#============
# IMPORT DATA
#============
supercars = pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/supercars.csv')



#----------
# GET NAMES
#----------
supercars.columns



#--------------
# RENAME COLUMN
#--------------

supercars_temp = supercars.rename(columns = {'horsepower':'hp'})


# INSPECT
supercars_temp.columns




#--------------
# RENAME COLUMN
#--------------
supercars.rename(columns = {'horsepower':'hp'}, inplace = True)


# INSPECT
supercars.columns
supercars.rename(str.upper, axis='columns')
supercars.index
supercars.rename(str.title, axis='columns')
super_str = supercars.rename(index=str)
super_str.index
super_str.loc['1', ['weight', 'model']]
#NOTE: you can also rename index values with 'index ='

#EOF