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
def color_conversion(h):
  if type(h)==str:
    if 'g' not in h:
      if h[0]=='#' and len(h)==7:
        A=['0x'+h[1:][i:i+2] for i in range(0,len(h[1:]),2)]
      elif h[0]!='#' and len(h)==6:
        A=['0x'+h[i:i+2] for i in range(0,len(h),2)]
      else:
        return "Invalid input!"
      d={'r':int(A[0],16), 'g':int(A[1],16), 'b':int(A[2],16)}
      return d
    else:
      return "Invalid input!"
  else:
    if all(0<=h[x]<=255 for x in h):
      return '#{}{}{}'.format(hex(h['r'])[2:].zfill(2), hex(h['g'])[2:].zfill(2), hex(h['b'])[2:].zfill(2))
    else:
      return "Invalid input!"

