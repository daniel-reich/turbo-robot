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
  start_point, index, maximum = 0, [], 0
  for num in range(start_point, len(lst)):
    temp_list = [x for x in lst]
    for change in range(k):
      try: temp_list[temp_list.index(0, num)] = 1
      except ValueError: break
    temp_list2 = "".join([str(x) for x in temp_list]).split("0")
    if max([len(x) for x in temp_list2]) > maximum:
      maximum = max([len(x) for x in temp_list2])
      index = [x for x in range(len(lst)) if str(lst[x]) != str(temp_list[x])]
  return index

