"""


Create a function that takes a string `str` and performs simple encoding as
per the following method:

  * Replace all single occurrence characters with `[`
  * Replace all characters with **two or more** occurrences with `]`

Return the final string after modification.

### Examples

    simple_encoder("Mubashir") ➞ "[[[[[[[["
    # '[' for each character
    
    simple_encoder("Matt") ➞ "[[]]"
    # ']' for both 't'
    
    simple_encoder("eD  aBiT") ➞ "[[]][[[["
    # Two spaces in between

### Notes

  * Strings can contain lower and uppercase letters. Treat them equally (i.e. A = a, B = b).
  * Spaces are also characters.

"""

def simple_encoder(s):
  encode = ''
  s = s.lower()
  for elem in s:
    if s.count(elem) >=2:
      encode += ']'
    else:
      encode += '['
  return encode

