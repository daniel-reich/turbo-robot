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

def zero_indices(lst, k):
  from itertools import combinations as co
  l = list(co([i for i in range(len(lst)) if lst[i] == 0], k))
  v = []
  for i in l:
    lst1 = lst[:]
    for j in i:
      lst1[j] = 1
    u = max([len(v) for v in ''.join([str(k) for k in lst1]).split('0')])
    v.append((-u, i))
  v = sorted(v)
  return list(v[0][1])

