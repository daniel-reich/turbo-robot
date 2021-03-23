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
        if not re.search(r"^#?[a-f0-9]{6}$", h):
            return "Invalid input!"
        color = ["r", "g", "b"]
        size = len(h)
        if size == 6:
            start = 0
        else:
            start = 1
        value = [int(h[i:i+2], 16) for i in range(start, size, 2)]
        return {c: value[i] for i, c in enumerate(color)}
    red, green, blue = h["r"], h["g"], h["b"]
    if (red < 0 or red > 255) or (green < 0 or green > 255) or (blue < 0 or blue > 255):
        return "Invalid input!"
    return "#" + "".join("0" + hex(ch)[2:] if len(hex(ch)[2:]) == 1 else hex(ch)[2:] for ch in [red, green, blue])

