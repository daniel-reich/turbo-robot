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

def alternate_pos_neg(l):
  
  if 0 in l:
    return False
  else:
    constructor = ['>0','<0'] if l[0] > 0 else ['<0','>0']
​
    for i in range(len(l)):
      if not eval('{}{}'.format(str(l[i]),constructor[i%2])) :
        return False
​
    return True

