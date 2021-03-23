"""


Given a string `worm` create a function that takes the length of the worm and
converts it into millimeters. Each `-` represents one centimeter.

### Examples

    worm_length("----------") ➞ "100 mm."
    
    worm_length("") ➞ "invalid"
    
    worm_length("---_-___---_") ➞ "invalid"

### Notes

Return `"invalid"` if an empty string is given or if the string has characters
other than `-`.

"""

def worm_length(worm):
  if worm=='':
    return 'invalid'
  for i in worm:
    if i!='-':
      return 'invalid'
  else:
    return str(len(worm)*10)+' mm.'

