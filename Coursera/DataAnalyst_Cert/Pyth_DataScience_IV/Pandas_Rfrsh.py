#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 12:11:03 2022

@author: craigrupp
"""

import pandas as pd

x = {'Name': ['Rose','John', 'Jane', 'Mary'], 'ID': [1, 2, 3, 4], 'Department': ['Architect Group', 'Software Group', 'Design Team', 'Infrastructure'], 
      'Salary':[100000, 80000, 50000, 60000]}

#casting the dictionary to a DataFrame
df = pd.DataFrame(x)

#display the result df
df

# Retrieving the "ID" column and assigning it to a variable x
x = df[['ID']]
x
print(type(x))

# Retrieve pandas series
sal_series = df['Salary']
print(sal_series)
print(type(sal_series))


#Retrieving the Department, Salary and ID columns and assigning it to a variable z
z = df[['Department','Salary','ID']]
z


# Exercises:
    
# Create DF (Screenshot within lesson = student grade/course details)
student_data = {'Student' : ['David', 'Samuel', 'Terry', 'Evan'], 'Age' : [27, 24, 22, 32], 
               'Country' : ['UK', 'Canada', 'China', 'USA'], 'Course' : ['Python', 'Data Structures', 'Machine Learning', 'Web Development'], 
               'Marks' : [85, 72, 89, 76]}
student_df = pd.DataFrame(student_data)
print(student_df)

# Problem 2: Retrieve the Marks column and assign it to a variable b
b = student_df[['Marks']]
b
type(b)

# Series
b_series = student_df['Marks']
b_series 
type(b_series)

# Problem 3: Retrieve the Country and Course columns and assign it to a variable c
c = student_df[['Country', 'Course']]
c


# Loc/Iloc
# Access the value on the first row and the first column
df.iloc[0, 0]

# Access the value on the first row and the third column
df.iloc[0,2]

# Access the column using the name
df.loc[0, 'Salary']


# Make Copy
df_c = df.copy()

print(df_c.head())

# Set Column to Index
df_c.set_index('Name', inplace=True)
df_c


#Now, let us access the column using the name
df_c.loc['Jane', 'Salary']


# Jane's Department
print(df_c.loc['Jane', 'Department'])

# Rose & Mary's :  Salary & Department
print(df_c.loc[['Mary', 'Rose'], ['Department', 'Salary']])



# Slicing
 
# let us do the slicing using old dataframe df

df.iloc[0:2, 0:3]

#let us do the slicing using loc() function on old dataframe df where index column is having labels as 0,1,2
df.loc[0:2,'ID':'Department']

df_idx = df.reset_index()
print(df_idx.head())
print(df_idx.iloc[0:2, 1:3])
print(df.loc[0:2, 'Name':'Salary'])


#let us do the slicing using loc() function on new dataframe df1 where index column is Name having labels: Rose, John and Jane
df_c.loc['Rose':'Jane', 'ID':'Department']



# =============================================================================
# Second Section
# Two files (same details just load in different types - Just use one with DF exercises)
# =============================================================================

# CSV
csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
df = pd.read_csv(csv_path)
print(df.head())
print(df.columns)
print(df.info())

# Excel
xlsx_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx'

df_xc = pd.read_excel(xlsx_path)
df_xc.head()

df_xc.columns

print(df_xc.iloc[1:4, 0:2])


df.loc[:, 'Rating']
type(df.loc[:, 'Rating'])
df[['Rating']]
type(df[['Rating']])



# =============================================================================
# Use the following list to convert the dataframe index df to characters and assign it to df_new; 
# find the element corresponding to the row index a and column 'Artist'. 
# Then select the rows a through d for the column 'Artist'
# =============================================================================
new_index=['a','b','c','d','e','f','g','h']

# Access index and updated
print(df.index, df.shape[0], len(new_index))
df.index = new_index
print(df.index)

df.loc['a', 'Artist']


df.loc['a':'d', 'Artist']
df.ix[0,0]























