"""


Create a function that determines whether a string is a valid hex code.

A hex code must begin with a pound key `#` and is exactly 6 characters in
length. Each character must be a digit from `0-9` or an alphabetic character
from `A-F`. All alphabetic characters may be uppercase or lowercase.

### Examples

    is_valid_hex_code("#CD5C5C") ➞ True
    
    is_valid_hex_code("#EAECEE") ➞ True
    
    is_valid_hex_code("#eaecee") ➞ True
    
    is_valid_hex_code("#CD5C58C") ➞ False
    # Length exceeds 6
    
    is_valid_hex_code("#CD5C5Z") ➞ False
    # Not all alphabetic characters in A-F
    
    is_valid_hex_code("#CD5C&C") ➞ False
    # Contains unacceptable character
    
    is_valid_hex_code("CD5C5C") ➞ False
    # Missing #

### Notes

N/A

"""

def is_valid_hex_code(txt):
  a = ['1','2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','a','b','c','d','e','f']
  s = 0
  
  for i in txt[1:]:
    if i in a:
      s = s
    else:
      s += 1
  
  if len(txt) > 7:
    s += 1
    
  if txt[0] != '#':
    s += 1
  
  return s == 0

