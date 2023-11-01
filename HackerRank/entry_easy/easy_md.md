## HackerRank 🧑‍💻 for Python First Diff Level (And a Few Medium Level Challenges) 🐍
* So sometimes the challenges are gonna be good to write in a markdown file as the detail isn't going to be the easiest comment for a straight python file in some scenarios
* Now ... to some challenges 
* Am also noting some challenges here for greater understanding of how the code working not just in a python script (see below!)
---

### **`File Details: Quick Summaries of Challenges`** 🗄️
* [**`Opening Challenges`**](/HackerRank/entry_easy/opening_challenges.py)
    * Leap Year Modulus Boolean Setting
    * Str building for input numeric value with range for loop
    * `List Comprehension` for permutation building - Further Details below for Challenge section capture
        * Good reminder on nested loop functionality in list comprehensions
    * `Runner Up Score` - use of all() for Boolean condition, sorted unique ranks with method chaining and **sorted** reverse argument to capture higher ranks
    * Formatting numeric string value for a rounded 2 digit float value
    * `Math pows`
    * list methods for **`mutating list commands` and update over While loop**
* [**`Second Set`**](/HackerRank/entry_easy/second_set.py)
    * `Tuple generation` from input and use of built_in hash method 
    * `Collections OrderedDict` - Receive input and iterate over total of N times - split input str by item/price and append or add to Ordered Dict
    * `Swap Values` - isalpha check with lower/upper check to swap values if character is alpha then join strings
    * **String operations** - `substr search`, `string mutation through slicing`, `split and join`
    * `String Operations` in `OrderedDict` for string check for any True characters in string based on provided string methods
        - Good reminder here of how to chain a method from an object (in this case a str) and pass a character to that object method call to evaluate
        - Also had tripped up on a test case here and using the Submissions part for the challenge allowed me to see the test case which failed and debug - I foolish put the same str method twice for two keys which was tripping me up
    * Last Challenge for this growing file is the `text wrap`: We are slicing through a string to print a new line of characters for a particular width to the end of the string. Good use of mutating iterator values against stop indexes for the slice as well as use of `math.ceil` and `math.floor` for conditionally checking how long the loop should run prior to printing out the remaining characters of the string
        - Also converting list items to a multiline string for the requested output 
* [**`Third Set`**](/HackerRank/entry_easy/third_set.py)
    * `Designer Doormat` - This is a good custom output of a print statement with manipulation of a str pattern to a break point. Symmetrical type pattern building
    * `Strings - Alphabet Rangoli` - In motion here but good challenge for nested loop and fluctuating index values to grab "keys" in a sorted alphabet dictionary. 
    * `Strings - Capitalize` - Pretty simple one here ... or not, we need to preserve spaces so we can use a regular expression to split at non-whitespace characters
        ```python
        >>> tcase = 'Hello   World  Lol'
        >>> len(tcase)
        18
        >>> cap_exp = ['hello', '   ', 'world', '  ', 'lol']
        >>> ''.join(cap_exp)
        'hello   world  lol'
        >>> len(''.join(cap_exp))
        18
        >>> import re
        >>> re.split(r'(\s+)', 'hello   world  lol')
        ['hello', '   ', 'world', '  ', 'lol']
        >>> big_s = ['hello', '   ', 'world', '  ', 'lol']
        >>> [x.title() if x[0].isalpha() else x for x in big_s]
        ['Hello', '   ', 'World', '  ', 'Lol']
        >>> title = [x.title() if x[0].isalpha() else x for x in big_s]
        >>> len(title)
        5
        >>> title
        ['Hello', '   ', 'World', '  ', 'Lol']
        >>> len(''.join(title))
        18
        >>> ''.join(title)
        'Hello   World  Lol'
        ```
