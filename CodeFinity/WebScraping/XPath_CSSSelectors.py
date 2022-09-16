#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 10:56:17 2022

@author: craigrupp
"""
# XPath
# =============================================================================
# In the previous sections, we used a lot of different methods to find needed data without knowing the HTML way to the tag. 
# To extract desired parts of code describing where the elements exactly are (in your HTML structure), you can use XPath.
# 
# XPath provides us with simple Python-friendly syntax to navigate through the HTML file. 
# The notation is familiar with folder organization on your computer.
# 
# xpath = "/html/head/div"
# Here we define the path to all div tags in head tags of html tags.

# To specify which div from a variety of tags you want, enclose its number in square brackets []
# xpath = "/html/head/div[2]"
# This path for the following tree will detect the second div of the head (numeration starts from 1):

# If you want to detect all div tags everywhere, not only in head tags, use //. This symbol is used to pass tags. 
# For example, you want to detect all div blocks but don’t know the whole path to each one: xpath = "//div"

# xpath = "/html/body//p"
# The code above would target all p tags in the body tag/element

# =============================================================================


# Attributes in XPath
# =============================================================================
# xpath = "/html/body/div[@id = 'id1']"
# The code above defines the path to all div tags of the body tag, where the id is id1.
# 
# 
# xpath = "/html/body/div[@id = 'id1']/p[3]"
# Here we select the third p tag of the previously found div tag by the id attribute.
# 
# 
# To direct all child elements of the tag, you can use an asterisk * (like in SQL). For example, the path to all tags of the head tag:
# xpath = "/html/head/*"
# 
# Find all elements, which class is equal to class1
# xpath = "//*[@class = 'class1']"   
# =============================================================================


## Note : Be careful with quotes! It’s a good rule to define the path with one type of quote (double) and the attributes with another one (single). Or vice versa.


# Import libraries
from urllib.request import urlopen
from scrapy.selector import Selector

# Open the page
url = "https://codefinity-content-media.s3.eu-west-1.amazonaws.com/18a4e428-1a0f-44c2-a8ad-244cd9c7985e/jesus.html"
page = urlopen(url)
html = page.read().decode("utf-8")

# Create the Selector object
sel = Selector(text = html)

# Select the Title
title = sel.xpath("//title")
print(title, type(title), len(title))
print(title[:10])

# The function returns the list of all title tags as selector objects, which could be inconvenient in use. 
# To get any tag you want as a string, just specify the number of the list element and apply the function .extract()
print(title[0].extract())


# Select all p tags
p_tags = sel.xpath("//p")
print(p_tags, len(p_tags))
for ptag, pidx in enumerate(p_tags):
    print(ptag, '\n', pidx)
print(p_tags[0], p_tags[3])

# Print the fourth element of the list as the string 
print(p_tags[3].extract())




# CSS Selectors 
# =============================================================================
# Another common way to navigate through HTML files other than XPaths is CSS Selectors.
# 
# In the syntax of the XPathes / means to move forward to one generation, in CSS Selectors for this purpose is >. 
# For example:
    
# xpath = "/html/head/title"
# сss_selector = "html > head > title"
# These two variables point to the same tag in different ways. 
# Pay attention that we ignore the first / by replacing XPath notation with CSS Selector.

# To specify which tag we want to extract, :nth-of-type() w/number of tags as parameter
# xpath = "/html/head/div[2]"
# сss_selector = "html > head > div:nth-of-type(2)" 

# Sometimes, you need a unique indicator for not counting all tags. 
# For this purpose, you can use the id attribute. To find the element of the file by id with CSS Selectors, use a # sign:   
# xpath = "/html/body/div[@id = 'id1']"
# css_selector = "html > body > div#id1"

# To build a path to all elements belonging to the class, even if they belong to other classes, use a period . after tag’s name. 
# For instance:
# xpath = "/html/body/div[@class = 'class1']"
# css_selector = "html > body > div.class1"
# =============================================================================




# CSS Selectors - Beautiful Soup
# =============================================================================
# we will consider another way to work with CSS Selectors using the library BeautifulSoup from the previous section. 
# To select the data from the file, use the function .select() of the already created BeautifulSoup object

# сss_locator = "html > body > div"
# print(soup.select(сss_locator))

# We know how to navigate through HTML files using attributes. 
# However, we can select all elements with a specified class or id without the tag’s name or path. For example
# print(soup.select("#id-1"))
# print(soup.select(".class-1"))
# In the first line, we select all elements with the id equal to id-1. 
# In the second line, CSS Selector navigates to all tags that belong to the class-1

# Iterate through all elements of your class with for loop
# for link in soup.select(".class-link > a"):
#     page = urlopen(link)
#     html = page.read().decode("utf-8")
#     new_soup = BeautifulSoup(html, "html.parser")
# Here we go through all the links of the class class-link and create BeautifulSoup object for each new page


# Keep in mind instead of urlib.request library you can send a get request to the page using the requests library and .content function
# import requests

# page_response = requests.get(url)
# page = page_response.content
# =============================================================================

from bs4 import BeautifulSoup
from urllib.request import urlopen

# Open the page
url = "https://codefinity-content-media.s3.eu-west-1.amazonaws.com/18a4e428-1a0f-44c2-a8ad-244cd9c7985e/page.html"
page = urlopen(url)
html = page.read().decode("utf-8")

# Create the BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")

# Select all a tags
a_tags = soup.select("a")
print(a_tags)

# Define and fill the list with links to the pages
links = []
for a in a_tags:
    links.append(a["href"])

    
print(links)

# Go thought all links
for link in links:
    # Open the page
    page = urlopen(link)
    html = page.read().decode("utf-8")

    # Create the BeautifulSoup object
    new_soup = BeautifulSoup(html, "html.parser")

    # Print the tag title of each page
    print(new_soup.title)




# =============================================================================
# Choose CSS Selector equal to the following XPath:
# Notice the // backslash on the xpath which signifies that we're targeting all elements in the html with a second respective div
# Not a direct path or > not needed for CSS Selector that is targeting all type elements to mirror the xpath
# =============================================================================

xpath = "/html//div[2]/h1[@id= 'id0']"
css_selector = "html div:nth-of-type(2) > h1#id0"










































