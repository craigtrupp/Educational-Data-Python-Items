#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 19:16:03 2022

@author: craigrupp
"""
import pandas as pd
data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/titanic_0.csv', index_col=0)
data.head(2)

# =============================================================================
# As you remember, we have two functions to check for the missing values. 
# To calculate the sum, just use the .sum() function. 
# Thus, in general, we have 4 variants of how to output the number of NaNs for each column:
# =============================================================================
data.isna().sum()


# =============================================================================
# The cabin column in the dataset has considerable missing rows and at this point with futher information, we can drop (but let's keep the rows')
# =============================================================================
data.drop(columns='Cabin', inplace=True)

data.isna().sum()


# =============================================================================
# The simplest way is to delete all rows that contain missing values. 
# or instance, 86 rows with ages are missed and 1 row in the column 'Fare' too. 
# Let's figure out how we can delete them. 
# In pandas, you can do it using one simple function similar to the one in the previous chapter called .dropna():
# =============================================================================
data.dropna(inplace=True)
data.isna().sum()



# =============================================================================
# Fill Missing values
# Deleting missing values is not the only way to get rid of them. 
# You can also replace all NaN with the defined value. 
# For instance, with the mean/median value of the column or with zeros
# =============================================================================
data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/titanic_2', index_col = 0)
data['Age'].median()
data.isna().sum()
data['Age'].fillna(value = data['Age'].median(), inplace=True)
data.isna().sum()
data['Age'].value_counts()
len(data.loc[data['Age'] == data['Age'].median()])





# =============================================================================
# What should we do to calculate the number of values in each category or to find out information about them?
# 
# You know .loc[], .isin(), .between() and a lot of functions already, but in pandas, there is a more beautiful and convenient way to do it. 
# Use the function .get_dummies(). We will apply it to the column 'Embarked' for an example. 
# Look at the implementation and the result (we will output random 5 passengers' names and new columns we created).
# =============================================================================
data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/titanic3.csv', index_col = 0)
print(data['Embarked'].unique())
data = pd.get_dummies(data, columns = ['Embarked'])
print(data[['Name', 'Embarked_C', 'Embarked_Q', 'Embarked_S']].sample(5))


# =============================================================================
# As a result, our function split the column 'Embarked' into three columns: 
# 'Embarked_C', 'Embarked_Q', 'Embarked_S'. In total, we have three categories. 
# Each passenger has their category in the 'Embarked' column. 
# Thus, our function creates three columns corresponding to each category, and in line, with each passenger, it fills the row of the column with 1 if the person initially related to the geology; 
# otherwise, 0. So, we can get 1 just in one column.
#
# pd.get_dummies() - function converts categorical variables into dummy (1 or 0).
# data - dataframe which you want to use.
# columns = ['Embarked'] - columns have categorical variables which you want into transform to dummy ones. Pay attention; it is obligatory to put column names into the list.
# =============================================================================
data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/titanic3.csv', index_col = 0)

# Modify the column
data = pd.get_dummies(data, columns = ['Sex'])
# Calculate the sum of values
sex_male = data['Sex_male'].sum()
# Calculate the sum of values
sex_female = data['Sex_female'].sum()

# Output the sum
print(sex_male, sex_female)    



# =============================================================================
# Manage Incorrect Column
# So, you received the result object. It means that the type of the column is non-numerical, but to calculate necessary values, the column need to be numerical. 
# Firstly we need to replace - by .. To do it, you will apply the function .str.replace() that replaces the character in the string in the data set column. 
# The syntax is data['column name'].str.replace('old_symbol','new_symbol'). 
# In our case, old_symbol is - and . is the new_symbol.
# Then, convert the column to the float data type. To do it use .astype() function. The syntax is data['column_name'].astype('type'). In our case type is 'float'.
# =============================================================================


data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/titanic3.csv', index_col = 0)
data['Fare'].value_counts()
# Invalid character, update dash to .
# Replace `-` with the `.`
data['Fare'] = data['Fare'].str.replace('-', '.')
# Convert column to the float type of data
data['Fare'].value_counts()
data['Fare'] = data['Fare'].astype('float')

# Output the type of the column 'Fare'
print(data['Fare'].dtype)



# =============================================================================
# Rename a Column
# To rename a column use .rename() function. 
# =============================================================================
data = pd.read_csv('https://codefinity-content-media.s3.eu-west-1.amazonaws.com/4bf24830-59ba-4418-969b-aaf8117d522e/titanic4.csv', index_col = 0)
data.columns
# 'Column_Current_Name': 'New_Name'
data.rename(columns = {'Survived': 'Survived_Passenger'}, inplace = True)
print(data.columns)  

    
    
    
