#####################################################
# FUNCTIONS
#
# How to ...
#   - define a new function
#   - modify a function to accept inputs (parameters)
#   - create functions with multiple parameters
#   - establish default function arguments
#
# sharpsightlabs.com
# © Copyright, Sharp Sight, Inc.
# All rights reserved
#
#####################################################



#=============================
# HOW TO DEFINE A NEW FUNCTION
#=============================

# DEFINE
def print_advice():
    print("Study data science.")


# EXECUTE
print_advice()



#========================================
# DEFINE FUNCTION WITH AN INPUT PARAMETER
#========================================

def hello_target(target):
    print("Hello",target)


# EXECUTE WITH ARGUMENT
hello_target("Cleveland!")
hello_target("Austin!")


# ERROR!
# - we defined an input parameter
#   but we aren't providing an argument 
#   when we execute the function
hello_target()



#=================================
# FUNCTION WITH A DEFAULT ARGUMENT
#=================================

#------------------------------------------------------------
# DEFINE
# – Here, we're defining an input parameter, 'subject'
#   and we're also providing a default argument 'data science'
# – If we run this without an argument, it will automatically
#   use 'data science' as the argument
# – but, we can still use a custom argument too
#------------------------------------------------------------
def print_custom_advice(subject = 'data science'):
    print("Study", subject)


# EXECUTE DEFAULT
print_custom_advice()


# EXECUTE WITH ARGUMENT
print_custom_advice(subject = 'statistics')



#==================================
# FUNCTION WITH MULTIPLE PARAMETERS
#==================================

#---------------------------------------------
# DEFINE
# - here, we're defining a function with
#   two input parameters
# – that means that we need to provide
#   two arguments when we execute the function
# – note: here, we're not providing defaults
#   so we'll get an error if we don't provide
#   two arguments
#---------------------------------------------

def hello_both(target1, target2):
    print("Hello", target1, "and", target2)
    print("Hello, {} and {}".format(str(target1), str(target2)))


# EXECUTE WITH 2 ARGUMENTS
hello_both("John", "Mike")



#===============================
# FUNCTION WITH RETURN STATEMENT
#===============================

# DEFINE
# – this function will return a value
def calculate_cube(number):
    return number ** 3


# EXECUTE
calculate_cube(3)


# STORE THE OUTPUT OF THE FUNCTION
cube_value = calculate_cube(3)

print(cube_value)


# END