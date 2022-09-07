##################################################
# DROP NA
#
# You'll learn:
# 
# - How to drop NA values from a dataframe
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

revenue_world_Q3Q4 = pd.DataFrame({'region':['Europe', 'Europe', 'North America', 'North America','South America','South America','Asia','Asia']
                            ,'quarter':['Q3','Q4','Q3','Q4','Q3','Q4','Q3','Q4']
                            ,'revenue':[61000,65000,73000,74000,72000,69000,69000,np.nan]
                            ,'currency':['Euro', 'Euro', 'USD', 'USD', np.nan, 'Peso', np.nan, np.nan]
                            })



# PRINT
print(revenue_world_Q3Q4, revenue_world_Q3Q4.shape)
# Only drop (all) if na (null) found in all three columns provided to subset
# Return doesn't remove rows as quarter has values for all rows
print(revenue_world_Q3Q4.dropna(how='all', subset=['quarter', 'revenue', 'currency']), 
      revenue_world_Q3Q4.dropna(how='all', subset=['quarter', 'revenue', 'currency']).shape)

# Any will drop
print(revenue_world_Q3Q4.dropna(how='any', subset=['quarter', 'revenue', 'currency']),
      revenue_world_Q3Q4.dropna(how='any', subset=['quarter', 'revenue', 'currency']).shape)

# Thresh requires threshold of how many non-NA values with common use of subset to require that many non-na values or will drop
revenue_world_Q3Q4

#See how last row is dropped here as from the the three columns chosen at least two can't be null : which in this case is False hence dropped
revenue_world_Q3Q4.dropna(how='any', subset=['quarter', 'revenue', 'currency'], thresh=2)
# Last row is not dropped with the inclusion of region as two of the row's column values are present
revenue_world_Q3Q4.dropna(how='any', subset=['quarter', 'revenue', 'currency', 'region'], thresh=2)



#--------
# DROP NA
#--------
revenue_world_Q3Q4.dropna()
revenue_world_Q3Q4.dropna().shape



#----------------
# DROP NA INPLACE
#----------------
revenue_world_Q3Q4.dropna(inplace = True)

print(revenue_world_Q3Q4)



#EOF