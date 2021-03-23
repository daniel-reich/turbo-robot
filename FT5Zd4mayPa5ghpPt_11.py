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
def hex_to_rgb(h):
    if not re.match(r'^#?[\da-f]{6}$', h):
        return 'Invalid input!'
    return {'r': int(h[-6:-4], 16), 'g': int(h[-4:-2], 16), 'b': int(h[-2:], 16)}
​
def rgb_to_hex(rgb):
    inRange = lambda c: 0 <= rgb[c] <= 255
    if not (inRange('r') and inRange('g') and inRange('b')):
        return 'Invalid input!'
    hexit = lambda n: hex(n+256)[-2:]
    return '#{}{}{}'.format(hexit(rgb['r']), hexit(rgb['g']), hexit(rgb['b']))
​
def color_conversion(h):
    return hex_to_rgb(h) if type(h) is str else rgb_to_hex(h)

