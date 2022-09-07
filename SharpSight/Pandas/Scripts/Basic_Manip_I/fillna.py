########################################################
# FILL NA
#
# You'll learn:
# 
# - How to fill NA values in a dataframe with new values
#
#
# © Copyright Sharp Sight, Inc.
# sharpsightlabs.com
# All rights reserved
#
########################################################


#----------------
# IMPORT PACKAGES
#----------------

import pandas as pd
import numpy as np




#------------------
# CREATE DATAFRAMES
#------------------

revenue_world_Q3Q4 = pd.DataFrame({'region':['Europe', 'Europe', 'North America', 'North America','South America','South America','Asia','Asia']
                            ,'quarter':['Q3','Q4','Q3','Q4','Q3','Q4','Q3','Q4']
                            ,'revenue':[61000,65000,73000,74000,72000,69000,69000,np.nan]
                            ,'currency':['Euro', 'Euro', 'USD', 'USD', np.nan, 'Peso', np.nan, np.nan]
                            })



# PRINT
print(revenue_world_Q3Q4)




#--------
# FILL NA
#--------
revenue_world_Q3Q4.fillna(0)
revenue_world_Q3Q4.head(8)
revenue_world_Q3Q4.fillna(value={'revenue': revenue_world_Q3Q4['revenue'].mean(), 'currency': 'GBP'})
revenue_world_Q3Q4.revenue.mean()

#----------------
# FILL NA INPLACE
#----------------
revenue_world_Q3Q4.fillna(0,inplace = True)

print(revenue_world_Q3Q4)




# EOF