"""


Create a function that takes a word and returns the new word without including
the first character.

### Examples

    new_word("apple") ➞ "pple"
    
    new_word("cherry") ➞ "herry"
    
    new_word("plum") ➞ "lum"

### Notes

The input is always a valid word.

"""

def new_word(word):
  word = list(word)
  word.pop(0)
  return "".join(word)

