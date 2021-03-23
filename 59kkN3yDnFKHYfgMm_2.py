"""


Given a string, return if a given letter **always** appears **immediately
before** another given letter.

### Worked Example

    best_friend("he headed to the store", "h", "e") ➞ True
    
    # All occurences of "h": ["he", "headed", "the"]
    # All occurences of "h" have an "e" after it.
    # Return True

### Examples

    best_friend("he headed to the store", "h", "e") ➞ True
    
    best_friend("i found an ounce with my hound", "o", "u") ➞ True
    
    best_friend("we found your dynamite", "d", "y") ➞ False

### Notes

  * Don't count letters with spaces between them (example #3).
  * All sentences will be given in lowercase.

"""

import re
def best_friend(txt, a, b):
  # Patern
  P = re.compile(a+b); # makes string e.g "he"
  # Find all cases of "he"
  X = re.findall(P,txt);
  # Find out if all cases "X" is equal to how many "h" are in string
  return len(X) == txt.count(a);

