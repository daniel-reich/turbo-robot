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
  if len(lst) == 1 and lst[0] == 0:
    return False
  else:
    counter1 = 0
    for i in range(len(lst)-1):
      if (lst[i] >= 0 and lst[i+1] < 0) or (lst[i+1] > 0 and lst[i] < 0):
        counter1 += 1
      else:
        return False
    if counter1 == len(lst)-1:
      return True
    return False

