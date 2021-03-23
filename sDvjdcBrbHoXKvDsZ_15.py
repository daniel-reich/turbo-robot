"""


Write a function that returns `True` if a given name can generate an array of
words.

### Examples

    anagram("Justin Bieber", ["injures", "ebb", "it"]) ➞ True
    
    anagram("Natalie Portman", ["ornamental", "pita"]) ➞ True
    
    anagram("Chris Pratt", ["chirps", "rat"]) ➞ False
    # Not all letters are used
    
    anagram("Jeff Goldblum", ["jog", "meld", "bluffs"]) ➞ False
    # "s" does not exist in the original name

### Notes

  * Each letter in the name may only be used once.
  * All letters in the name must be used.

"""

def anagram(name, words):
  i = 0
  j = 0
  name = list(name.lower().replace(' ',''))
  while i < len(words):
    while j < len(words[i]):
      if words[i][j] not in name:
        return False
      else:
        name.remove(words[i][j])
      j += 1
    j = 0
    i += 1
  if len(name) > 0:
    return False
  return True

