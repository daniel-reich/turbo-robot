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
        if h[0] == '#':
            h = h[1:]
        if len(h) != 6:
            return 'Invalid input!'
        for x in h:
            if x not in '0123456789abcdef':
                return 'Invalid input!'
        return {'r':int(h[:2], 16),
                'g':int(h[2:4], 16),
                'b':int(h[4:], 16)}
    z = [hex(x)[2:].zfill(2)
         for x in [h['r'], h['g'], h['b']]
         if 0 <= x <= 255]
    if len(z) != 3:
        return 'Invalid input!'
    return '#' + z[0] + z[1] + z[2]

