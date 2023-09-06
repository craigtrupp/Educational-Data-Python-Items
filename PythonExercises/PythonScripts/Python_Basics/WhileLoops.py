## Power of Two
def is_power_of_two(number):
  if number == 0:
    return False 
  while number % 2 == 0:
    number = number / 2
  return number == 1
  

# Calls to the function
print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False

## Result when Running in terminal (See Course Notes for further detail on handling if needed )
# False
# True
# True
# False

## Sum Divisors : Return the sum of all divisors of a number, without including the number itself 
# Reminder : Divisor is a number that divides into the number without a remainder
def sum_divisors(number):
    divisor = 1
    total = 0
    # Offset any values less than 1 to return no divisors (or the total of 0)
    if number < 1:
        return 0 
    # This will execute at least once with the offset above (2 > 1)
    while number > divisor:
        # Checks if passed number is divisible by dividsor (1 initially which it will be and checks to make sure to not add to the total if the number is simply divisible by itself (divisor * number))
        if number % divisor == 0 and number * divisor != number:
            total += divisor
            divisor += 1
        else:
            divisor += 1
    return total

print(sum_divisors(0)) # Should print 0
print(sum_divisors(2)) # Should print 0 not by itself
print(sum_divisors(3)) # Should print 0 as only by 1 and itself
print(sum_divisors(6)) # Would think just 5 (2 and 3) Should print 1+2+3+4+6+9+12+18
print(sum_divisors(36)) # 55
print(sum_divisors(102)) # 114

# 0
# 0
# 0
# 5
# 54
# 113


# Variable accepted should be multipled by numbers 1 through 5  and printed with the multiplication table (see print statement)
# Code needs to limit the result to not exceed 25 
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier < 6:
        result = number * multiplier 
        if  result > 25 :
            # Enter the action to take if the result is greater than 25
            return 
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        
        # Increment the appropriate variable
        multiplier += 1

print(multiplication_table(3))
print(multiplication_table(5))
print(multiplication_table(8))


## Quiz Question

# Function should count how many event numbers exist in a sequence from 0 to to the given number where 0 counts as an even number 
def even_numbers(n):
    count = 0
    current_number = 0
    while current_number <= n: # Complete the while loop condition
        if current_number % 2 == 0:
            count += 1 # Increment the appropriate variable
        current_number += 1 # Increment the appropriate variable
    return count
    
print(even_numbers(25))   # Should print 13
print(even_numbers(144))  # Should print 73
print(even_numbers(1000)) # Should print 501
print(even_numbers(0))    # Should print 1
print(even_numbers(6)) # Should equal 4

## Results
# 13
# 73
# 501
# 1
# 4