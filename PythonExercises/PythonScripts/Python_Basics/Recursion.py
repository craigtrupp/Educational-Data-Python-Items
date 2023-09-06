# The function sum_positive_numbers should return the sum of all positive numbers between the number n received and 1. 
# For example, when n is 3 it should return 1+2+3=6, and when n is 5 it should return 1+2+3+4+5=15.

def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n <= 1:
        return n
    # The recursive case is adding this number to 
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

## Outputs from above
# 6
# 15

## Run for 3 
# First Iteration : 
    # 3 < 1 False  so it returns the function call 3 + func_(2) 
    # Important to remember the 3 stays in memory so we can add on to it later
# Second Iteration : 
    # 2 < 1 False so it returns the function call 2 + func(1)
    # Now we have the numbers 3 (first iteration), 2 (second iteration) and the func call
# Third Iteration : 
    # 1 <= 1 
    # So we lastly return the N (which would be 1)
# Final (3 + 2  + 1)


def factorial(n):
    print("Factorial called with " + str(n))
    if n <= 1:
        print("Returning 1")
        return 1
    result = n * factorial(n -1)
    print("Returning " + str(result) + " for factorial of " + str(n))
    return result

print(factorial(4))

# Factorial called with 4
# Factorial called with 3
# Factorial called with 2
# Factorial called with 1
# Returning 1
# Returning 2 for factorial of 2
# Returning 6 for factorial of 3
# Returning 24 for factorial of 4
# 24


def is_power_of(number, base):
  # see if divisible (no remainder)
  if number % base == 0:
    # Start choping the tree (or number conition al check)
    number = number / base
    # if were down to having been divisible by itself for the below check else, keep slicing it down 
    if number == base:
      return True 
    else:
      return is_power_of(number, base)
  else:
    return False

print(is_power_of(8,2)) 
print(is_power_of(64,4))
print(is_power_of(70,10))

## Returns
# True
# True
# False


