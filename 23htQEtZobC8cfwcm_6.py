"""


Create a function that returns `True` if smaller lists can concatenate to form
the target list and `False` otherwise.

### Examples

    canConcatenate([[1, 2, 3, 4], [5, 6], [7]], [1, 2, 3, 4, 5, 6, 7]) ➞ True
    
    canConcatenate([[2, 1, 3], [5, 4, 7, 6]], [7, 6, 5, 4, 3, 2, 1]) ➞ True
    
    canConcatenate([[2, 1, 3], [5, 4, 7, 6, 7]], [1, 2, 3, 4, 5, 6, 7]) ➞ False
    # Duplicate 7s not found in target list.
    
    canConcatenate([[2, 1, 3], [5, 4, 7]], [1, 2, 3, 4, 5, 6, 7]) ➞ False
    # Missing 6 from target list.

### Notes

  * Lists do not have to be sorted (see example #2).
  * Lists should concatenate to create the final list exactly (see examples #3 and #4).

"""

def canConcatenate(lst, target):
  k = []
  for index in lst:
    k += index
  k.sort()
  target.sort()
  return k == target

