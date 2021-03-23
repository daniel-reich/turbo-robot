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
  indices = []
  for i,element in enumerate(lst):
    if element == 0:
      indices.append(i)
  
  max_count = 0
  count = 0
  total_zeros = len(indices)
  
  result = []
  
  for i in range(total_zeros - (k - 1)):
    subarr = indices[i: i + k]
    for j in range(len(lst)):
      if lst[j] == 1 or j in subarr:
        count += 1
      else:
        if count > max_count:
          max_count = count 
          result = subarr 
        count = 0
  
  if count > max_count:
    max_count = count
    result = subarr
    
  return result

