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
    s = {1, 2}
    cache = [0 for _ in range(n + 1)]
    cache[0] = 1
    for i in range(n + 1):
        cache[i] += sum(cache[i - x] for x in s if i - x > 0)
        cache[i] += 1 if i in s else 0
    return cache[-1]

