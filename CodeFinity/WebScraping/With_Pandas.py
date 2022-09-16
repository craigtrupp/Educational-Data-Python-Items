#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 14:04:46 2022

@author: craigrupp
"""

# Work w/Dataframes from Scraped Data

# In this chapter, we will consider the method, where the parsed HTML data will be contained in the dictionary, 
# to be lately converted to the DataFrame.

# =============================================================================
# The last step is to convert our dictionary to the DataFrame. 
# To do this, import the library pandas and initialize the DataFrame using the method .from_dict() to convert the dictionary:
#     
# import pandas as pd
# statue_df = pd.DataFrame.from_dict(statue_data, orient = 'index')
# 
# We specified the parameter orient as the 'index' to create the DataFrame using dictionary keys as rows.
# =============================================================================

# Import libraries
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

# Open the page
url = "https://codefinity-content-media.s3.eu-west-1.amazonaws.com/18a4e428-1a0f-44c2-a8ad-244cd9c7985e/page.html"
page = urlopen(url)
html = page.read().decode("utf-8")

# Create the BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")

# Select all a tags
a_tags = soup.select("a")
print([a['href'] for a in a_tags])
# Define and fill the list with links to the pages
links = []
links_comp = [a['href'] for a in a_tags]
for a in a_tags:
    links.append(a["href"])
print(links)
print(links_comp)
# Define the dictionary
statue_dict = {}

# Go thought all links
for link in links:
    # Open the page
    page = urlopen(link)
    html = page.read().decode("utf-8")

    # Create the BeautifulSoup object
    new_soup = BeautifulSoup(html, "html.parser")

    # Get the title and other data on the page select returns title in array (index[0].get_text() pulls only the text)
    statue_title = new_soup.select("title")[0].get_text()
    #print(new_soup.select("title"))
    # Get the list items from each statue
    statue_data = new_soup.find("ul")
    #print({statue_title : statue_data})
    # Save the data in the dictionary
    statue_dict[statue_title] = statue_data

# Evaluate statue_dict (title is the key and list items are the value for each read in link)
print(statue_dict)


df_test = pd.DataFrame.from_dict(statue_dict, orient='index', dtype='object')
print(df_test.head(1))
# All ul list sizes are hopefully the same! Thankfully they are! This is removing the empty \n type columns 
df_test = df_test.iloc[:, [x for x in range(13) if x % 2 != 0]]
# Rename columns to key 
df_test.rename(columns = {1 : "Name", 3: "Country", 5: "City", 7: "Height", 9: "Material", 11: "Completion Date"}, inplace=True)

test = df_test.head(1)
df_test.drop(['Name'], axis=1, inplace=True)
print(df_test.loc['The Big Buddha', :], df_test.loc['The Big Buddha', 'City'], type(df_test.loc['The Big Buddha', 'City']))

# https://stackoverflow.com/questions/39475978/apply-function-to-each-cell-in-dataframe
import numpy as np
def slicebs4(x):
    hey = x.string
    hey = hey[hey.find(':')+2:]
    return hey

print(slicebs4(test.loc['The Big Buddha', 'Country']))
test.apply(np.vectorize(slicebs4))
df_test = df_test.apply(np.vectorize(slicebs4))
df_test.head(2)
# Codefinity

statue_dict_two = {}
# Go thought all links
for link in links:
    # Open the page
    page = urlopen(link)
    html = page.read().decode("utf-8")

    # Create the BeautifulSoup object
    new_soup = BeautifulSoup(html, "html.parser")

    # Get the title and other data on the page
    statue_title = new_soup.title.get_text()
    statue_info = new_soup.find("ul").get_text()

    # Save the data in the dictionary
    statue_dict_two[statue_title] = statue_info

print(statue_dict_two)
# Convert dictionary to the DataFrame
df = pd.DataFrame.from_dict(statue_dict_two, orient='index')
#print(df.columns)
# Display the max amount of columns
pd.set_option('display.max_columns', None)

# Separate the text on page by columns
print(df[0].str.split(r"\n", expand=True))



