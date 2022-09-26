##################################################
# DIST PLOT
#
# You'll learn:
# 
# - Plot the distribution of a variable
#     - plot histogram in seaborn
#     - plot KDE (density plot)
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
import seaborn as sns






#============
# IMPORT DATA
#============
country_data = pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/country_data.csv', index_col = 'country_code')
supercars = pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/supercars.csv')
bank= pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/bank.csv')



#=====================
# BASIC HISTOGRAM PLOT w/KDE Probability per x-axis included
#=====================
sns.set_style("dark")
sns.distplot(supercars.top_speed, bins=30)



#---------------------------
# REMOVE KERNEL DENSITY LINE
#---------------------------
sns.distplot(supercars.top_speed, bins=30, kde = False)



#-------------
# CHANGE COLOR
#-------------
sns.distplot(supercars.top_speed
             ,bins=30
             ,kde = False
             ,color = 'navy'
             )



#======================
# CHANGE NUMBER OF BINS
#======================

# REMOVE KERNEL DENSITY LINE
sns.distplot(supercars.top_speed
             ,bins=10
             ,kde = False
             )




#END