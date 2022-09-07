##################################################
# SEABORN SCATTERPLOT
#
# You'll learn:
# 
# - How to make a simple scatterplot with seaborn
#
# - How to modify your seaborn scatterplots
#     - make the points more transparent
#     - increase the size of the point
#     - create a bubble chart
#     - change the color of the points
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
supercars = pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/supercars.csv')



print(supercars)


#----------------
# INSPECT COLUMNS
#----------------
supercars.columns



#---------------
# SET FORMATTING
#---------------

sns.set()


#==================
# BASIC SCATTERPLOT
#==================

sns.scatterplot( data = supercars
                ,x = 'horsepower'
                ,y = 'top_speed'
                ).set_tile('Horsepower')



#-------------------
# REMOVE POINT EDGES
#-------------------

sns.scatterplot( data = supercars
                ,x = 'horsepower'
                ,y = 'top_speed'
                ,edgecolor = 'none'
                )



#-------------------------------
# CHANGE THE COLOR OF THE POINTS
#-------------------------------

sns.scatterplot( data = supercars
                ,x = 'horsepower'
                ,y = 'top_speed'
                ,edgecolor = 'none'
                ,color = 'red'
                )




#-----------------------------------------
# REDUCE OPACITY OF POINTS
# - i.e., make the points more transparent
#-----------------------------------------

sns.scatterplot( data = supercars
                ,x = 'horsepower'
                ,y = 'top_speed'
                ,edgecolor = 'none'
                ,alpha = .2
                )



#-----------------------------------------
# CHANGE COLOR PALETTE
# - i.e., make the points more transparent
#-----------------------------------------

sns.scatterplot( data = supercars
                ,x = 'horsepower'
                ,y = 'top_speed'
                ,edgecolor = 'none'
                ,hue = 'torque'
                ,palette = "YlOrRd"
                )



#------------------------------
# CHANGE THE SIZE OF THE POINTS
#------------------------------

sns.scatterplot( data = supercars
                ,x = 'horsepower'
                ,y = 'top_speed'
                ,edgecolor = 'none'
                ,s = 7
                )



#-------------
# BUBBLE CHART
#-------------
print(supercars['weight'].sort_values(ascending=False))
# Weight values are set on this with their size 
print(supercars.iloc[1057, :])
sns.scatterplot( data = supercars
                ,x = 'horsepower'
                ,y = 'top_speed'
                ,edgecolor = 'none'
                ,size = 'weight'
                )


sns.scatterplot( data = supercars
                ,x = 'horsepower'
                ,y = 'top_speed'
                ,edgecolor = 'none'
                ,size = 'weight'
                ,sizes = (5,200)
                )





#EOF