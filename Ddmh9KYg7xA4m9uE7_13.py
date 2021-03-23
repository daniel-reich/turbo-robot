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

def convert_binary(s):
  s = list(s.lower())
  lst = []
  for l in s:
    if ord(l) in range(97, 110):
      lst.append('0')
    elif ord(l) in range(109, 123):
      lst.append('1')
  return ''.join(lst)

