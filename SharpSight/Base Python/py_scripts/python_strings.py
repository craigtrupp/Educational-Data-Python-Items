##############################################################
# PYTHON STRINGS
#
# How to ...
#   - create strings
#   - retrieve characters from strings
#   - retrieve slices of characters from strings
#   - find string items
#   - modify strings (upper case, lower case, etc.)
#
# sharpsightlabs.com
# © Copyright, Sharp Sight, Inc.
# All rights reserved
#
##############################################################



#--------------
# STRING BASICS
#--------------

# Create a string with single quotes
string_var = 'data'


# Create a string with double quotes
mystring = "Python’s a good language."


# PRINT STRING
print(mystring)


# Get the length of a string
len(mystring)


# Create string from other data type
print(str(4.4), type(str(4.4)))


# Combine two strings (concatenation)
string1 = 'I like '
string2 = 'Python'

newstring = string1 + string2



#-----------------------------
# RETREIVING STRING CHARACTERS
#-----------------------------

stringvar = 'Data'

# get first character
stringvar[0]


# get second character
stringvar[1]


# get last character
stringvar[-1]



#--------------
# STRING SLICES
#--------------

mystring = 'data'


#Extract first two characters
mystring[0:2]


#Extract last two characters
mystring[-2:]


#Extract middle two characters
mystring[1:3]



#----------------------------
# MODIFY THE CASE OF A STRING
#----------------------------
myquote = 'Slow is smooth, smooth is fast.'


# Convert all of the letters in this string to upper case.
myquote.upper()


# Convert all of the letters in this string to lower case.
myquote.lower()


# Capitalize each word in this string.
myquote.title()



#--------------------------------
# MISCELLANEOUS STRING OPERATIONS
#--------------------------------

# Count the number of times the letter 's' appears in this string.
myquote.count('s')
myquote.count('smooth')


# Find the first occurrence of the letter 't' in this string.
myquote.find('t')


# Use a method to remove the period at the end of this string.
myquote.strip('.')
print(myquote)
#Note chain a method doesn't modify the string but will return a string with the mehtod result call on the dtype
#END