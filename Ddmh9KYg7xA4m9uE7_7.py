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
  result = ''
  for ch in string.lower():
    if ord(ch) in range(ord('a'), ord('n')):
      result += '0'
    elif ord(ch) in range(ord('n'), ord('{')):
      result += '1'
    else:
      raise ValueError('Non-alpha character is not allowed.')
  return result

