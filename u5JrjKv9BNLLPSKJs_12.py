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

def basis_steps(height, steps):
    if height == 0:
        return 1
    elif height < 0:
        return 0
    total = 0
    for i in steps:
        total += basis_steps(height-i, steps)
    return total
​
​
def steps_dict(steps):
    d = {0: 1}
    for i in range(1, max(steps) + 1):
        d[i] = basis_steps(i, steps)
    return d
​
​
def num_ways(height, steps) -> int:
    d = steps_dict(steps)
    if height in d:
        return d[height]
    for i in range(max(steps) + 1, height + 1):
        d[i] = 0
        for j in steps:
            d[i] += d[i-j]
    return d[height]

