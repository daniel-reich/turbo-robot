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

def color_conversion(h):
  if type(h) == str:
    if '#' in h: h = h[1:]
    if len(h) != 6: return 'Invalid input!'
    try:
      ans = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
      return {'g': ans[1], 'r': ans[0], 'b': ans[2]}
    except:
      return 'Invalid input!'
  else:
    if (h['r'] < 0 or h['r'] > 255) or (h['g'] < 0 or h['g'] > 255) or (h['b'] < 0 or h['b'] > 255): return 'Invalid input!'
    return '#%02x%02x%02x' % (h['r'], h['g'], h['b'])

