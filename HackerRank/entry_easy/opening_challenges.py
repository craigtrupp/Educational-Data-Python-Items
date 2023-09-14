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


### Find The Runner Up Score
# Given the participants' score sheet for your University Sports Day, you are required to 
# find the runner-up score. You are given "n" scores. Store them in a list and find the score of 
# the runner-up.
## Constraints : 
#   2 <= n <= 10 (number of scores must be between 2 and 10)
#   -100 <= A[i] <= 100 (each score in defined -100 to 100 range)
if __name__ == '__main__':
    n = int(input()) # n == 5
    arr = map(int, input().split()) # list(arr) == [2, 3, 6, 6, 5] but as a map object (transform to arr)

ranks = list(arr) # transform map object for second constraint check
constraint_1 = 2 <= n <= 10
constraint_2 = all([True for x in ranks if x >= -100 and x <= 100])
if constraint_1 and constraint_2:
    unique_ranks = list(set(ranks))
    ranked_scores = sorted(unique_ranks, reverse=True)
    runner_up_score = ranked_scores[1]
print(runner_up_score)

