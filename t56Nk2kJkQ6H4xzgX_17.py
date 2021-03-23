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

def swap_xy(txt):
  import re
  ans = [coordinate.strip() for coordinate in re.split('[\(\),*]', txt) \
  if coordinate.strip()]
  odd = [i for no, i in enumerate(ans) if no%2 == 1]
  even = [i for no, i in enumerate(ans) if no%2 == 0]
  ans = ', '.join(['('+i+', '+j+')' for i, j in zip(odd,even)])
  return ans

