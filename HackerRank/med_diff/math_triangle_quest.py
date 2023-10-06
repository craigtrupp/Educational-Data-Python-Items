#### **Math - Triangle Quest 2** ####
# You are given a positive integer N.
# Your task is to print a palindromic triangle of size N.

# For example, a palindromic triangle of size 5 is:
# 1
# 121
# 12321
# 1234321
# 123454321

# You can't take more than two lines. The first line (a for-statement) is already written 
# for you.You have to complete the code using exactly one print statement.

# https://realpython.com/lessons/range-decrementing/

## Input - 5

## output
# 1
# 121
# 12321
# 1234321
# 123454321 



for i in range(1, int(input()) + 1):
    print(*[str(i) for i in range(1, i + 1)] + [str(i) for i in range(i - 1, 0, -1)])

## Output - Unpacking the combined list gives right values .. wrong spacing
# 1
# 1 2 1
# 1 2 3 2 1
# 1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1


for i in range(1, int(input()) + 1):
    print(*[i for i in range(1, i + 1)] + [i for i in range(i - 1, 0, -1)], sep='')

## Output - Still a string though
# 1
# 121
# 12321
# 1234321
# 123454321





## Aceepted Solution : This challenge kinda sucked
for i in range(1, int(input()) + 1):
    print(int(i*ascii(1))**2)
