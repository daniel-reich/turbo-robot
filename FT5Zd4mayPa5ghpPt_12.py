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
    if type(h) == str and (len(h) == 6 or (len(h) == 7 and h[0] == '#')):
        try:
            red, gr, blue = (int(h[-6: -4], 16), int(h[-4: -2], 16),
                             int(h[-2:], 16))
        except ValueError:
            return 'Invalid input!'
        if 0 <= red < 256 and 0 <= gr < 256 and 0 <= blue < 256:
            return {'r': red, 'g': gr, 'b': blue}
    elif type(h) == dict:
        if ('r' in h and 'g' in h and 'b' in h and len(h) == 3
                and 0 <= h['r'] < 256 and 0 <= h['g'] < 256
                and 0 <= h['b'] < 256):
            red, gr, blue = hex(h['r'])[2:], hex(h['g'])[2:], hex(h['b'])[2:]
            return '#{:0>2}{:0>2}{:0>2}'.format(red, gr, blue)
    return 'Invalid input!'

