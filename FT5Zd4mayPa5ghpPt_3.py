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

def cc_str_to_hex(s):
    s = s.replace('#', '')
    if len(s) != 6:
        return "Invalid input!"
    try:
        return {'r': int("0x" + s[:2], 16), 'g': int("0x" + s[2:4], 16), 'b': int("0x" + s[4:], 16)}
    except:
        return "Invalid input!"
    
def cc_hex_to_str(h):
    if min(h.values()) < 0 or max(h.values()) > 255:
        return "Invalid input!"
    return '#' + hex(h['r'])[2:].zfill(2) + hex(h['g'])[2:].zfill(2) + hex(h['b'])[2:].zfill(2)
​
def color_conversion(h):
    return cc_str_to_hex(h) if type(h) == str else cc_hex_to_str(h)

