#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 08:19:14 2022

@author: craigrupp
"""

# Web Scraping
# =============================================================================
# Web Scraping is the method of getting data from the Web. 
# It is used to collect large amounts of information from websites. 
# For example, compare prices on different platforms or collect social media.
# 
# The first step will be to extract the data as an HTML file. 
# Once we have the raw data in such a format, we can get any information we want
# =============================================================================

from urllib.request import urlopen

url = "https://codefinity-content-media.s3.eu-west-1.amazonaws.com/18a4e428-1a0f-44c2-a8ad-244cd9c7985e/page.html"
page = urlopen(url)

print(page)

# =============================================================================
# It returns HTTPResponse object. 
# To parse it, use the .read() method, which returns a sequence of bytes, and then 
# the function decode("utf-8") to decode the data from bytes to string
# =============================================================================
bytes = page.read()
html = bytes.decode("utf-8")

print(html)
# One line
print(page.read().decode("utf-8"))


# String Methods
# =============================================================================
# One of the ways to do it - use string methods. 
# For example, function .find(). This method returns the index of the first appearance of the string you want to find.
# =============================================================================
print(html.find("<h1>"))

# Find the first index of the tag
print(html)
index_first = html.find("<title>")
print(index_first)

# Find the last index of the tag
index_last = html.find("</title>") + len("</title>")
print(index_last, len("</title>"), html.find("</title>"))

# Extract the title
title = html[index_first:index_last]
print(title)

# Title no headers
print(html[html.find("<title>")+7:html.find("</title>")])


# RegEx
# =============================================================================
# Regular expressions (or regex) are patterns that help to search for information within a string. To use them, import re module:
# =============================================================================
import re

# * (zero or more)
result = re.findall("xy*z","xz; xyz; xyyz; xy;")
print(result)

# =============================================================================
# The function .findall() finds all parts of the string which start with 'x', end with 'z', and have any number of the characters 'y' between them (including 0). 
# The method returns the list of all matches found and the empty list if no match was there:
# =============================================================================

# To find matches regardless case, you can use re.IGNORECASE as the third argument:
print(re.findall("apple", "Apple is a fruit."))
print(re.findall("apple", "Apple is a fruit.", re.IGNORECASE))


# Find all words in the variable text which start with 'a', end with 'c', and have zero or more instances of the character 'b'. Ignore the case.
text = "ac abc Axc a c aC aBc AbBbBc ABBA"
result = re.findall("ab*c", text, re.IGNORECASE) 

# Print the result
print(result)

# =============================================================================
# The symbol . stands for any character in the regular expression. 
# For instance, we want to find all parts of a string which start with 'a' and end with 'c' separated by a single character:
# =============================================================================
text = "abc a c abbc ac adc"
print(text.split(" "))
result = re.findall("a.c", text)
print(result)
# print(result) : ['abc', 'a c', 'adc']

# Like function
def wildcard(string, exp):
    capturedexp = []
    while string.find(exp[0]) != -1:
        a_ind = string.find(exp[0])
        any_char_count = exp.count('.')
        end_char = string[-1]
        if string[a_ind + (any_char_count + 1)] == end_char and len(string[a_ind:]) > len(exp) + 1:
            end_char_index_inclusion = a_ind + (any_char_count + 1) + 1
            capturedexp.append(string[a_ind:end_char_index_inclusion])
            string = string[end_char_index_inclusion:]
            continue
        elif string[a_ind + (any_char_count + 1)] == end_char and len(string[a_ind:]) < len(exp) + 1:
            # End of String catch
            capturedexp.append(string[a_ind:])
            break
        else:
            string = string[a_ind+1:]
            continue
    return capturedexp
    

print(wildcard(text, "a.c"))
# ['abc', 'a c', 'adc']
print(wildcard("caad cdcd cad ceed cfgrd cfad", "c..d"))
# ['caad', 'cdcd', 'ceed', 'cfad']    
print('a.c'.count('.'))
print(len("adc"))

# While loop basic for a little refreshing for above break/continue logic
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
    

# Back to the Lesson 
# =============================================================================
# The symbols .* are used to find expressions with any character repeated any number of times:
# =============================================================================
text_1 = "abc addc ac axc aOc"
result_1 = re.findall("a.*c", text_1)
print(result_1)



# Search
# =============================================================================
# There is another method for finding matches - .search(). 
# It is much more complicated than the function .findall() since it returns the answer as MatchObject. 
# The object stores different groups of the data because the function .search() also finds matches inside other matches and returns them.
# =============================================================================
match = re.search("ab*c", "Axc ABc Ac", re.IGNORECASE)
print(match.group())

# Huh .. that's odd (oh wait that's how .group() prioritizes!)
# =============================================================================
# Just remember that the function .group() of this object will return the first and most appropriate result:
# =============================================================================


# Sub
# =============================================================================
# You can also substitute text you want. 
# Use the function .sub() of the module re to replace text (the first argument) that matches your expression to the new one (the second argument) 
# and the string in which we make a replacement (the third argument). For instance:
# =============================================================================
text = "I love <apples>."
text = re.sub("<.*>", "dogs", text)
print(text)

text = "I replace <words> with the word <cats>."
text = re.sub("<.*>", "CATS", text)
print(text)

# <.*?> All type catch
# =============================================================================
# What is going on with cats? Why, in the second example, weren’t both words replaced? 
# If you use the regular expression <.*>, everything between the first < and the last > will be replaced (like in our example). 
# It happens since regular expressions try to find the longest possible match. To avoid such mistakes, use the regular expression <.*?>. 
# It works the same way but tries to find the shortest possible match:
# =============================================================================
text_1 = "I replace <words> with the word <cats> because we love <animals>."
print(re.sub("<.*?>", "CATS", text_1))



# HTML - RegEx!
# =============================================================================
# How to Extract Text from HTML Using Regular Expressions

# Here we will get the content of title without tags and errors because of extra spaces since 
# the regular expression .*? helps to extract data with any number of spaces.
# always use the exp : *? in familiar situations. This symbol will match the smallest number of letters possible.
# =============================================================================

# Open the page
url = "https://codefinity-content-media.s3.eu-west-1.amazonaws.com/18a4e428-1a0f-44c2-a8ad-244cd9c7985e/budda.html"
page = urlopen(url)
html = page.read().decode("utf-8")

# Define the pattern and extract text
pattern = "<h1.*?>.*?</h1.*?>"
matches = re.search(pattern, html, re.IGNORECASE)
h1 = matches.group()
print(h1)
# Remove tags
h1_clean = re.sub("<.*?>", "", h1)

# Print the result
print(h1_clean)















    