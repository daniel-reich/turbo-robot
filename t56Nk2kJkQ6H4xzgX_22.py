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
  s = re.sub(r"\)\, ", ")  ", txt)
  s = re.split("  ", s)
  new_s = []
  for el in s:
    temp = re.findall(r'\-*\d+', el)
    new_s.append("(" + temp[1]+ ", "+ temp[0] + ")")
  return ", ".join(new_s)

