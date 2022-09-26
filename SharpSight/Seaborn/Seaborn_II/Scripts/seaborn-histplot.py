##################################################
# HISTPLOT
#
# You'll learn:
# 
# - Plot the histogram of a variable with Seaborn
# – Change the number of bins
# – Change the color
# – Add a KDE line
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
import matplotlib.pyplot as plt
import seaborn as sns



#============
# IMPORT DATA
#============
country_data = pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/country_data.csv', index_col = 'country_code')
supercars = pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/supercars.csv')
bank= pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/bank.csv')


#--------------------
# SET PLOT FORMATTING
#--------------------
plt.style.use('fivethirtyeight')



#---------------------
# BASIC HISTOGRAM PLOT
#---------------------

# WITHOUT PARAMETERS
sns.histplot(supercars.top_speed)


# USING PARAMETERS
sns.histplot(data = supercars
             ,x = 'top_speed'
             )


#-------------
# CHANGE COLOR
#-------------
sns.histplot(data = supercars
             ,x = 'top_speed'
             ,color = 'navy'
             )


#----------------------
# CHANGE NUMBER OF BINS
#----------------------
sns.histplot(data = supercars
             ,x = 'top_speed'
             ,bins = 10
             )


#----------------------------
# CHANGE TRANSPARENCY (Alpha)
#----------------------------
sns.histplot(data = supercars
             ,x = 'top_speed'
             ,alpha = 0.5
             ,color = 'red'
             )


#-------------
# ADD KDE LINE
#-------------
sns.histplot(data = supercars
             ,x = 'top_speed'
             ,kde = True
             )




#END