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

def best_friend(txt, a, b):
  if txt[-1]==a:return False
  for i in range(len(txt)-1):
    if txt[i]==a and txt[i+1]!=b:
      return False
  return True

