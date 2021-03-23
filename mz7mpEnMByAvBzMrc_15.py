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
def Log2(x):
  if x == 0: return false;
  else: return math.log10(x) / math.log10(2)
  
def power_of_two(num):
  return math.ceil(Log2(num)) == math.floor(Log2(num))

