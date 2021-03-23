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
  if re.match('rgba? +\(', color): 
    return False
    
  color = ''.join(ch for ch in color if ch not in '   ')
  has_a, r, g, b, a = re.findall('rgb(a)?\(({0})?,({0})?,({0})?(?:,({0}))?\)'.format('[\d.-]+%?'), color)[0]
  
  if (has_a and not 0 <= float(a or -1) <= 1) or (not has_a and a): 
    return False
  
  per = all(i.endswith('%') and 0 <= float(i[:-1]) <= 100 for i in (r, g, b))
  hxd = all(i.isnumeric() and 0 <= float(i) <= 255 for i in (r, g, b))
  
  return per or hxd

