#### **Strings - Designer Door Mat** #### 
# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

# Mat size must be N X M. (N is an odd natural number, and M is 3 times N.)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.

## Sample Design
# Size: 7 x 21 
# ---------.|.---------
# ------.|..|..|.------
# ---.|..|..|..|..|.---
# -------WELCOME-------
# ---.|..|..|..|..|.---
# ------.|..|..|.------
# ---------.|.---------

# Size: 11 x 33
# ---------------.|.---------------
# ------------.|..|..|.------------
# ---------.|..|..|..|..|.---------
# ------.|..|..|..|..|..|..|.------
# ---.|..|..|..|..|..|..|..|..|.---
# -------------WELCOME-------------
# ---.|..|..|..|..|..|..|..|..|.---
# ------.|..|..|..|..|..|..|.------
# ---------.|..|..|..|..|.---------
# ------------.|..|..|.------------
# ---------------.|.---------------
import statistics as stats
catch = input()
items = [int(x) for x in catch.split()] # transform n, m to int for operations down the line
n, m = items[0], items[1]
surrounding_pattern = '.|.'
offset = 1
# use stats library to get median of N (N = 7, median needs = list of all integers up to N)
break_point = stats.median([x for x in range(1, n + 1)]) # [for n = 7 [1,2,3,4,5,6,7]]
string_rows = []
for i in range(1, n + 1):
    if i < break_point:
        string_rows.append((surrounding_pattern * offset).center(m, '-'))
        offset += 2
    elif i == break_point:
        string_rows.append('WELCOME'.center(m, '-'))
    else:
        offset -= 2
        string_rows.append((surrounding_pattern * offset).center(m, '-'))
print( '''{}'''.format('\n'.join(string_rows)))

