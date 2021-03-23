"""


In the Recursive Staircase Problem, your task is to find the number of ways of
climbing a staircase of `n` stairs, with a set `s` possible steps. The example
below shows that if `n` was `2` and `s` was `{ 1, 2 }`, the answer would be
`2`:

           _
       _ |2  You could either go from step 0-2 (because the set s contains 2), or
    _ | 1    you could go from 0-1-2 (because the set s contains 1, taking one step at a time).
    0

More examples below.

### Examples

    num_ways(4, { 1, 2 }) ➞ 5
    
    num_ways(3, { 1, 2, 3 }) ➞ 4
    
    num_ways(10, { 1, 2, 3, 4 }) ➞ 401

### Notes

The more efficient your solution the better. Do not use unecessary recursion
as this will mean the program needs far longer to complete the tests.

"""

def new_ways(a,b):
    l = len(b)
    temp = [0 for x in range(a)]
    temp[0] = 1
    temp[1] = 1
​
    for i in range(2,a):
        j = 1
        while j <= l and j <= i:
            temp[i] += temp[i-j]
            j += 1
    return temp[a-1]
​
def num_ways(n, s):
    return new_ways(n+1,s)
