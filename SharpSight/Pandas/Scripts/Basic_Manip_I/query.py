#################################################
# QUERY AND RETURN SPECIFIC ROWS
#
# How to ...
#   - Query a dataframe to return specific rows
#   - query based on simple conditions
#   - query based on "compound" logical conditions
#
#
# © Copyright Sharp Sight, Inc.
# sharpsightlabs.com
# All rights reserved
#
#################################################


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




############################################
# QUERY
# - query() subsets your data and
#   keeps rows matching specific criteria
#
############################################


#------------------------------------------
# "query" the rows of the supercars dataset
# - here we are essentially retrieving
#   subsets of the data
#---------------------------------------

# query()
supercars.query('horsepower > 300')



#--------------------------------------------
# Query based on factor or character variable
#--------------------------------------------
supercars.query("decade == '2010s'")
supercars.decade.value_counts()


#-------------------------------------
# Query on multiple conditions
# - Use logical operators like 
#   '&' and '|' to combine conditions
#-------------------------------------


#AND
supercars.query('horsepower > 300').query('decade == "2010s"')
supercars.query('(horsepower > 300) & (decade == "2010s")')

#OR
supercars.query('(horsepower > 300) | (decade == "2010s")')



#-----------------------------------
# Query on multiple character values
#-----------------------------------
supercars.query("make in ['Bugatti', 'Porsche']")
supercars.make.unique()
len(supercars['make'])


#EOF
