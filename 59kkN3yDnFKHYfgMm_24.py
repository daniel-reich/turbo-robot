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

def best_friend(s, a, b):
  return s != a if len(s) == 1 else False \
    if s[0] == a and s[1] != b else best_friend(s[1:], a, b)
