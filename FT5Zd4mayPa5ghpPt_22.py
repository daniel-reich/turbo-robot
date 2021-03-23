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

from PIL import ImageColor
​
def clamp(x):
    return max(0, min(x, 255))
​
def color_conversion(h):
    """[Color Conversion] RGB to HEX and HEX to RGB"""
    if isinstance(h, dict):
        r, g, b = h["r"], h["g"], h["b"]
        
        for c in [r, g, b]:
            if c > 255 or c < 0:
                return "Invalid input!"
        
        return "#{:02x}{:02x}{:02x}".format(r, g, b)
    else:
        try:
            if h.count("#") == 0:
                h = "#" + h
            r, g, b = ImageColor.getcolor(h, "RGB")[:]
            return {"r": r, "g": g, "b": b}
        except:
            return "Invalid input!"

