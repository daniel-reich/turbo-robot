"""


Write a function that transforms all letters from `[a, m]` to `0` and letters
from `[n, z]` to `1` in a string.

### Examples

    convert_binary("house") ➞ "01110"
    
    convert_binary("excLAIM") ➞ "0100000"
    
    convert_binary("moon") ➞ "0111"

### Notes

Conversion should be case **insensitive** (see example #2).

"""

def convert_binary(string):
  zeros = [chr(i) for i in range(97,110)]
  out = ""
  for i in string.lower():
    if i in zeros:
      out += "0"
    else:
      out += "1"
  return out

