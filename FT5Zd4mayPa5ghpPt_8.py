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
    if isinstance(h, str):
        h = h[1:] if h[0] == '#' else h
        if any(x not in '#0123456789abcdef'for  x in h ) or len(h) > 6:
            return 'Invalid input!'
        else:
            values = {x: i for i, x in enumerate('0123456789abcdef')}
            t = list(zip(h, h[1:]))[::2]
            return {x: values[t[i][0]] * 16 + values[t[i][1]] for i, x in enumerate('rgb')}
    else:
        if any(x < 0 or x > 255 for x in h.values()):
            return 'Invalid input!'
        else:
            values = {i: x for i, x in enumerate('0123456789abcdef')}
            return ''.join(['#'] + [str(values[h[x] // 16]) + str(values[h[x]%16]) for x in 'rgb'])

