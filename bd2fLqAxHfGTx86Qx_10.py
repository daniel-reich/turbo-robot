"""


An input string can be completed if additional letters can be added and no
letters need to be taken away to match the word. Furthermore, the order of the
letters in the input string must be the same as the order of letters in the
final word.

Create a function that, given an input string, determines if the word can be
completed.

### Examples

    can_complete("butl", "beautiful") ➞ True
    # We can add "ea" between "b" and "u", and "ifu" between "t" and "l".
    
    can_complete("butlz", "beautiful") ➞ False
    # "z" does not exist in the word beautiful.
    
    can_complete("tulb", "beautiful") ➞ False
    # Although "t", "u", "l" and "b" all exist in "beautiful", they are incorrectly ordered.
    
    can_complete("bbutl", "beautiful") ➞ False
    # Too many "b"s, beautiful has only 1.

### Notes

Both string input and word will be lowercased.

"""

import re
def can_complete(initial, word):
  query = "(.*)".join([ch for ch in initial]) 
  return True if re.match(query, word) else False
