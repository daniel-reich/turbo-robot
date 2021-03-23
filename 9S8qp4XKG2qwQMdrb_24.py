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

from math import factorial
def ways_to_climb(n1,n2=0,total=0):
  total += factorial(n1+n2)//(factorial(n1)*factorial(n2))
​
  if n1 < 2:
    return total
  else:
    n1, n2 = n1-2, n2+1
    return ways_to_climb(n1,n2,total)

