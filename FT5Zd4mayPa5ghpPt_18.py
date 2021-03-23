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
  if isinstance(h, str):
    rgb = h.strip('#')
    if not re.match(r'^[a-f0-9]{6}$', rgb):
      return 'Invalid input!'
    red, green, blue = rgb[:2], rgb[2:4], rgb[4:]
    colors = []
    for color in (red, green, blue):
      value = int(color, base=16)
      if value < 0 or value > 255:
        return 'Invalid input!'
      colors.append(value)
    return {
      color: val
      for color, val in zip(['r', 'g', 'b'], colors)
    }
  else:
    order = ['r', 'g', 'b']
    colors = []
    for color, val in sorted(h.items(), key=lambda x: order.index(x[0])):
      if val < 0 or val > 255:
        return 'Invalid input!'
      colors.append('{:0>2x}'.format(val))
    return '#{}'.format(''.join(colors))

