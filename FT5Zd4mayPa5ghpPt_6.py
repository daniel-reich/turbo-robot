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

hex = '0123456789abcdef'
​
def color_conversion(h):
  if type(h) == str:
    if any(x not in hex+'#' for x in h):
      return "Invalid input!"
    if h[0]=='#' and len(h)==7:
      return {'r':hex_to_num(h[1:3]), 'g':hex_to_num(h[3:5]), 'b':hex_to_num(h[5:7])}
    elif h[0]!='#' and len(h)==6:
      return {'r':hex_to_num(h[0:2]), 'g':hex_to_num(h[2:4]), 'b':hex_to_num(h[4:6])}
    else:
      return "Invalid input!"
  else:
    if all(0<=h[x]<256 for x in ['r','g','b']):
      return '#{}{}{}'.format(*[num_to_hex(h[x]) for x in ['r','g','b']])
    else:
      return "Invalid input!"
    
def hex_to_num(str):
  return hex.index(str[0])*16+hex.index(str[1])
def num_to_hex(n):
  return hex[n//16]+hex[n%16]

