##################################################
# CONCAT
#
# You'll learn:
# 
# - How to 'concatenate' multiple dataframes
#     - i.e. how to combine dataframes vertically
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
import numpy as np




#------------------
# CREATE DATAFRAMES
#------------------

revenue_EU_NA_Q1Q2 = pd.DataFrame({'region':['Europe', 'Europe', 'North America', 'North America']
                            ,'quarter':['Q1','Q2','Q1','Q2']
                            ,'revenue':[65000,62000,60000,63000]
                            })



revenue_world_Q3Q4 = pd.DataFrame({'region':['Europe', 'Europe', 'North America', 'North America','South America','South America','Asia','Asia']
                            ,'quarter':['Q3','Q4','Q3','Q4','Q3','Q4','Q3','Q4']
                            ,'revenue':[61000,65000,73000,74000,72000,69000,69000,np.nan]
                            })


# INSPECT
print(revenue_EU_NA_Q1Q2.shape)
print(revenue_world_Q3Q4.shape)
print(revenue_EU_NA_Q1Q2.columns, revenue_world_Q3Q4.columns)



#-----------------------
# CONCATENATE DATAFRAMES
#-----------------------
pd.concat([revenue_EU_NA_Q1Q2, revenue_world_Q3Q4])




#----------------------------------------
# CONCATENATE DATAFRAMES AND IGNORE INDEX
#----------------------------------------
pd.concat([revenue_EU_NA_Q1Q2, revenue_world_Q3Q4]
          ,ignore_index = True)





#EOF