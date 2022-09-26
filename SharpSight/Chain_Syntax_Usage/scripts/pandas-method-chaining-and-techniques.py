################################################
# COMBINING SYNTAX & DATA TECHNIQUES
#
# You'll learn:
# 
# - How to "chain" Pandas methods together
# - How to aggregate and "wrangle" data using
#    multiple tools
# - Techniques and "recipes"
#    for getting things done
#
# © Copyright Sharp Sight
# sharpsightlabs.com
# All rights reserved
#
################################################


#---------------
# load packcages
#---------------
import pandas as pd



#---------
# GET DATA
#---------
supercars = pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/supercars.csv')
bank = pd.read_csv('https://learn.sharpsightlabs.com/datasets/pdm/bank.csv')



#--------
# Inspect
#--------
bank.head()
bank.columns
bank.describe()



#===========================
# DATA SUBSETTING TECHNIQUES
#===========================

#---------------------------
# FILTER
# - retrieve a single variable
#---------------------------

bank.filter(['balance'])

# Identation error if opening and closing of chain methods not wrapped in paranthesis
(bank
   .filter(['balance'])
)



#-------------------------------
# FILTER
# - retrive a multiple variables
#-------------------------------
bank.filter(['job', 'balance', 'age'])
# Same as the below iloc which is getting all the rows then were subsetting on the multiple columns (numeric row index vs 'string' column retrieval)
bank.iloc[0:][['job', 'balance', 'age']]

# if use one column
bank.iloc[0:]['job']
#---------------------------------
# FILTER 
# - only the numeric columns
# dataframe.select_dtypes
#---------------------------------
bank.select_dtypes(include = ['int','float'])[:5]
bank.info()


#---------------------------------
# QUERY
# - subset rows where age is 25
#---------------------------------
bank.query('age == 25')
# Grab the tail 
bank.query('age == 25').tail(2)


#-----------------------------------
# SUBSET ROWS ON MULTIPLE CONDITIONS
# - subset rows where age is 25
# - subset rows where loan is 'yes'
#-----------------------------------

(bank
  .query("age == 25")
  .query("loan == 'yes'")
)

(bank
  .query("age == 25")
  .query("loan == 'yes'")
)[['age', 'loan', 'job', 'subscribed']]


#---------------------------------
# QUERY & FILTER
# - only the numeric columns
#---------------------------------

(bank
  .query("age == 25")
  .filter(['age', 'job', 'subscribed'])
)

(bank
 .query('age == 25')
 .select_dtypes(include = ['int', 'float'])
)[:5]

print(len((bank
 .query('age == 25')
 .select_dtypes(include = ['int', 'float'])
)))


#===========================
# DATA INSPECTION TECHNIQUES
#===========================

#--------
# Inspect
#--------
bank.describe()


#---------------------------------------------
# COUNT RECORDS BY VARIABLE
#  - count by "education' categorical variable
#---------------------------------------------

(bank
  .education
  .value_counts()
)


#---------------------------------
# GET UNIQUE VALUES FOR A VARIABLE
#---------------------------------

(bank
  .job
  .unique()
)
print(bank['job'].unique())



#--------------------
# COUNT UNIQUE VALUES
#--------------------

(bank
  .job
  .nunique()
)



#---------------------------
# LOOK FOR DUPLICATE RECORDS
#---------------------------

# NOTE: supercars is not unique on model
(supercars
  .assign(count = 1)
  .groupby('model')
  .agg('sum')
  .filter(['model','count'])
  .query('count > 1')
  .sort_values('count', ascending=False)
)[:5]

# Quick View into count column and looking for duplicate model rows
(supercars
  .assign(count = 1)
  .groupby('model')
  .agg({'count' : 'sum'})
  .sort_values('count', ascending=False))

(supercars
  .assign(count = 1)
  .groupby('model')
  .agg('sum')
  .sort_values('count', ascending=False))


# NOTE: supercars _is_ unique on model and year combined
(supercars
  .assign(count = 1)
  .groupby(['model','year'])
  .agg({'count': 'sum'})
  .filter(['model','year','count'])
  .sort_values('count', ascending=False)
)





#=============================
# CALCULATE SUMMARY STATISTICS
#=============================

#---------------------------
# CALCULATE THE MEAN BALANCE
#---------------------------

(bank
   .filter(['balance'])
   .agg('mean')
)



#-----------------------------------------------
# QUERY & CALCULATE AVERAGE BALANCE
# - query on age
# - calculate average balance 
# - note: we're looking at 'age' but it could be
#   any variable of interest
#-----------------------------------------------

(bank
   .query('age == 25')
   .describe()
)



#------------------------------------------------------
# QUERY, GROUP, AND CALCULATE AVERAGE BALANCE
# - calculate the avaerage balance,
#   for a specific age, grouped by categorical variable
#------------------------------------------------------

# SIMPLE QUERY
(bank 
  .query('age == 25')
  .groupby('education')
  .agg('mean')
  .filter(['balance'])
)


# MORE COMPLEX QUERY
(bank 
  .query('(age >= 25) & (age <= 34)')
  .groupby('education')
  .agg('mean')
)

# perform lambda on dataframes filtered columns to clean up age & balance
(bank 
  .query('(age >= 25) & (age <= 34)')
  .groupby('education')
  .agg('mean')
  .filter(['age', 'balance'])
  .agg({'age' : lambda x: round(x,1), 'balance': lambda x: round(x, 2)})
)

# EOF