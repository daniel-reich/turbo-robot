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
  regex1 = re.compile(r'^(rgb)\(\s?(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]%?|[0-9]%?|100%)\s?,'
                      r'\s?(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]%?|[0-9]%?|100%)\s?,'
                      r'\s?(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]%?|[0-9]%?|100%)\s?\)')
  regex2 = re.compile(r'^(rgba)\(\s?(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]%?|[0-9]%?|100%)\s?,'
                      r'\s?(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]%?|[0-9]%?|100%?)\s?,'
                      r'\s?(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]%?|[0-9]%?|100%)\s?,'
                      r'\s?([01]|0\.\d{1,}|\.\d{1,})\s?\)')
  
  if 'rgba' in color:
    return bool(re.match(regex2, color))
  else:
    return bool(re.match(regex1, color))

