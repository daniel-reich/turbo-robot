"""


Create a function which validates whether a given list **alternates** between
_positive_ and _negative_ numbers.

### Examples

    alternate_pos_neg([3, -2, 5, -5, 2, -8]) ➞ True
    
    alternate_pos_neg([-6, 1, -1, 4, -3]) ➞ True
    
    alternate_pos_neg([4, 4, -2, 3, -6, 10]) ➞ False

### Notes

  * Lists can be of any length.
  * It doesn't matter if a list begins/ends with a positive or negative, as long as it alternates.
  * If a list contains 0, return `False` (as it is neither positive nor negative).

"""

def alternate_pos_neg(lst):
  i = 0
  k = 0
  if lst.count(0):
    return False
  while i < len(lst):
    if lst[i] < 0:
      k += 1
    i += 1
    if i == len(lst):
      break
    if lst[i] > 0:
      k += 1
    i += 1
  return k == 0 or k == len(lst)

