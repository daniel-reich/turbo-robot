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
  
  Length = len(lst)
  
  if (0 in lst):
    return False
  
  if (Length < 2):
    return True
  
  Group_A = []
  Group_B = []
  
  Counter = 0
  Length = len(lst)
  
  while (Counter < Length):
    
    Item = lst[Counter]
    
    if (Counter % 2 == 0):
      Group_A.append(Item)
      Counter += 1
    else:
      Group_B.append(Item)
      Counter += 1
  
  Test_A1 = min(Group_A)
  Test_A2 = max(Group_A)
  
  Test_B1 = min(Group_B)
  Test_B2 = max(Group_B)
  
  if (Test_A1 > 0) and (Test_B2 < 0):
    return True
  elif (Test_B1 > 0) and (Test_A2 < 0):
    return True
  else:
    return False

