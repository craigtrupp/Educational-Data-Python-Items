##############################################################
# USING Python LIKE A CALCULATOR
#
# How to ...
#   - use Python like a calculator
#   - use mathematical operators to perform math calculations
#   - calculate with "literal" numbers
#   - calculate with variables
#
# sharpsightlabs.com
# © Copyright, Sharp Sight, Inc.
# All rights reserved
#
##############################################################


#========================
# CALCULATING WITH Python
#========================


#--------------------------------
# CALCULATING WITH LITERAL VALUES
#--------------------------------

# ADDITION
7 + 2

# SUBTRACTION
8 - 3

# MULTIPLICATION
3 * 4

# DIVISION
13 / 2

# EXPONENTIATION
3**3

# NEGATIVE NUMBERS
5 * -2


#---------------------------
# CALCULATING WITH VARIABLES
#---------------------------

# define variables
a = 5
b = 3


# add them together
a + b


# mix variables with literal values
a + 4


#---------------------------------------------------------
# NOTE: 
#  Calculations don't automatically change variable values
#---------------------------------------------------------

# Define variable and perform calculation
a = 4
a + 1

# Notice that after the addition operation, the value of a is unchanged
a


#-------------------------------
# CHANGE THE VALUE OF A VARIABLE
#-------------------------------

a = 4
a = a + 1

a
#5


#========================================
# ORDER OF OPERATIONS
#
# Here, I'll show you a calculation with
# brackets in different places
#
# This will result in different values
# depending on the order of operations
# for the calulaiton
#========================================

3 + 5 * 4
#23 1) 5 * 4 2) 3 + 20 (result of first operation)

(3 + 5) * 4
#32 1) parentheses =8 2) value * 4 = 32

3 + (5 * 4)
#23 explicit declaration on what runs first


#END