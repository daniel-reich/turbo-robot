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
  x= min(abs(ord('a')-ord(s)),abs(ord('e')-ord(s)),abs(ord('i')-ord(s)),abs(ord('o')-ord(s)), abs(ord('u')-ord(s))) 
  if chr(ord(s)-x) in ('aeiou'):
    return chr(ord(s)-x) 
  else:
    return chr(ord(s)+x)

