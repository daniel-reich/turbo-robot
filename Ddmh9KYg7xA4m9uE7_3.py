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
  ret_str = ""
  for c in string.lower():
    if c in "abcdefghijklm":
      ret_str += "0"
    else:
      ret_str += "1"
  return ret_str

