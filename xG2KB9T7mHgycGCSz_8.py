"""


Create a function to test if a string is a valid pin or not.

A valid pin has:

  * Exactly 4 or 6 characters.
  * Only numerical characters (0-9).
  * No whitespace.

### Examples

    valid("1234") ➞ True
    
    valid("45135") ➞ False
    
    valid("89abc1") ➞ False
    
    valid("900876") ➞ True
    
    valid(" 4983") ➞ False

### Notes

Empty strings should return `False` when tested.

"""

def valid(txt):
  return len(txt) in [4, 6] and all(['0' <= c <= '9' for c in txt])

