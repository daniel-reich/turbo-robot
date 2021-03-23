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
​
    if n <= 1 : return 1
    if n == 2 : return 2
​
    res = [0] * (n+ 1)
    res[0] = 1
    res[1] = 1
    res[2] = 2
​
    for i in range(3 , n + 1):
        res[i] = res[i - 1] + res[i-2]
​
    return res[n]

