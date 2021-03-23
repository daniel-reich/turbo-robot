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
  max_length = 0
  index = 0
  flips = k
  for i in range(len(lst)):
    length = 0
    for j in range(i, len(lst)):
      if lst[j] == 0:
        if flips == 0: break
        flips -= 1
      length += 1
    if length > max_length:
      max_length = length
      index = i
    flips = k
  indicies = []
  for i in range(index, min(len(lst), index + max_length)):
    if lst[i] == 0:
      indicies.append(i)
  return indicies

