##################################################
# GROUP BY
#
# You'll learn:
# 
# - How to use the Pandas .groupby()
#     - How to group by a single variable
#     - How to group by multiple variables
#     - How to aggregate your data
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



#============
# IMPORT DATA
#============
supercars = pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/supercars.csv')
bank = pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/bank.csv')


#-----------------
# DATA INSPECTION
#-----------------

# get first few records
supercars.head()
supercars.columns





###################################################
# GROUP BY
# - groupby() groups your data (i.e., aggregates)
#   by a given variable
#
###################################################


#-------------------------------------------
# aggregate (i.e., group) the supercars data
#  by the "decade" variable using groupby()
#-------------------------------------------

supercars_group_decade = supercars.groupby('decade')


# CALCULATE STATISTICS
supercars_group_decade.mean()
supercars_group_decade.median()
supercars_group_decade[['torque', 'top_speed']].agg(['min', 'max'])
# Subset Dataframe and columns not included in groupby have agg methods applied
supercars[['model', 'year', 'torque', 'top_speed']].groupby(['model', 'year']).agg(['mean', 'max'])


#===============================
# Bank data example
#===============================

bank.head()
bank.columns



#--------------------------------------
# Calculate median metrics by 'marital'
#--------------------------------------
bank_grp_marital = bank.groupby('marital')

bank_grp_marital.median()



#------------------------------------------------------
# Calculate median metrics by 'marital' AND 'education'
#------------------------------------------------------

bank_grp_marital_ed = bank.groupby(['marital', 'education'])

bank_grp_marital_ed.median()






# EOF