"""


Create a function that takes a number as an argument and returns `True` or
`False` depending on whether the number is symmetrical or not. A number is
symmetrical when it is the same as its reverse.

### Examples

    is_symmetrical(7227) ➞ True
    
    is_symmetrical(12567) ➞ False
    
    is_symmetrical(44444444) ➞ True
    
    is_symmetrical(9939) ➞ False
    
    is_symmetrical(1112111) ➞ True

### Notes

N/A

"""

import math
def is_symmetrical(num):
  num = str(num)
  for x in range(0, math.floor(len(num)/2)):
    if num[x] != num[-1-x]:
      return False
  return True