* [**`Fourth Set`**](/HackerRank/entry_easy/fourth_set.py)
    * `Itertools.product` itertools.product() This tool computes the cartesian product of input iterables. It is equivalent to nested for-loops. For example, product(A, B) returns the same as ((x,y) for x in A for y in B).
        - You are given a two lists A and B. Your task is to compute their cartesian product X.
    * `Itertools.permutations` - You are given a string S. Your task is to print all possible permutations of size l of the string in lexicographic sorted order.
    * `collections.Counter` - Raghu is a shoe shop owner. His shop has X number of shoes.
    He has a list containing the size of each shoe he has in his shop.
    There are N number of customers who are willing to pay  xi amount of money only if they get the shoe of their desired size.
    Your task is to compute how much money Raghu earned. Here is a fairly straight forward use to create a counter object for key/index count than can use a dctionary properties to decrement the keys as we receive input for customers if the size is available or not
    * `Default Dict - collections` - More input and print out for conditional checking of a default_dict and assigning a "index" value should the value of an input be equal to a seen letter for the amount of iterations as dicated by the number gathered from other input
    * `Collections - Named Tuples`- This was a really good challenge and one they requested in 4/5 lines of code or less. The **named_tuple** takes positional assignment after creating the original prototype object so that once we iterate through the students, we can unpack the input in our list comprehension to create a `student_tuple` object with position assignment provided in the input of subsequent lines for the student's details. Including the code here below for reference
    ```python
        # Enter your code here. Read input from STDIN. Print output to STDOUT
        from collections import namedtuple
        students, student_tuple = int(input()), namedtuple('Student', ' '.join(input().split()))
        student_marks = [int(s.MARKS) for s in [student_tuple(*input().split()) for _ in range(students)]]
        print(sum(student_marks) / students)
    ```
    * Python Code Breakdown above
        - The first line (outside the import), gets the total students and the tuple object uses the the 2ND line of input which has the columns/properties we create with the tuple
        - In the list comprehension, we can create a student tuple object with subsequent lines of then student data input which is in the order from the second input in terms of the properties which the tuple can correctly assign to the properties, it needs the values in a 'str' so we use a **`*`** to pass the lines of student input data to the tuple for as long as the len of student we get from the first input
            - Next in the list comprehension, we can then isolate properties of the tuple object and simply have to turn the assignet str value to an int to get a mathematical sum
    * `Collections : Word Order` - You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification. 
        - Note: Each input line ends with a "\n" character.
        - Good Opportunity for an OrderedDict usage and then can use some of the methods with the object to get the output values. 
        - See further defintion of break down of code in the file

