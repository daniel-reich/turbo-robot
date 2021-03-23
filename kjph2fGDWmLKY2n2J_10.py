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
def valid_color(color):
  pattern = ['rgb\(({0}),({0}),({0})\)'.format('[\s\t]*[\d\.%]+[\s\t]*'),
    'rgba\(({0}),({0}),({0}),({0})\)'.format('[\s\t]*[\d\.\%]+[\s\t]*')]
  return any(valid_pattern(p, color) for p in pattern)
  
def valid_pattern(pattern, color):
  match = re.findall(pattern, color)
  if not match:
    return False
  match = match[0]
  if len(match) == 3:
    return all(valid_c(color) for color in match)
  return all(valid_c(color) for color in match[:-1])\
    and valid_c(match[-1], 'alpha')
    
def valid_c(c, t=''):
  n = eval(c.replace('%','/100'))
  if ('%' in c) or (t == 'alpha'):
    return 0<=n<=1
  return 0<=n<=255

