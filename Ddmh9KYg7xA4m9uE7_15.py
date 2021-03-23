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

import re
def convert_binary(string):
  bin=""
  for i in string:
    if re.match(r"[a-mA-M]", i):
      bin+="0"
    else:
      bin+="1"
  return bin

