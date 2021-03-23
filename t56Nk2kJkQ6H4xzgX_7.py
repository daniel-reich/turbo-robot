"""


Write a function that swaps the X and Y coordinates in a string.

### Examples

    swap_xy("(1, 2), (3, 4)") ➞ "(2, 1), (4, 3)"
    
    swap_xy("(11, 23), (43, 99)") ➞ "(23, 11), (99, 43)"
    
    swap_xy("(-5, -3), (7, 4)") ➞ "(-3, -5), (4, 7)"

### Notes

  * Some numbers have multiple digits.
  * Some numbers will be negative.

"""

import re
def swap_xy(txt):
  nums = [int(x) for x in re.findall('-?[0-9]+',txt)]
  j = str([tuple(nums[:2][::-1]), tuple(nums[2:][::-1])])
  return j.strip('[]')

