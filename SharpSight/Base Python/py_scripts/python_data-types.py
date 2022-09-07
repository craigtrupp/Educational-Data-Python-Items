###########################################################
# ESSENTIALS OF PYTHON VARIABLES AND DATA TYPES
#
# How to ...
#   - create a variable
#   - print the contents of a variable
#   - check the data type of a variable
#   - reuse variable names
#   – create valid variable names
#
# sharpsightlabs.com
# © Copyright, Sharp Sight, Inc.
# All rights reserved
#
###########################################################



# Note: THIS IS A COMMENT



#-------------------
# CREATE VARIABLE: x
#-------------------
x = 42


#Print contents of variable
print(x)


#-----------------------------------------------------
# REUSING VARIABLE NAMES
# – note: names do *not* have a type
# – we can use a variable name for a numeric type
#   and then later use a variable name for a different
#   type like a string, list, etc
#-----------------------------------------------------

# Set value and print
x = 42
print(x)


# REUSE variable name 'x'
# – here, we're using a different number 
x = 11
print(x)


# REUSE variable name 'x'
# – here, we're using a string
x = 'This one goes to eleven.'
print(x)


# MORE TYPES
x = ['a','b','c']    #list
x = ('a','b','c')    #tuple
x = {42, 2.718, 'a'} #set
x = {'a':'alpha','b':'bravo','c':'charlie'} #dictionary
x = 2.718 #float



#---------------------------------------------------
# VARIABLE NAMING
# – capital letters are valid
# – lower case letters are valid
# – underscores are valid
# – numbers are valid inside the name
# – numbers are *invalid* at the beginning of a name
#---------------------------------------------------

# These are valid variable names
A_variable = 42
a_variable = 3.3
a_3rd_variable = 'Dummy data'



# ERROR
# – This is invalid
# – variable names can *not* begin with a digit
#9_variable = 9.99



#--------------------------------------------------
# OBJECT TYPE
# – we can get the data type stored in the variable
#   by using the type() function
#--------------------------------------------------

x = 11
type(x)


x = "This one goes to eleven."
type(x)



# END