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

def ways_to_climb(h):
    if h==0 or h==1:
          return 1
    if h==2:
          return 2
    else:
          return ways_to_climb(h-1)+ways_to_climb(h-2)

