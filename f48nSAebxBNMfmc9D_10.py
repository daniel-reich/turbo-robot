"""


Write a function that receives a list of words and a mask. Return a list of
words, sorted alphabetically, that match the given mask.

### Examples

    scrambled([”red”, “dee”, “cede”, “reed”, “creed”, “decree”], “*re**”) ➞ [“creed”]
    
    scrambled([”red”, “dee”, “cede”, “reed”, “creed”, “decree”], “***”) ➞ [“dee”, “ree”]

### Notes

The length of a mask will never exceed the length of the longest word in the
word list.

"""

import re
def scrambled(words, mask):
  return [m.group(0) for m in [re.match('^' + mask.replace('*', '.') + '$', word) for word in words] if m != None]

