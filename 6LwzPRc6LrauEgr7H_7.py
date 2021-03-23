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
  length = 0 
  
  
  for l in worm:
    if l != "-":
      return "invalid"
    else:
      length = length + 1
      
  
  if length == 0:
    return "invalid"
  else:
    length = length * 10
    string = str(length) + " " + "mm."
    return string

