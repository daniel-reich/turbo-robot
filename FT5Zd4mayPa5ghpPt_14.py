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
    conversion = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "a": 10, "b": 11,
                  "c": 12, "d": 13, "e": 14, "f": 15}
    inv_conversion = {v: k for k, v in conversion.items()}
    if type(h) == str:
        avail_chars = ["#", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        valid = True
        for x in h:
            valid = valid and (x in avail_chars)
​
        if valid:
            if len(h) == 6:
                r = 16 * conversion[h[0]] + conversion[h[1]]
                g = 16 * conversion[h[2]] + conversion[h[3]]
                b = 16 * conversion[h[4]] + conversion[h[5]]
​
                return {"r": r, "g": g, "b": b}
            elif len(h) == 7 and h[0] == "#":
                r = 16 * conversion[h[1]] + conversion[h[2]]
                g = 16 * conversion[h[3]] + conversion[h[4]]
                b = 16 * conversion[h[5]] + conversion[h[6]]
​
                return {"r": r, "g": g, "b": b}
            else:
                return "Invalid input!"
        else:
            return "Invalid input!"
    elif type(h) == dict:
        r = h["r"]
        g = h["g"]
        b = h["b"]
​
        string = "#"
​
        if r >= 0 and g >= 0 and b >= 0:
            if r <= 255 and g <= 255 and b <= 255:
                string = string + inv_conversion[(r - r%16) / 16] + inv_conversion[r%16]
                string = string + inv_conversion[(g - g%16) / 16] + inv_conversion[g%16]
                string = string + inv_conversion[(b - b % 16) / 16] + inv_conversion[b % 16]
                return string
            else:
                return "Invalid input!"
        else:
            return "Invalid input!"
    else:
        return "Invalid input!"

