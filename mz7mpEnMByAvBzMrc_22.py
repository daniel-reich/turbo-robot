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

from math import log
def power_of_two(num):
  return log(num, 2) % 1 == 0

