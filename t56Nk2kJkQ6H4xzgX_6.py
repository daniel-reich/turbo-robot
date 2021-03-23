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
    lst = [int(d) for d in re.findall(r'-?\d+', txt)]
    for i in range(0, 3, 2):
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return '(%d, %d), (%d, %d)' % (lst[0], lst[1], lst[2], lst[3])

