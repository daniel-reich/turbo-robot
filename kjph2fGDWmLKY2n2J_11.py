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
  p = re.compile('rgb(|a)\(((\d|\.|\%|\s)*,){2,3}(\d|\.|\%|\s)*\)')
  if not re.match(p, color):
    return False
  is_rgba = 'a' in color
  values = color[(5 if is_rgba else 4):-1].split(',')
  if is_rgba and len(values) == 4:
    rgb = values[:3]
    if not 0 <= float(values[3]) <= 1:
      return False
  elif not is_rgba and len(values) == 3:
    rgb = values
  else:
    return False
  try:
    rgb = [float(v) if '%' not in v else float(v.replace('%', ''))*2.55 for v in rgb]
  except:
    return False
  return all(0 <= v <= 255 for v in rgb)

