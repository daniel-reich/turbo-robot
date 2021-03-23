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
  lst = list(map(str, lst))
  best_run = 0
  indices = ()
  
  zero_positions = [idx for idx, i in enumerate(lst) if i == '0']
  for comb in combinations(zero_positions, k):
    arr = lst[:]
    for i in comb:
      arr[i] = '1'
    max_run = max(len(i) for i in ''.join(arr).split('0'))
    if max_run > best_run:
      best_run = max_run
      indices = comb
      
  return list(indices)

