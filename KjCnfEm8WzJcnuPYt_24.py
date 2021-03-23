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

from itertools import combinations as C, groupby as gb
def zero_indices(lst, k):
  A=[i for i, x in enumerate(lst) if not x]
  S=[]
  for x in C(A,k):
    lst2=lst.copy()
    for y in x:
      lst2[y]+=1
    B=[list(g) for t, g in gb(lst2) if t]
    S.append((list(x),len(max(B, key=len))))
  return sorted(S, key=lambda x: (-x[1], x))[0][0]

