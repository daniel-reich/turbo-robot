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
    str1 = txt[txt.index('(') + 1 : txt.index(',')]
    str2 = txt[txt.index(',') + 2 : txt.index(')')]
    str3 = txt[txt.rindex('(') + 1 : txt.rindex(',')]
    str4 = txt[txt.rindex(',') + 2 : txt.rindex(')')]
    return '({}, {}), ({}, {})'.format(str2, str1, str4, str3)

