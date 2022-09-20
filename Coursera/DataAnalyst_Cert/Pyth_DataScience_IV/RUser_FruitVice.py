#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 15:31:32 2022

@author: craigrupp
"""

# =============================================================================
# Simple APIs
# Random User and Fruitvice API Examples
# 
# Objectives
# After completing this lab you will be able to:
# 
# Load and use RandomUser API, using RandomUser() Python library
# Load and use Fruitvice API, using requests Python library
# =============================================================================

# =============================================================================
# The advantages of using APIs:
# 
# Automation. Less human effort is required and workflows can be easily updated to become faster and more
# productive.
# Efficiency. It allows to use the capabilities of one of the already developed APIs than to try to independently implement some functionality from scratch.
# The disadvantage of using APIs:
# 
# Secirity. If the API is poorly integrated, it means it will be vulnerable to attacks, resulting in data
# breeches or losses having financial or reputation implications.
# =============================================================================


# =============================================================================
# One of the applications we will use in this notebook is Random User Generator. 
# RandomUser is an open-source, free API providing developers with randomly generated users to be used as placeholders for testing purposes. 
# This makes the tool similar to Lorem Ipsum, but is a placeholder for people instead of text. 
# The API can return multiple results, as well as specify generated user details such as gender, email, image, username, address, title, first and last name, and more. 
# More information on RandomUser can be found here.
# 
# Another example of simple API we will use in this notebook is Fruitvice application. 
# The Fruitvice API webservice which provides data for all kinds of fruit! 
# You can use Fruityvice to find out interesting information about fruit and educate yourself. 
# The webservice is completely free to use and contribute to.
# =============================================================================

!pip install randomuser

from randomuser import RandomUser
import pandas as pd

# Create User Object
r = RandomUser()
type(r)

print(r.generate_users(15))
r_user_15 = r.generate_users(15)
print(r_user_15)


# Loop through users and pull attributes
for user in r_user_15:
    print (user.get_full_name()," ",user.get_email())

# Pull all methods for r User object
print([method for method in dir(r)])
    
# Generate Photos of Random Users
print(type(r.get_picture()))
print(r.get_picture())
user_photos = []
for user in r_user_15:
    user_photos.append({'Name': user.get_full_name(), "Jpg_image": user.get_picture()})
print(user_photos)


# Define function to generate 10 random users and following properties : [Name, Gender, City, State, Email, Dob, Picture] and return pandas dataframe
def get_users():
    users =[]
     
    for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
      
    return pd.DataFrame(users)     

df1 = get_users()
print(df1.head())



# =============================================================================
# Fruitvice API - Requests Library Usage
# =============================================================================

#Import req'd libraries
import requests
import json

# Simple Get Request for retrieve data
data = requests.get("https://www.fruityvice.com/api/fruit/all")
print(data.status_code)
print(data.text, type(data.text))

# The data is a JSON type dictionary that has been encapsulated as a string, let's use the json.load() function on the text to transform the type
fruit_results = json.loads(data.text)
print(type(fruit_results), fruit_results[0:2])

# Convert JSON Data into pandas dataframe
fruits_df = pd.DataFrame(fruit_results)
print(fruits_df.head())
# Validate all Keys were turned into columns
print(fruits_df.columns, fruit_results[0].keys())


print(fruits_df.iloc[0, -1])

# The result is in a nested json format. The 'nutrition' column contains multiple subcolumns (ie a dictionary), so the data needs to be 'flattened' or normalized.
# Provide loaded in results from the data's text 
fruits_df_flattened = pd.json_normalize(fruit_results)
fruits_df_flattened.head()
fruits_df_flattened.columns
# See how the values have maintained their parent like lookup to the nutritions object

# Check on Some Data in new df
cherry = fruits_df_flattened.loc[fruits_df_flattened["name"] == 'Cherry']
(cherry.iloc[0]['family']) , (cherry.iloc[0]['genus'])


# Quick Agg call on genus for calories and sugar sum stats
fruits_df_flattened.groupby('genus').agg({'nutritions.carbohydrates':['min', 'max', 'mean'], 'nutritions.calories': ['min', 'max', 'mean']})

# In this Exercise, find out how many calories are contained in a banana. (Couple different ways) and w/multiple columns
print(fruits_df_flattened.loc[fruits_df_flattened['name'] == 'Banana', 'nutritions.calories'])
print(fruits_df_flattened.loc[fruits_df_flattened['name'] == 'Banana', ['nutritions.calories', 'nutritions.carbohydrates']])
print(fruits_df_flattened.loc[fruits_df_flattened['name'] == 'Banana'][['nutritions.calories', 'nutritions.carbohydrates']])


# Another Free API for some quick pandas df building
data2 = requests.get("https://www.fishwatch.gov/api/species")
print(type(data2.text))
results2 = json.loads(data2.text)
data2_df = pd.DataFrame(results2)

print(data2_df.head(2))




