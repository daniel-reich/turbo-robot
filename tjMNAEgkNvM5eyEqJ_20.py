"""


You are given two inputs:

  1. An array of abbreviations.
  2. An array of words.

Write a function that returns `True` if each abbreviation **uniquely
identifies** a word, and `False` otherwise.

### Examples

    unique_abbrev(["ho", "h", "ha"], ["house", "hope", "happy"]) ➞ False
    // "ho" and "h" are ambiguous and can identify either "house" or "hope"
    
    unique_abbrev(["s", "t", "v"], ["stamina", "television", "vindaloo"]) ➞ True
    
    unique_abbrev(["bi", "ba", "bat"], ["big", "bard", "battery"]) ➞ False
    
    unique_abbrev(["mo", "ma", "me"], ["moment", "many", "mean"]) ➞ True

### Notes

Abbreviations will be a substring from `[0, n]` from the original string.

"""

def unique_abbrev(abbs, words):
  k = 0
  while k < len(abbs):
    i = 0
    num = 0
    while i < len(words):
      if words[i].startswith(abbs[k]):
        num = num + 1
      if num > 1:
        return False
      i = i + 1
    k = k + 1
  return True