* [**`Fifth Set ... Sets!`**](/HackerRank/entry_easy/fifth_set.py)
    * `Intro : Sets` - This one was pretty straight forward. They just wanted an average of distinct values passed in from the main function. There is a decent map function on a list of strings that was a section of the input received from the challenge. Just recall map takes a function and applies it over the iterable or second argument in the call which you can then commonly chain and place the map's output into another list as this example does
    * `Sets : Symmetric Difference` - Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both. (anti-join)
    * `Sets : (Medium Difficulty) Happiness Index` - Setting of a index by checking of array values in two sets ... not sure why this was ranked as medium difficulty
    * `Sets : Set Add` - Rupal has a huge collection of country stamps. She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of N country stamps. 
        - Used Set comprehension as well as a for loop here for object method calling to accomplish the same result of adding input to a set
    * `Sets : Set functions - discard(), remove(), & pop()` - You have a non-empty set s, and you have to execute N commands given in N lines. The commands will be pop, remove and discard.
        - Take note of how the **`getattr`** method call is used to assign a method call from a passed string argument from an input can be appropriately applied to an instance of a set object.
        - Useful reminder of how if a string is passed to a function how it can be applied to it's object type
            -  [Call Function of Module by Using its Name as String](https://stackoverflow.com/questions/3061/calling-a-function-of-a-module-by-using-its-name-a-string?rq=1)
    * `Sets : Union Operation` - The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers. You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. The same student could be in both sets. Your task is to find the total number of students who have subscribed to at least one newspaper.
        - Fairly straight forward. Union operator similar to **`SQL`** will only select either unique items or matching items (only once .. **no dupes!!**)
    * `Sets : Intersection Operation` - The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed only to French, and some have subscribed to both newspapers. You are given two sets of student roll numbers. One set has subscribed to the English newspaper, one set has subscribed to the French newspaper. Your task is to find the total number of students who havesubscribed to both newspapers.
        - Again .. fairly straight forward here and for this item, we are essentially doing a **inner join** of the two sets where only the matched values in each set is returned or the intersection of both data types
    * `Sets : Difference Operation` - You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to only English newspapers.
        - This is more of an **anti-join** type for one set against another and will return from the left-side set what isn't in the method call
    * `Sets : Symmetric Difference` - You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to either the English or the French newspaper but not both.
        - Unique values in set a or b. Not overlapping values in a venn-diagram
    * [**`Final Set Operations`**](/HackerRank/entry_easy/fifth_stcnt_set.py) - File was growing pretty large above so will start a new file for a few more challenges to round out the set operation challenges
        - `Sets : Mutations` - Here we are similary using the **`gtattr`** to take input from a set number of lines to perform a passed set operation on the input of another operation. We are just mutating a single list with various set values from an iteration of **N** new sets in a loop. We assign the set operation provided from the input onto the master/chief set and mutate the initial set in place based on our received input for a set operation
        - `Sets : The Captain's Room` - Unsure of why a set is needed here. Essentially we are looking for an occurrence of size of guests in a room that has a `count` of K times in a provided list. The only value that isn't the size of `K` is the captain's room which is unique to all the other guests who have K room at their party size
        - `Sets : Check Subset` - See the input details as that's most pertinent for the challenge. Here we are looking two sets with K amount of values for each provided in an input. Our task here is to determine if all values of set A (first input in test case) are of element set B (second set input). Print `True` of `False` if A is a subset of B (B must maintain all values of A)
            - Would appear a simple interesection and count will give us what we need (it did)
        - `Sets: Check Strict Superset` - You are given a set  and  other sets.Your job is to find whether set  is a strict superset of each of the  sets. Print True, if  is a strict superset of each of the  sets. Otherwise, print False.A strict superset has at least one element that does not exist in its subset.
            - Here we just need to perform a similar intersection to confirm the **superset** has all values of the test input set (intersection should equal the length of the test superset). After, another simple length check to confirm that the matching intersection length of super set A and the set B is less than superset A which would qualify as having at least one element more than its' subset

* [**`Sixth Set`**](/HackerRank/entry_easy/sixth_set.py) 
    * `Calendar Module` - The calendar module allows you to output calendars and provides additional useful functions for them. You are given a date. Your task is to find what the day is on that date.
    * `Errors and Exceptions` - Some fairly straight forward try/except block for capturing value errors and zero division type errors when running an operation
    * `Incorrect Regex` - Given strings to find out whether S is a valid regex or not with a try/except block and using the **`re`** 
    * `itertools.combinations` - You are given a string S. Your task is to print all possible combinations, up to size k, of the string in lexicographic sorted order.

* [**`Seventh Set`**](/HackerRank/entry_easy/se7th_set.py)

---

### **Challenges Breakdown Selections** ⛰️

* **`List Comprehensions`**

![List Comp Question](images/l_comprehension_coords.png)
* So trick here is using multiple for loops in the comprehension which are **`nested loops`**
```python
# Let's say for instance we have the values for our input
# x = 1, y = 1, z = 1, n = 2
>>> x, y, z, n = 1, 1, 1, 2
>>> x
1
>>> y
1
>>> z
1
>>> n
2
>>> [[a, b] for a in range(x + 1) for b in range(y+1)]
[[0, 0], [0, 1], [1, 0], [1, 1]]
```
* **`Output Breakdown`**
    - **a** or idx[0] in our list output shows a zero and is the result of the first for loop execution
    - Now once that first 0 is generated for the temp variable **a**, the second for loop with temp variable **b** starts
        * Now as a nested loop in the comprehension (which this is but a little more difficult to see on first glance), the entire for loop for b will run
        * **`Most Imporant Point`** : the chaining of for loops in a list comprehension will work as a nested iteration which in our challenge is very useful as the objective is to create possible permutations of all the different values
* **`Back to Permutations`**
```python
>>> x, y, z, n = 1, 1, 1, 2
>>> permutations = [[a, b, c] for a in range(x+1) for b in range(y+1) for c in range(z+1)]
>>> permutations
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
```
* **`Output Breakdown : Nested Iterations`**
    * The third list index or `permutations[2]` is when the last for loop iteration with variable **`c`** completes
    - as variable **`z`** is **1** the range or loops is range(2) == [0, 1], thus the `permutations[2] & permutations[3]` is the set of iterations run for the second value of **`b`** or 1
        - thus permutations[2][-1] is **`c's`** first iteration of 0 and permutations[3][-1] is **`c's`** second iterations of 1
    *  Now once **`c`** completes for the last value of b, we exit the nested loop back to variable **`a`** which completes it's second and last value of 1 with the possible ranges of `b` and `c` with 

* **`Now Last Part`**
    * Now we need to print an array of the elements/list coordinates that do not sum to the the value of **`n`**
```python
>>> permutations = [[a, b, c] for a in range(x + 1) for b in range(y + 1) for c in range(z + 1)]
>>> ## We have all the permutations now and we need to print the permutations
>>> ## which don't sum to the value of n or our last argument
>>> permutations_not_sum_n = [x for x in permutations if sum(x) != n]
>>> print(permutations_not_sum_n)
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
```