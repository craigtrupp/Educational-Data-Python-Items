##################################################
# RESET INDEX
#
# You'll learn:
# 
# - How to use the .reset_index() method in Pandas
# - How to turn the index back into a column
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




#-----------------
# CREATE DATAFRAME
#-----------------

emp_fst_nm = pd.DataFrame({'employee_id' : [101,102,103,104,900]
                           ,'first_name' : ['John', 'Paul', 'George', 'Ringo', 'Stuart']
                           })

multi_level = pd.DataFrame({'country' : ['USA', 'USA', 'USA', 'USA'],
                            'region' : ['Southwest', 'East', 'Northwest', 'Northwest'],
                            'city' : ['Santa Fe', 'Philadelphia', 'Seattle', 'Portland']
                            });

multi_level.set_index((['country', 'region']), inplace=True)
multi_level.loc[[('USA', 'Southwest'), ('USA', 'East')], 'city']


#----------
# SET INDEX
#----------

emp_fst_nm.set_index('employee_id', inplace = True)



# PRINT
print(emp_fst_nm)


# CHECK INDEX
emp_fst_nm.index



#------------
# RESET INDEX
#------------

emp_fst_nm.reset_index()




# CHECK INDEX
# - note: the index is still the same!
# - we need to use "inplace ="
emp_fst_nm.index



#--------------------
# RESET INDEX INPLACE
#--------------------

emp_fst_nm.reset_index(inplace = True)


# CHECK INDEX
emp_fst_nm.index


# PRINT
print(emp_fst_nm)





#EOF