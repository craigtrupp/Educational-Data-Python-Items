##################################################
# MELT
#
# You'll learn:
# 
# - How to use the .melt() method
# - How to reshape your data from wide to long
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



#---------
# GET DATA
#---------

revenue_wide = pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/revenue_wide.csv')



# INSPECT
print(revenue_wide)

revenue_wide.columns
revenue_wide.head(2)
[revenue_wide.melt('region', ['Q1', 'Q2']), revenue_wide.melt('region', ['Q1', 'Q2']).index]

#-----------------------
# MELT
# - reshape wide to long
#-----------------------

revenue_wide
#region : column that contains values (Europe & North America) that will identify the rows in the new column
revenue_wide.melt(id_vars = ['region']
                  ,value_vars = ['Q1','Q2']
                  )

revenue_wide.melt(id_vars=['region'], value_vars=['Q1'], value_name='revenue', var_name='quarter')


# ADD NAME TO 'VALUE' VARIABLE
revenue_wide.melt(id_vars = ['region']
                  ,value_vars = ['Q1','Q2']
                  ,value_name = 'revenue'
                  )



# ADD NAME TO 'VARIABLE' VARIABLE
# Original two rows in wide dataframe takes the region as the identifier 
# Moves the values in Q1 and Q2 column of wide dataframe into their own row
# Generally think of data spread over time series put into rows with a context of what that value is
revenue_wide
revenue_wide.melt(id_vars = ['region']
                  ,value_vars = ['Q1','Q2']
                  ,value_name = 'revenue'
                  ,var_name = 'quarter'
                  )




#END