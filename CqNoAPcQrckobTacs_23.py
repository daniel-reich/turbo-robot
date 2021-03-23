"""


Create a function that takes a list of increasing letters and return the
missing letter.

### Examples

    missing_letter(["a", "b", "c", "e", "f", "g"]) ➞ "d"
    
    missing_letter(["O", "Q", "R", "S"]) ➞ "P"
    
    missing_letter(["t", "u", "v", "w", "x", "z"]) ➞ "y"
    
    missing_letter(["m", "o"]) ➞ "n"

### Notes

  * Tests will always have exactly one letter missing.
  * The length of the test list will always be at least two.
  * Tests will be in one particular case (upper or lower but never both).

"""

import string
def missing_letter(lst):
  abc_lo = string.ascii_letters[:len(string.ascii_letters) // 2]
  abc_up = string.ascii_letters[len(string.ascii_letters) // 2:]
  return "".join([ch for _, ch in enumerate(abc_lo if lst[0].islower() else abc_up) 
          if ch not in lst and lst[0] < ch < lst[-1]])

