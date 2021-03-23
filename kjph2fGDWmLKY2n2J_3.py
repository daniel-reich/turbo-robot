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
def valid_color (color):
  return bool(re.match("rgb(a)?\((,?((?=\d{1,3}\%)(100|\d{1,2})\%|(25[0-5]|1?\d{1,2}))){3}(?(1),(1\.0*|0?\.?\d+))\)", "".join(color.split()))) and (color.startswith("rgb(") or color.startswith("rgba("))

