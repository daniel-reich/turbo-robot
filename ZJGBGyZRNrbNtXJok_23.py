"""


Given a letter, created a function which returns the nearest vowel to the
letter. If two vowels are equidistant to the given letter, return the
_earlier_ vowel.

### Examples

    nearest_vowel("b") ➞ "a"
    
    nearest_vowel("s") ➞ "u"
    
    nearest_vowel("c") ➞ "a"
    
    nearest_vowel("i") ➞ "i"

### Notes

  * All letters will be given in lowercase.
  * There will be no alphabet wrapping involved, meaning the closest vowel to "z" should return "u", not "a".

"""

def nearest_vowel(s):
  s = ord(s) - 97
  if s < 3:
    return "a"
  elif s < 7:
    return "e"
  elif s < 12:
    return "i"
  elif s < 18:
    return "o"
  else:
    return "u"

