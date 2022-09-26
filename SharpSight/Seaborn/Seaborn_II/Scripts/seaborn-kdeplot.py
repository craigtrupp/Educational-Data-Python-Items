##################################################
# KDE PLOT
#
# You'll learn:
# 
# - How to create a density plot of a variable
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
import numpy as np



#=======================
# SET SEABORN FORMATTING
#=======================
sns.set()



#============
# IMPORT DATA
#============
country_data = pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/country_data.csv', index_col = 'country_code')
supercars = pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/supercars.csv')
bank= pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/bank.csv')



#===================
# BASIC DENSITY PLOT
#===================

sns.kdeplot(supercars.top_speed)


#-----------------------------
# CHANGE THE COLOR OF THE LINE
#-----------------------------

sns.kdeplot(supercars.top_speed, color = 'red')



#----------------------------------
# CHANGE THE SMOOTHNESS OF THE LINE
#----------------------------------

sns.kdeplot(supercars.top_speed, bw = 1)



#------------
# ADD SHADING
#------------

sns.kdeplot(supercars.top_speed, shade = True)



#===========================
# 2 DIMENSIONAL DENSITY PLOT
#===========================

x_var = np.random.normal(size = 100)
y_var = x_var + np.random.normal(size = 100, loc = 0, scale = 5)
print(list(zip(x_var[:10], y_var[:10])))

subset = list(zip(x_var[:10], y_var[:10]))
x_subsets = [x[0] for x in subset]
y_subsets = [x[1] for x in subset]
print(x_subsets, '\n', y_subsets)
# Confirm the separated zip objets can be passed to seaborn
print(subset)

# Subset 2D KDE plot
sns.kdeplot(x_subsets, y_subsets, shade=True)

# Total
sns.kdeplot(x_var,y_var)



#========================
# SHADE THE  PLOT
# - i.e. fill in the plot 
#   with color
#========================

sns.kdeplot(x_var,y_var, shade = True)



# END