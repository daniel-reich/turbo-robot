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

def num_ways(n, s):
    '''
    Returns the number of ways to climb n stairs with each of the number of
    stairs in set s: assumed to go from 1 to a maximum value e.g {1,2,3}.
    '''
    m = max(s)
    temp = 0
    result = [1]
​
    for i in range(1, n + 1):
        j = i - m - 1
        k = i - 1
        if j >= 0:  # i.e possible for this value of i
            temp -= result[j]  # remove elements of previous window
        temp += result[k]
        result.append(temp)
​
    return result[n]

