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
  a = 'abcdefghijklmnopqrstuvwxyz'
  if s in vowels:
    return s
  for i in range(1,6):
    if a.index(s)-i>=0 and a.index(s)+i<len(a):
      if a[a.index(s)-i] in vowels and a[a.index(s)+i] in vowels:
        return a[a.index(s)-i]
    if a.index(s)-i>=0 and a[a.index(s)-i] in vowels:
      return a[a.index(s)-i]
    if a.index(s)+i<len(a) and a[a.index(s)+i] in vowels:
      return a[a.index(s)+i]

