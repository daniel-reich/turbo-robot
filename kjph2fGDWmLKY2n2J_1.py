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
​
open_ = r"^rgb(a)?\(\s*"
rgb = r"(25[0-5]|2[0-4]\d|1?\d?\d|100%|\d?\d%)"
comma = r"\s*,\s*"
alpha = r"\s*(?(1),\s*((?:0?\.\d*)?\d{1,3})\s*\)|\))?"
combined = "".join((open_, comma.join([rgb] * 3), alpha))
​
def valid_color (color):
  match = re.fullmatch(combined, color)
  if match is None:
    return False
  return True

