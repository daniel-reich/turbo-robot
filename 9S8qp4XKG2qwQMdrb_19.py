"""


Write a function that returns the number of ways a person can climb **n
stairs** , where the person may only climb **1** or **2** steps at a time.

To illustrate, if **n = 4** there are **5** ways to climb:

    [1, 1, 1, 1]
    [2, 1, 1]
    [1, 2, 1]
    [1, 1, 2]
    [2, 2]

### Examples

    ways_to_climb(1) ➞ 1
    
    ways_to_climb(2) ➞ 2
    
    ways_to_climb(5) ➞ 8

### Notes

A staircase of height `0` should return `1`.

"""

def ways_to_climb(n):
    if n <= 1:
        return 1
    ways = {step: 0 for step in range(n + 1)}
    ways[0] = 1
    for step in range(n - 1):
        ways[step+1] += ways[step]
        ways[step+2] += ways[step]
    ways[n] += ways[n-1]
    return ways[n]

