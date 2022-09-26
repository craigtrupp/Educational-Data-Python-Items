######################################################
# FACET GRID
#
# You'll learn:
# 
# - How to use the seaborn.FacetGrid() function
# - How to create "small multiple" charts with seaborn
#     - AKA trellis plots
#     - AKA grid chart
#
#
# © Copyright Sharp Sight, Inc.
# sharpsightlabs.com
# All rights reserved
#
######################################################



#----------------
# IMPORT PACKAGES 
#----------------
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt



#---------------
# SET FORMATTING
#---------------
sns.set_style("dark")



#----------------
# IMPORT DATASETS
#----------------
supercars = pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/supercars.csv')
bank= pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/bank.csv')
stocks = pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/stocks.csv')


#--------
# INSPECT
#--------
stocks.head()
supercars.columns



#-------------------------
# PLOT SOLO CHART
# - use this for reference
#-------------------------

plt.hist(x = bank.age)




#================
# SINGLE ROW GRID
#================
grid_layout = sns.FacetGrid(bank, col = 'education')
grid_layout.map(plt.hist, 'age')



#===================
# SINGLE COLUMN GRID
#===================
grid_layout = sns.FacetGrid(bank, col = 'education', col_wrap = 1)
grid_layout.map(plt.hist, 'age')




#======================================
# CREATE "WRAPPED" SMALL MULTIPLE CHART 
#======================================

grid_layout = sns.FacetGrid(bank, col = 'job', col_wrap = 3)
grid_layout.map(plt.hist, 'age')



#===========================
# CREATE SMALL MULTIPLE WITH 
#   2-VARIABLE GRID LAYOUT
#===========================

grid_layout = sns.FacetGrid(bank, col = 'marital', row = 'education')
grid_layout.map(plt.hist, 'age')




#END