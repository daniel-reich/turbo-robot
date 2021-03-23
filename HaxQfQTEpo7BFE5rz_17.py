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
  if 0 in lst:
    return False
  l = []
  evens = [lst[i] for i in range(0, len(lst), 2)]
  odds = [lst[i] for i in range(1, len(lst), 2)]
  if lst[0] > 0:
    for i in evens:
      if i < 0:
        l.append(False)
    for i in odds:
      if i > 0:
        l.append(False)
  if lst[0] < 0:
    for i in evens:
      if i > 0:
        l.append(False)
    for i in odds:
      if i < 0:
        l.append(False)
  return all(l)

