"""


Write a function that takes a string and calculates the number of letters and
digits within it. Return the result in a dictionary.

### Examples

    count_all("Hello World") ➞ { "LETTERS":  10, "DIGITS": 0 }
    
    count_all("H3ll0 Wor1d") ➞ { "LETTERS":  7, "DIGITS": 3 }
    
    count_all("149990") ➞ { "LETTERS": 0, "DIGITS": 6 }

### Notes

  * Tests contain only alphanumeric characters.
  * Spaces are not letters.
  * All tests contain valid strings.

"""

import string
def count_all(txt):
  lettcount = 0
  digicount = 0
  
  for i in txt:
    if i in string.ascii_lowercase or i in string.ascii_uppercase:
      lettcount += 1
    elif i in "0123456789":
      digicount += 1
      
  
  return {'LETTERS':lettcount,'DIGITS':digicount}

