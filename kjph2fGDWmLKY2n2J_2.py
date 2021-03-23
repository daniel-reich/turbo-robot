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
  x = re.search('^rgb\(\s*([0-9]{1,2}\%?|1[0-9]{2}|2[0-4][0-9]|25[0-5]|100\%)\s*,\s*([0-9]{1,2}\%?|1[0-9]{2}|2[0-4][0-9]|25[0-5]|100\%)\s*,\s*([0-9]{1,2}\%?|1[0-9]{2}|2[0-4][0-9]|25[0-5]|100\%)\s*\)$|^rgba\(\s*([0-9]{1,2}\%?|1[0-9]{2}|2[0-4][0-9]|25[0-5]|100\%)\s*,\s*([0-9]{1,2}\%?|1[0-9]{2}|2[0-4][0-9]|25[0-5]|100\%)\s*,\s*([0-9]{1,2}\%?|1[0-9]{2}|2[0-4][0-9]|25[0-5]|100\%)\s*,\s*(0?(\.\d+)?|1(\.0)?)\s*\)$', color)
  if x:
    return True
  return False

