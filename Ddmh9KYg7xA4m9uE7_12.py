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
  a = string.lower()
  ans = ""
  for i in range(0 , len(a)):
    if ord(a[i]) >= 97 and ord(a[i]) <= 109:
      ans += "0"
    else:
      ans += "1"
  return ans

