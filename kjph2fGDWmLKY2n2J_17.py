"""


Given an RGB(A) CSS color, determine whether its format is valid or not.
Create a function that takes a string (e.g. `"rgb(0, 0, 0)"`) and return
`True` if it's format is correct, otherwise return `False`.

### Examples

    valid_color("rgb(0,0,0)") ➞ True
    
    valid_color("rgb(0,,0)") ➞ False
    
    valid_color("rgb(255,256,255)") ➞ False
    
    valid_color("rgba(0,0,0,0.123456789)") ➞ True

### Notes

  * Alpha is between 0 and 1.
  * There are a few edge cases (check out the **Tests** tab to know more).

"""

import re
COLOR = re.compile(r'rgba?\((\s*\d+%?)\s*,\s*(\d+%?)\s*,\s*(\d+%?)\s*,?\s*(\d*\.?\d+)?\s*\)$')
​
def valid_color (color):
    nopercent = lambda n: float(n[:-1])/100*255 if n[-1] == '%' else float(n)
    m = COLOR.match(color)
    if not m:
        return False
    if not all(m.groups()[:3]):
        return False
    nnn = tuple(map(nopercent, m.groups()[:3]))
    if ('rgba' in color) != bool(m.group(4)):
        return False
    if m.group(4) and not(0 <= float(m.group(4)) <= 1):
        return False
    return all(map(lambda c: 0<=int(c)<256, nnn))

