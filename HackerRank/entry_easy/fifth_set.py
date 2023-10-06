#### **Sets : Intro to Sets** ####
# A set is an unordered collection of elements without duplicate entries.
# When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.

# Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student 
# Mickey to compute the average of all the plants with distinct heights in her greenhouse.

# Formula used: avg = sum_distinct_heights / total_distinct_heights

# >>> list(map(int, '1 3 5 9 11 35'.split()))
# [1, 3, 5, 9, 11, 35] - Quick reminder of some of the logc in the main function below

def average(array):
    # your code goes here
    return sum(set(array)) / len(set(array))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)



#### ** Sets: Symmetric Difference ** ####
# Task
# Given 2 sets of integers, M and N, print their symmetric difference in ascending order. 
# The term symmetric difference indicates those values that exist in either M or N but do not exist in both. (anti-join)

# Input Format

# The first line of input contains an integer, M.
# The second line contains M space-separated integers.
# The third line contains an integer, N.
# The fourth line contains N space-separated integers.

# Output Format

# Output the symmetric difference integers in ascending order, one per line.
# Enter your code here. Read input from STDIN. Print output to STDOUT
M = int(input())
a = set(map(int, input().split()))
N = int(input())
b = set(map(int, input().split()))
sym_diff = a.symmetric_difference(b) 
print(*sorted(list(sym_diff)), sep='\n')