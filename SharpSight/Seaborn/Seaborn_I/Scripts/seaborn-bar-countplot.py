##################################################
# COUNT PLOT (i.e. BAR CHART of counts)
#
# You'll learn:
# 
# - How to make a bar chart of counts
# - How to modify a bar chart
#     - change the color of the bars
#     - change the width of the bars
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
supercars = pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/supercars.csv')
bank= pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/bank.csv')



#=======================
# SET SEABORN FORMATTING
#=======================
sns.set_theme()



#-----------------
# BASIC COUNT PLOT
#-----------------
sns.countplot(data = bank
            ,x = 'education'
            )


#-----------------
# CHANGE BAR COLOR
#-----------------

# 'named' color
sns.countplot(data = bank
            ,x = 'education'
            ,color = 'darkred'
            )


# hex color
sns.countplot(data = bank
            ,x = 'education'
            ,color = '#20DFDF'
            )



#----------------------------
# CREATE HORIZONTAL BAR CHART
#----------------------------
sns.countplot(data = bank
            ,y = 'job'
            ,color = 'darkred'
            )



#-------------------
# SORT BARS BY COUNT
#-------------------
print(bank['job'].value_counts(ascending=False))
sns.countplot(data = bank
            ,y = 'job'
            ,color = 'darkred'
            ,order = bank['job'].value_counts(ascending=True).index
            )
print(bank['job'].value_counts().index)
print(supercars.head(2))
print(supercars.info())







#END