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

import string
def color_conversion(h):
   if type(h) is str:
       if all(c in string.hexdigits+'#' for c in h):
            if h[0]!='#' and len(h)==6:
               a = hex2rgb('#'+h)
               return({'r': a[0], 'g': a[1],'b': a[2]})
            elif h[0]!='#' and len(h)!=6:
               return ('Invalid input!')
            else:
               a = hex2rgb(h)
               return({'r': a[0], 'g': a[1], 'b': a[2]})
       else:
               return('Invalid input!')
   else:
      if h['r'] >=0 and h['g']>=0 and h['b']>=0 and h['r'] <=255 and h['g']<=255 and h['b']<=255  :
         return('#'+rgb2hex((h['r'],h['g'],h['b'])))
      else: return('Invalid input!')
​
def rgb2hex(rgb):
    return '%02x%02x%02x' % rgb
​
def hex2rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3))

