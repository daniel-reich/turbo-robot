"""


You are given a **list of binary integers** and `k`, the **number of flips**
allowed.

Write a function that returns the indices of zeroes of which, when flipped,
return the **longest contiguous sequence of ones**.

### Examples

    zero_indices([1, 0, 1, 1, 0, 0, 0, 1], 1) ➞ [1]
    
    zero_indices([1, 0, 0, 0, 0, 1], 1) ➞ [1]
    
    zero_indices([1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0], 3) ➞ [6, 7, 9]
    
    zero_indices([1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0], 3) ➞ [7, 8, 9]

### Notes

If multiple combinations of indices tie for longest one sequence, return the
indices which occur **first** (see examples #2, #3).

"""

from itertools import combinations
​
def zero_indices(lst, k):
  indices = [idx for idx, i in enumerate(lst) if not i]
  combos = [list(i) for i in combinations(indices, k)]
  
  return max(combos, key=lambda x: longest_run(flip_bits(lst, x)))
  
def flip_bits(lst, combo):
  return [i or int(idx in combo) for idx, i in enumerate(lst)]
  
def longest_run(lst):
  return max(len(i) for i in ''.join(map(str, lst)).split('0'))

