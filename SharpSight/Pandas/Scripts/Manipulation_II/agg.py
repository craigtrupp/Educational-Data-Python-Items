##################################################
# AGG
#
# You'll learn:
# 
# - How to "aggregate" your data
# - How to calculate summary statistics
#     - mean
#     - median
#     - min, max
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
bank = pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/bank.csv')




#===========================================================
# AGG
# - agg() "aggregates" data in a dataframe by applying 
#   a given summary statistic 
# - i.e., you provide the statistic, and agg will calculate
#   that statistic
#
#===========================================================


#------------------------------------------------
# Calculate aggregation for all numeric variables
#------------------------------------------------
supercars.info()
supercars.agg('mean')



#------------------------------------
# Calculate supercar horsepower stats
#------------------------------------

# inspect
supercars.head()


# mean
supercars['horsepower'].agg('mean') # 304.6559


# NOTE: Attribute access is discouraged
#supercars.horsepower.agg('mean')
#supercars.horsepower.agg('mean')




# median
supercars['horsepower'].agg('median') # 275

# max
supercars['horsepower'].agg('max')  # 1184

# min
supercars['horsepower'].agg('min')  # 34
print(supercars[['horsepower', 'weight']].agg(['mean']), type(supercars[['horsepower', 'weight']].agg(['mean'])))
supercars[['horsepower', 'weight']].agg(['min', 'max'])
# Series return type can be used with .iloc to return a similar type min 
supercars['horsepower'].sort_values(ascending=True).iloc[0]
# standard deviation
supercars['horsepower'].agg('std')  # 163.01
print(supercars.info())
# Subset dataframe then order based grouping on the make .. then year with those two aggs functions
# Note here is the groupby columns have agg functions run on returned total for non grouped by columns 
print(supercars[['make', 'year', 'horsepower', 'weight']].groupby(['make', 'year']).agg(['mean', 'max']))


#--------------------------------------------------
# Calculate multiple summary stats at the same time
#--------------------------------------------------

supercars['horsepower'].agg(['mean','median'])




#-------------------------------------------
# Calculate multiple summary stats by groups
#-------------------------------------------


bank.groupby(['marital','education']).agg(['mean','median'])
banks = bank.groupby(['marital','education']).agg(['mean','median'])
print(bank.columns)
print(bank['mortgage'].dtypes, bank['mortgage'].head(1))
# EOF