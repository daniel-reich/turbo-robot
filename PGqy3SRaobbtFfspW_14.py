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

import itertools
def simple_pair(lst, n):
  pairs = list(itertools.combinations(lst, 2))
  result = [pair for pair in pairs if (pair[0] * pair[1]) == n]
  return list(result[0]) if len(result) != 0 else None

