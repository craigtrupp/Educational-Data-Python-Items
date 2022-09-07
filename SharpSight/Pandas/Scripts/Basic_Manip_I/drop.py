##################################################
# DROP
#
# You'll learn:
# - How to use the .drop() method
# - How to drop columns from a Pandas dataframe
# - How to drop rows from a Pandas dataframe
#
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



#-------------------
# DROP SINGLE COLUMN
#-------------------
supercars.tail(1)
supercars_temp = supercars.drop(columns = 'engine_size')
supercars_temp.tail(1)


# check
supercars_temp.columns

#Index(['model', 'make', 'year'
#       ,'decade', 'horsepower', 'torque'
#       ,'seconds_0_60', 'top_speed', 'weight']
#       ,dtype='object')


#----------------------
# DROP MULTIPLE COLUMNS
#----------------------

supercars_temp = supercars.drop(columns = ['engine_size', 'weight'])


# check
supercars_temp.columns

#Index(['model', 'make', 'year'
#       ,'decade', 'horsepower', 'torque'
#       ,'seconds_0_60', 'top_speed']
#       ,dtype='object')





#===================
# DROP ROWS BY INDEX
#===================


#---------
# GET DATA
#---------
country_data = pd.read_csv('https://learn.sharpsightlabs.com/wp-content/datasets/pdm/country_data.csv', index_col = 'country_code')


print(country_data)
country_data.tail(n = 7)



#---------------------------
# DROP SINGLE ROW (by index)
#---------------------------
country_data.drop(index = 'SXM', inplace=True) # Note that SXM is missing



#------------------------------
# DROP MULTIPLE ROWS (by index)
#------------------------------
country_data.drop(index = ['SXM','MAF']) # Note that SXM _and_ MAF are missing
country_data.columns
country_data.loc[['SXM', 'TCA'], ['continent', 'gdp']]
country_data.loc[['USA', 'JPN'], ['continent', 'gdp']]
country_data.loc['USA':'JPN', 'country':'gdp']

#EOF