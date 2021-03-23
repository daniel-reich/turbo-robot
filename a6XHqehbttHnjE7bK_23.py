"""


A repdigit is a positive number composed out of the same digit. Create a
function that takes an integer and returns whether it's a repdigit or not.

### Examples

    is_repdigit(66) ➞ True
    
    is_repdigit(0) ➞ True
    
    is_repdigit(-11) ➞ False

### Notes

  * The number `0` should return `True` (even though it's not a positive number).
  * Check the **Resources** tab for more info on repdigits.

"""

def is_repdigit(num):
  try:
    lst=[int(x) for x in str(num)]
    if num < 0:
      return False
    if num == 0:
      return True
    for i in lst:
      if lst.count(i) == len(lst):
        return True
    else: return False
  except : return False

