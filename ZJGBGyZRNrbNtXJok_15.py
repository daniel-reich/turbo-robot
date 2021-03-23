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
  vowels = 'aeiou'
  lower = ord(s) - 1
  higher = ord(s) + 1
  if s in vowels:
    return s
  while chr(lower) not in vowels and chr(higher) not in vowels:
    lower -= 1
    higher += 1
  if chr(lower) in vowels:
    return chr(lower)
  return chr(higher)

