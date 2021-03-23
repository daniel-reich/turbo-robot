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
  L = []
  for i in range(3):
      L.append(words[0].startswith(abbs[i]))
      L.append(words[1].startswith(abbs[i]))
      L.append(words[2].startswith(abbs[i]))
  return L == [True, False, False, False, True, False, False, False, True]

