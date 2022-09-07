#########################################################
# BOOLEAN EXPRESSIONS AND COMPARISONS
#
# How to ...
#   - compare values and use logical expressions
#   - combine logical expressions using logical operators
#
# sharpsightlabs.com
# © Copyright, Sharp Sight, Inc.
# All rights reserved
#
#########################################################


#===============
# BOOLEAN BASICS
#===============

# True and False are built-in keywords
type(True)
type(False)


# You can use True and False as values
true_bool = True


print(true_bool)
type(true_bool)




#======================
# COMPARISON OPERATIONS
#======================

#--------------------------------------------
# Comparison operations return boolean values
#--------------------------------------------

1 == 1
  
1 != 2
  
100 > 5

100 < 5

3 <= 555
  
3 >= 555

42 in [1, 2, 3, 42, 5]


#--------------------------------------
# COMPARISON OPERATIONS, WITH VARIABLES
#--------------------------------------

x = 42
y = 11

x == y



#=============================
# COMPOUND BOOLEAN EXPRESSIONS
#=============================

#------------------------------------------------------------
# – We can combine comparison operations and 
#   small logical expressions into larger logical expressions
# – To do this, we can use and, or, and not
#------------------------------------------------------------

(10 > 1) and (9 == 9)


(10 > 1) and (9 == 1)


(10 > 1) and not (9 == 9)


(42 == 7) or (2 == 2)


(42 == 7) or True


#--------------------------------------
# ORDER OF OPERATIONS
# - comparison operations are evaluated 
#   before logical operators
#--------------------------------------

10 > 1 and 9 == 9

(10 > 1) and (9 == 9)



# END