##################################################
# HEATMAP
#
# You'll learn:
# 
# - How to make a heatmap with seaborn
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



# INSPECT
print(bank)
print(bank.columns)


#=======================
# SET SEABORN FORMATTING
#=======================
sns.set()



#===============
# AGGREGATE DATA
#===============

bank_meanbal_ed_by_marital = (bank
  .groupby(['education','marital'])
  .agg('mean')  
  .filter(['balance'])
  .reset_index()
  .pivot('education', 'marital', 'balance')
)
# Here is the groupby dataframe we are ultimately turning into a heat map
print(bank.groupby(['education', 'marital']).agg('mean'))
# Only use one agg statistic column : balance (must pass even single column in a list) 
print(bank.groupby(['education', 'marital']).agg('mean').filter(['balance']))
# reset index prior to creating pivot table
print(bank.groupby(['education', 'marital']).agg('mean').filter(['balance']).reset_index())
# pivot table (rows : education , col = marital status and agg value for pairs is balance)
print(bank.groupby(['education', 'marital']).agg('mean').filter(['balance']).reset_index().pivot('education', 'marital', 'balance'))

print(bank_meanbal_ed_by_marital)






#===============
# CREATE HEATMAP
#===============


sns.heatmap(data = bank_meanbal_ed_by_marital)






#END