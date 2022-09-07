###########################################
# Pandas .loc
#
# How to ...
#  - use the .loc[] method
#  - retrieve data by index
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
# LOC
#=========

# SELECT SINGLE CELL (loc)
country_data.loc['JPN' , 'country']


# SELECT SINGLE ROW OF DATA (loc)
country_data.loc['JPN' , :]


# SELECT SINGLE COLUMN OF DATA (loc)
country_data.loc[: , 'country']


# SELECT SLICE OF ROWS (loc)
country_data.loc['JPN':'GBR' , :]


# SELECT SLICE OF COLUMNS (loc)
country_data.loc[: , 'country':'population']


# SELECT SLICE OF CELLS (loc)
country_data.loc['JPN':'GBR' , 'country':'population']



# END