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

# this seemed more direct than recursion to me
def num_ways(n, s):
    d = {n:1}
    for k in range(n-1, -1, -1):
        cnt = 0
        for j in sorted(s):
            cnt += d.get(k+j, 0)
        d[k] = cnt
    return d[0]

