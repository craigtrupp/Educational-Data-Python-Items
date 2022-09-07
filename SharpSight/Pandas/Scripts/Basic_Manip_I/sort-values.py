####################################################
# SORT VALUES
#
# How to ...
#   - use the .sort_values() method
#   - sort the values of a dataframe
#   - sort in ascending order
#   - sort in descending order
#   - re-index the dataframe after sorting
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




#=====================================================
# SORT THE VALUES
#  .sort_values() sorts your data by a given variable
#
#=====================================================

# inspect 
supercars.head()
supercars.top_speed.min() #74
supercars.top_speed.max() #273



#-----------------------------------------------------------
# 1: sort the data by "top_speed" using .sort_values()
#    note: sort_values() sorts in ascending order by default
#-----------------------------------------------------------

supercars.sort_values('top_speed')
supercars.loc[:, ['top_speed', 'model']].sort_values('top_speed').head()
supercars.loc[:, ['top_speed', 'model']].sort_values('top_speed', ascending=False).head()
# Sort by model (Descending), then for same model rows, sort by top_speed in Lowest to HIghest
supercars.loc[:, ['model', 'top_speed']].sort_values(by=['model', 'top_speed'], ascending=[False, True]).head(10)


# Store the sorted data in a new dataframe
supercars_sorted = supercars.sort_values('top_speed')


# inspect
# note: top row has top_speed 74
# - this is the same as the minimum top_speed
#   that we calculated earlier
# - this is a good way to 'check' that
#   .sort_values() worked the way we expected

(supercars_sorted
 .filter(['model', 'top_speed'])
 .head()
 )



#-----------------------------------------------------
# 2: sort the data by "top_speed" using sort_values()
#    in *descending* order(i.e., high to low)
#-----------------------------------------------------


supercars.sort_values('top_speed', ascending = False)


(supercars
 .sort_values('top_speed', ascending = False)
 .filter(['model', 'year', 'top_speed'])
 .head()
 )



#-----------------
# RESET THE INDEX : Update index to have sorted type association with index value
# Common to sort and then reset_index to give index closeness to sorted values
#-----------------

(supercars
 .sort_values('top_speed')
 .reset_index(drop = True)
)



#EOF