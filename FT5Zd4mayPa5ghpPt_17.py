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
    if type(h) == dict:
        for i in h:
            if h[i] < 0 or h[i] > 255:
                return "Invalid input!"
        r = hex(h["r"])[2:]
        g = hex(h["g"])[2:]
        b = hex(h["b"])[2:]
        return "#{}{}{}".format(r.zfill(2), g.zfill(2), b.zfill(2))
    else:
        ok = "1234567890abcdef"
        h = h.replace("#", "")
        if not all([i in ok for i in h]) or len(h) != 6:
            return "Invalid input!"
        r = int(h[:2], 16)
        g = int(h[2:4], 16)
        b = int(h[4:], 16)
        return {"r" : r, "g" : g, "b" : b}

