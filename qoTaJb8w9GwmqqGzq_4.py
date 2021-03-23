"""


Create a function that returns `True` if the first list is a **subset** of the
second. Return `False` otherwise.

### Examples

    is_subset([3, 2, 5], [5, 3, 7, 9, 2]) ➞ True
    
    is_subset([8, 9], [7, 1, 9, 8, 4, 5, 6]) ➞ True
    
    is_subset([1, 2], [3, 5, 9, 1]) ➞ False

### Notes

Both lists will contain only unique values.

"""

def is_subset(lst1, lst2):
  for n in lst1:
    if n not in lst2 :
      return False
  return True

