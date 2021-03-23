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
  l = []
  for i in range(len(name)):
    if name[i] != ' ':
      l.append(name[i].lower())
  for i in range(len(words)):
    for j in range(len(words[i])):
      if words[i][j].lower() in l:
        l.remove(words[i][j])
      else:
        return False
  if len(l) == 0:
    return True
  else:
    return False

