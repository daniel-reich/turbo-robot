"""


 **Mubashir** needs your help to write a simple algorithm of multiplication.

Given an array of integers `lst` and an integer `n`, find out a pair of
numbers `[x, y]` from a given array such that **x * y = n**.

If the pair is not found, return `None`.

### Examples

    simple_pair([1, 2, 3], 3) ➞ [1, 3]
    
    simple_pair([1, 2, 3], 6) ➞ [2, 3]
    
    simple_pair([1, 2, 3], 9) ➞ None

### Notes

N/A

"""

from itertools import combinations
​
def simple_pair(lst, n):
  return [[list(i) for i in combinations(lst, 2) if i[0] * i[1] == n] or [None]][0][0]

