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
def valid_color (color):
  if re.search("^rgba", color) != None:
    if re.search("^rgba\(\s?(0?\.?\d*\s?,\s?){3}0?\.?\d*\s?\)$", color) != None:
      return True
    
  elif re.search("^rgb", color) != None:
    if re.search("^rgb\(\s?((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9][0-9]|[0-9])\s?,\s?){2}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9][0-9]|[0-9])\s?\)$", color) != None:
      return True
      
    elif re.search("^rgb\(\s?((100|[0-9][0-9]|[0-9])%\s?,\s?){2}(100|[0-9][0-9]|[0-9])%\s?\)$", color) != None:
      return True
      
  return False

