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

def missing_letter(lst):
  x = ord(lst.pop(0))
  for i in lst:
    i = ord(i)
    if i == x + 1:
      x = i
    else:
      return chr(x + 1)

