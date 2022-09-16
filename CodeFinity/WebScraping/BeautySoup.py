#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 14:52:23 2022

@author: craigrupp
"""

# =============================================================================
# Regular expressions are great for matches but a bit inconvenient. 
# Python provides us with an instrumental library for web scrapping - BeautifulSoup!
# BeautifulSoup makes it easy to go through HTML files and extract the parts we are interested in
# =============================================================================


# Import libraries
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Open the page
url = "https://codefinity-content-media.s3.eu-west-1.amazonaws.com/18a4e428-1a0f-44c2-a8ad-244cd9c7985e/jesus.html"
page = urlopen(url)
html = page.read().decode("utf-8")
print(html)
# Create the BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")

print(soup.h1)

# Print the first h1 tag : https://beautiful-soup-4.readthedocs.io/en/latest/index.html?highlight=h1#encodings
print(soup.prettify())
print(soup.find_all())
print(soup.h1)
print(soup.p)
# Pull hrefs
print(soup.find_all('a'))



# Attributes
# =============================================================================
# In the code, we used the method .name to get the tag’s name and the function .attrs, which returns all tag attributes as a dictionary.
# 
# Another useful function is .get_text(), which extracts all the raw text from the website without HTML tags.
# =============================================================================
print(soup.h1.string)
print(soup.h3.get_text())
print(soup.div.name)
print(soup.div.attrs)

# If a tag contains more than one thing (or nothing), it is unclear what .string should refer to, so the function returns None.
print(soup.h2.get_text())

# Print attributes of the p tag
print(soup.p.attrs) 

# Print only the text of the ul tag
ul = soup.ul.get_text()
print(soup.ul.get_text(), type(soup.ul.get_text()))
print(soup.prettify())

print(ul[:29])
new_lines = []
for i in range(len(ul)):
    if ul[i] == '\n':
        new_lines.append(i)
print(new_lines)


# Find : FindAll
# =============================================================================
# BeautifulSoup offers methods for going through HTML tags. One of them is the function .find(). 
# It returns the first tag which matches the parameter or None if there are no matches
# =============================================================================
    

print(soup.find("p"))
# Same find
print(soup.p)
# Find all
print(soup.find_all("p"))
print(soup.find("h9"))

# Drill Down into class/id tags within the HTML body
print(soup.prettify())
print(soup.find_all("div", id = "id2"))
print(soup.find_all(attrs = {"class" : "banner"}))
print(soup.find_all(attrs = {"class":"afterbanner", "id": "id1"}))


# Little more HTML real estate to work with
url = "https://codefinity-content-media.s3.eu-west-1.amazonaws.com/18a4e428-1a0f-44c2-a8ad-244cd9c7985e/mother.html"
page = urlopen(url)
html = page.read().decode("utf-8")

# Create the BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")

# Print the first div tag
print(soup.find("div"))

# Print the tag p with the correct id
print(soup.find_all("p", attrs={"id" : "id0"}))

# Print the first div tag
print(soup.find("div"))

# Print the tag p with the correct id
print(soup.find_all("p", attrs={"id" : "id0"}))


import re

# We can also use the function .find_all() to find not only one but multiple tags using a list.
print(soup.find_all(['title', 'h1']))

print(soup.prettify())
def find_all_condition(tag):
    return tag.string == "City: Kyiv"
print(soup.find_all(find_all_condition))
iterab = soup.find_all(["div", "h1", "title"])
for i, idx in enumerate(range(len(iterab))):
    print(iterab[i], idx)


#W/Regex
# =============================================================================
# What to do if you want to get all of the tags h1-h8? To create eight element list? 
# Such a way can be a bit painful and takes a lot of time. Here you can apply the symbols []. 
# The regular expression will be h[1-8]. It means "match any number from 1 to 8 in combination with h".
# =============================================================================


tags = soup.find_all(re.compile("h[1-8]"))
print(tags)


# You can manipulate not only numbers but also characters! 
# For example, the following code extracts all the dl and dt tags:

# Here the regular expression means "match any the character l or t in combination with d".
dl_dt = soup.find_all(re.compile("d[lt]"))
print(dl_dt)




