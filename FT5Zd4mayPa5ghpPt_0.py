"""


Create a function that converts RGB to HEX and vice versa.

`color_conversion("#ff09d3")` converts the string param from HEX to RGB.
`color_conversion({"r": 235, "g": 64, "b": 52})` converts the dict param from
RGB to HEX.

### Examples

    color_conversion("#ffffff") ➞ {"r": 255, "g": 255, "b": 255}
    
    color_conversion("#ff0025") ➞ {"r": 255, "g": 0, "b": 37}
    
    color_conversion({"r": 40, "g": 200, "b": 125}) ➞ "#28c87d"
    
    color_conversion({"r": -1, "g": 0, "b": 256}) ➞ "Invalid input!"
    
    color_conversion("c9bade") ➞ {"r": 201, "g": 186, "b": 222}

### Notes

  * The **_RGB_** value must be between 0 and 255.
  * Hex value input can be prefixed with a hash (`#`) or without (see example #5).

"""

import re
​
def color_conversion(h):
  if type(h) is str:
    if not bool(re.match('#?[0-9a-f]{6}$', h)): 
      return 'Invalid input!'
    r, g, b = re.findall('#?(..)(..)(..)', h)[0]
    return {'r': int(r, 16), 'g': int(g, 16), 'b': int(b, 16)}
  else:
    if any(i not in range(256) for i in h.values()): 
      return 'Invalid input!'
    return '#{:02x}{:02x}{:02x}'.format(h['r'], h['g'], h['b'])

