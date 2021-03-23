"""


Write a function that returns `True` if an integer can be expressed as a power
of base value 2 and `False` otherwise.

### Examples

    power_of_two(32) ➞ True
    
    power_of_two(1) ➞ True
    
    power_of_two(18) ➞ False

### Notes

N/A

"""

import math
​
def power_of_two(num):
  if num == 1:
      return True
  for i in range(1, num):
    if num == 2**i:
      return True
  return False

