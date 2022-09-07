##################################################
# MERGE
#
# You'll learn:
# 
# - How to merge two dataframes (i.e., how to join)
#     - how to do a left join
#     - how to do a right join
#     - how to do a inner join
#     - how to join multiple dataframes
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



#------------------------
# CREATE SECOND DATAFRAME
#------------------------

emp_lst_nm = pd.DataFrame({'employee_id' : [101,102,103,104,901]
                           ,'last_name' : ['Lennon', 'McCartney', 'Harrison', 'Starr', 'Best']
                           })


print(emp_lst_nm)


#   employee_id  last_name
#0          101     Lennon
#1          102  McCartney
#2          103   Harrison
#3          104      Starr
#4          901       Best



#------------------------
# CREATE THIRD DATAFRAME
#------------------------

emp_job = pd.DataFrame({'employee_id' : [101,102,103,104,900,901]
                        ,'job': ['vocals', 'bass', 'guitar', 'drums','bass', 'drums']
        })


print(emp_job)

#   employee_id     job
#0          101  vocals
#1          102    bass
#2          103  guitar
#3          104   drums
#4          900    bass
#5          901   drums




#-----------
# LEFT MERGE
#-----------

print(emp_lst_nm)
print(emp_fst_nm)

pd.merge(emp_lst_nm, emp_fst_nm, on = 'employee_id', how = 'left')



#------------
# Right MERGE
#------------

print(emp_lst_nm)
print(emp_fst_nm)

pd.merge(emp_lst_nm, emp_fst_nm, on = 'employee_id', how = 'right')


#------------
# INNER MERGE
#------------

print(emp_lst_nm)
print(emp_fst_nm)

pd.merge(emp_lst_nm, emp_fst_nm, on = 'employee_id', how = 'inner')




#-----------------------------------------------
# METHOD VERSION
# - here we're going to use the .merge() method
#   instead of the .merge() function
#-----------------------------------------------

emp_fst_nm.merge(emp_lst_nm, on = 'employee_id', how = 'inner')





#-------------------------------
# CHAIN MULTIPLE MERGES
# - this technique is important 
#   when you have multiple files
#-------------------------------
emp_job
(emp_fst_nm
 .merge(emp_lst_nm, on = 'employee_id', how = 'inner')
 .merge(emp_job, on = 'employee_id', how = 'left')
)
(emp_fst_nm.merge(emp_lst_nm, on="employee_id", how="inner")
.merge(emp_job, on="employee_id", how="left"))


#EOF