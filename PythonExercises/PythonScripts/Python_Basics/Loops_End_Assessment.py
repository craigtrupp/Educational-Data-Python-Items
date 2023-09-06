## 3 Function should count how many event numbers exist in a sequence from 0 to to the given number where 0 counts as an even number 
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



## 4 Function should print a sequence of numbers in descending order, from the given "high" variable to the given "low variable"
## inner loop is a bit deceiving (3, 0 (1-1), -1): this loops three times (3, 2, 1) but similar doesn't go to lowest threshold (0) hence why y is never 0
def sequence(low, high):
    # Complete the outer loop range to make the loop run twice
    # to create two rows
    for x in range(low, high): 
        # Complete the inner loop range to print the given variable
        # numbers starting from "high" to "low" 
        # Hint: To decrement a range parameter, use negative numbers
        for y in range(high, low - 1, -1): 
            if y == low:
                # Don’t print a comma after the last item
                print(str(y)) 
            else:
                # Print a comma and a space between numbers
                print(str(y), end=", ") 

sequence(1, 3)
# Should print the sequence 3, 2, 1 two times

## Output
# 3, 2, 1
# 3, 2, 1


# 5 Function should show the count of values from 0 to the "max" parameter  that are evenly divisible by the "divisor" parameter
def divisible(max, divisor):
    count = 0 # Initialize an incremental variable
    for x in range(0, max): # Complete the for loop
        if x % divisor == 0:
            # print(x) guess we want 0 too!
            count += 1 # Increment the appropriate variable
    return count

print(divisible(100, 10)) # Should be 10
print(divisible(10, 3)) # Should be 4 [0, 3, 6, 9]
print(divisible(144, 17)) # Should be 9


# 6 
def even_numbers(maximum):
    return_string = "" # Initializes variable as a string
    # Complete the for loop with a range that includes all even numbers
    # up to and including the "maximum" value, but excluding 0.
    for number in range(2, maximum + 1, 2): 
        # Complete the body of the loop by appending the even number
        # followed by a space to the "return_string" variable.
        return_string +=  f'{number} '  
    # This .strip command will remove the final " " space at the end of
    # the "return_string".
    return return_string.strip() 

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed


## Returns (Look Good)
# 2 4 6
# 2 4 6 8 10

# 2


#9 End of nested for loop return (last value setting for each is 4 (last value of range 5) and 16 which is last range vale of (14) .. 13 and then that + 3 )
num1 = 0
num2 = 0
for x in range(5):
    num1 = x
    for y in range(14):
        num2 = y + 3

print(num1 + num2)
## 20 
