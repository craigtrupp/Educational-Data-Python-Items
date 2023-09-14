# An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

# In the Gregorian calendar, three conditions are used to identify leap years:

# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.
# This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years
def is_leap(year):
    leap = False
    # Write your logic here
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            leap = True
        elif year % 100 == 0 and year % 400 != 0:
            leap = False 
        else:
            leap = True
    return leap

year = int(input())
print(is_leap(year))


# The included code stub will read an integer, , from STDIN.
# Without using any string methods, try to print the following:
# Note that "" represents the consecutive values in between.
# Example
# Print the string 12345

if __name__ == '__main__':
    n = int(input())
if n >= 1 and n <= 150:
    num_str = ''
    for x in range(1, n+1):
        num_str += str(x)
print(num_str)


## See The List Comprehension for the problem defined and explanation of the output and generation of permutations
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

permutations = [[a, b, c] for a in range(x + 1) for b in range(y + 1) for c in range(z + 1)]
## We have all the permutations now and we need to print the permutations
## which don't sum to the value of n or our last argument
permutations_not_sum_n = [x for x in permutations if sum(x) != n]
print(permutations_not_sum_n)
