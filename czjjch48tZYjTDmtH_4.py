"""


For this task, you will write two validators.

  1.  **Shift Validator:** When each element is translated (added or subtracted) by a constant.
  2.  **Multiple Validator:** When each element is multiplied (by a positive or negative number) by a constant.

A few examples to illustrate these respective functions:

### Examples

    is_shifted([1, 2, 3], [2, 3, 4]) ➞ True
    # Each element is shifted +1
    
    is_shifted([1, 2, 3], [-9, -8, -7]) ➞ True
    # Each element is shifted -10
    
    is_multiplied([1, 2, 3], [10, 20, 30]) ➞ True
    # Each element is multiplied by 10
    
    is_multiplied([1, 2, 3], [-0.5, -1, -1.5]) ➞ True
    # Each element is multiplied by -1/2
    
    is_multiplied([1, 2, 3], [0, 0, 0]) ➞ True
    # Each element is multiplied by 0

### Notes

  * The given lists are the same length.
  * Keep in mind one special case: if the **second list** is a list of **only zeroes** , then the first list can be anything (the multiplier will be `0`).

"""

def is_shifted(lst1, lst2):
  shift = lst2[0]-lst1[0] 
  for i in range(0, len(lst1)):
      if lst1[i] + shift == lst2[i]:
        continue
      else:
        return False
  return True
​
def is_multiplied(lst1, lst2):
  multi = lst2[0]/lst1[0]
  for i in range(0,len(lst1)):
    if lst1[i]*multi == lst2[i]:
      continue
    else:
      return False
  return True
