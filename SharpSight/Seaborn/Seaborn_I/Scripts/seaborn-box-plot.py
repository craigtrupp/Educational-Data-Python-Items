##################################################
# SEABORN BOXPLOTS
#
# You'll learn:
# 
# - How to make box plots with Seaborn
# - How to change the color of the boxes
# - How to make a horizontal boxplot
# - How to change the width of the bars
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
#country_data = pd.read_csv('https://learn.sharpsightlabs.com/wp-content/datasets/pdm/country_data.csv', index_col = 'country_code')
supercars = pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/supercars.csv')
bank= pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/bank.csv')



# INSPECT
print(supercars)
supercars.columns


#----------------
# SET PLOT FORMAT
#----------------
sns.set()


#===============
# SIMPLE BOXPLOT
#===============

sns.boxplot(data = bank
            ,x = 'marital'
            ,y = 'age'
            )



#==============================
# CHANGE THE COLOR OF THE BOXES
#==============================

sns.boxplot(data = bank
            ,x = 'marital'
            ,y = 'age'
            ,color = 'aqua'
            )



#==========================
# MAKE A HORIZONTAL BOXPLOT
#==========================

#--------------------------
# VERTICAL 
# NOTE: WE CAN'T READ THIS!
#--------------------------
sns.boxplot(data = bank
            ,x = 'job'
            ,y = 'age'
            )


#-----------
# HORIZONTAL
#-----------
sns.boxplot(data = bank
            ,x = 'age'
            ,y = 'job'
            ,orient = 'h'
            )



#=============================
# CHANGE THE WIDTH OF THE BARS
#=============================

sns.boxplot(data = bank
            ,x = 'marital'
            ,y = 'age'
            ,color = 'aqua'
            ,width = .5
            )



#==========================
# CREATE A 'DODGED' BOXPLOT
#==========================

sns.boxplot(data = bank
            ,x = 'marital'
            ,y = 'age'
            ,hue = 'education'
            )

sns.boxplot(data=bank
            , x='age'
            , y='marital'
            , hue='education'
            , orient='h'
            , width=.5)


# END