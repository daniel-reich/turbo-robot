"""


Write a function that returns `True` if two arrays, when combined, form a
**consecutive sequence**. A consecutive sequence is a sequence without any
gaps in the integers, e.g. `1, 2, 3, 4, 5` is a consecutive sequence, but `1,
2, 4, 5` is not.

### Examples

    consecutive_combo([7, 4, 5, 1], [2, 3, 6]) ➞ True
    
    consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]) ➞ False
    
    consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]) ➞ False
    
    consecutive_combo([44, 46], [45]) ➞ True

### Notes

  * The input lists will have unique values.
  * The input lists can be in any order.

"""

def consecutive_combo(lst1, lst2):
  min_of_all = min(min(lst1), min(lst2))
  max_of_all = max(max(lst1), max(lst2))
  if len(range(min_of_all, max_of_all)) + 1 == len(set(lst1)) + len(set(lst2)):
    return True
  return False

