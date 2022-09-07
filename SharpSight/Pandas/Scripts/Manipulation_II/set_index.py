##################################################
# SET INDEX
#
# You'll learn:
# 
# - How to set an index for a Pandas dataframe
# - How to set an index in place
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


print(emp_fst_nm)


#   employee_id first_name
#0          101       John
#1          102       Paul
#2          103     George
#3          104      Ringo
#4          900     Stuart


#------------
# CHECK INDEX
#------------

# Default range index applied to dataframe 29
[emp_fst_nm.index, emp_fst_nm.shape[0]]



#----------
# SET INDEX
#----------

emp_fst_nm.set_index('employee_id')
# drop by default True, can keep the column in place and set the index .. kinda crazy but maybe some use cases
emp_fst_nm.set_index('employee_id', drop=False)
emp_keep_col = emp_fst_nm.set_index('employee_id', drop=False)
emp_keep_col.index, emp_keep_col.columns
emp_keep_col.loc[101:103, ['employee_id', 'first_name']]
#            first_name
#employee_id           
#101               John
#102               Paul
#103             George
#104              Ringo
#900             Stuart


print(emp_fst_nm)


# Note: the index is not set!
#
#   employee_id first_name
#0          101       John
#1          102       Paul
#2          103     George
#3          104      Ringo
#4          900     Stuart




#------------------
# SET INDEX INPLACE
#------------------

emp_fst_nm.set_index('employee_id', inplace = True)


print(emp_fst_nm)



#            first_name
#employee_id           
#101               John
#102               Paul
#103             George
#104              Ringo
#900             Stuart



#------------
# CHECK INDEX
#------------

emp_fst_nm.index



# EOF