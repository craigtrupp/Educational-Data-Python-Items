###########################################
# Pandas .iloc
#
# How to ...
#  - use the .iloc[] method
#  - retrieve data by integer index
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
import pandas as pd



#------------------
# GET DATA FROM URL
#------------------
country_data = pd.read_csv('https://learn.sharpsightlabs.com/wp-content/datasets/pdm/country_data.csv', index_col = 'country_code')

print(country_data )



#=========
# ILOC
#=========

# SELECT SINGLE CELL (iloc)
country_data.iloc[2 , 0]



# SELECT SINGLE ROW OF DATA (iloc)
country_data.iloc[2 , :]



# SELECT SINGLE COLUMN OF DATA (iloc)
country_data.iloc[: , 1]



# SELECT SLICE OF ROWS (iloc)
country_data.iloc[2:4 , :]



# SELECT SLICE OF COLUMNS (iloc)
country_data.iloc[: , 1:4]



# SELECT SLICE OF CELLS (iloc)
country_data.iloc[1:4 , 1:4]





# END