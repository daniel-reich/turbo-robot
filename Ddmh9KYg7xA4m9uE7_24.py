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
  result = []
  for i in string:
    if i == "a" or i == "A" or i == "b" or i == "B" or i == "c" or i == "C" or i == "d" or i == "D" or i == "e" or i == "E" or i == "f" or i == "F" or i == "g" or i == "G" or i == "h" or i == "H" or i == "i" or i == "I" or i == "j" or i == "J" or i == "k" or i == "K" or i == "l" or i == "L" or i == "m" or i == "M":
      result.append("0")
    else:
      result.append("1")
  return "".join(result)

