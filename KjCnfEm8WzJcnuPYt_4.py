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
def zero_indices(lst, k):
  curr = (0,0,0)
  highest = longest_one_length(lst)
  possidx = [idx for idx in combinations(range(len(lst)),k)]
  
  #remove possible flips that are already 1s, not needed
  for i in range(0,len(possidx),-1):
    if any(lst[j] == 1 for j in possidx[i]):
      possidx.pop(i)
      
  #find the set of flips with the longest 1s
  for check in possidx:
    guess = [1 if i in check else lst[i] for i in range(len(lst))]
    ln = longest_one_length(guess)
    if ln > highest:
      highest = ln
      curr = check
  return list(curr)
  
def longest_one_length(lst):
  count = 0
  highest = 0
  for i in lst:
    if i:
      count += 1
    else:
      if count > highest:
        highest = count
      count = 0
  if count > highest:
    highest = count
  return highest

