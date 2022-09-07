##################################################
# BARPLOT
#
# You'll learn:
# 
# - How to make a bar chart
# - How to modify a bar chart
#     - change the color of the bars
#     - remove error bars
# - How to make a "dodged" bar chart
# - How to aggregate data for a bar chart
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
import matplotlib.pyplot as plt



#============
# IMPORT DATA
#============
#supercars = pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/supercars.csv')
bank= pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/bank.csv')



# INSPECT
print(bank)
print(bank.columns)


#=======================
# SET SEABORN FORMATTING
#=======================
sns.set()



#-----------------
# BASIC BAR PLOT
#-----------------

sns.barplot(data = bank, x = 'education', y = 'balance')


#-----------------
# CHANGE BAR COLOR
#-----------------

sns.barplot(data = bank
            ,x = 'education'
            ,y = 'balance'
            ,color = 'aqua'
            )



#------------------
# REMOVE ERROR BARS
#------------------

sns.barplot(data = bank
            ,x = 'education'
            ,y = 'balance'
            ,color = 'aqua'
            ,ci = None
            )



#---------------------
# HORIZONTAL BAR CHART
#---------------------
sns.barplot(data = bank
            ,y = 'education'
            ,x = 'balance'
            )



#-----------------
# DODGED BAR CHART
#-----------------
sns.barplot(data = bank
            ,x = 'education'
            ,y = 'balance'
            ,hue = 'marital'
            )

primary = bank[bank['education'] == 'primary']
secondary = bank[bank['education'] == 'secondary']
tertiary = bank[bank['education'] == 'tertiary']
unknown = bank[bank['education'] == 'unknown']
primary.head(1), secondary.head(1)
# =============================================================================
# shape mismatch: objects cannot be broadcast to a single shape
# fg, ax = plt.subplots()
# ax.bar(primary['education'], bank['balance'], label='primary')
# ax.bar(secondary['education'], secondary['balance'], label='secondary', bottom=primary['balance'])
# ax.bar(tertiary['education'], tertiary['balance'], label='tertiary', bottom=secondary['balance'])
# ax.bar(primary['unknown'], bank['unknown'], label='unknown', bottom=tertiary['balance'])
# =============================================================================



#================================
# CREATE CHART OF AGGREGATED DATA
# - median balance by education
#================================


#--------------------------
# CREATE AGGREGATED DATASET
#--------------------------

bank_median_by_ed = (bank
 .groupby('education')
 .agg('median')
 .reset_index()
 )
  

# INSPECT
print(bank_median_by_ed)
print(bank_median_by_ed.columns)



#---------------
# PLOT BAR CHART
#---------------

sns.barplot(data = bank_median_by_ed
            ,x = 'education'
            ,y = 'balance'
            ,color = 'aqua'
            )
plt.xlabel("Education")
plt.ylabel("Median Balance")



#END