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
  to_hex = lambda n: ('0'+hex(n)[2:])[-2:]
  if type(h) is dict:
    r, g, b = h['r'], h['g'], h['b']
    if any([x < 0 or 255 < x for x in [r, g, b]]): return 'Invalid input!'
    return '#{}{}{}'.format(to_hex(r), to_hex(g), to_hex(b))
  if not bool(re.search(r'\A#?[0-9a-f]{6}\Z', h)): return 'Invalid input!'
  r, g, b = re.findall(r'(?:.{2})', h.strip('#'))
  return {'r': int('0x'+r, 16), 'g': int('0x'+g, 16), 'b': int('0x'+b, 16)}

