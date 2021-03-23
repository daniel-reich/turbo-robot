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

import string
def nearest_vowel(c):
    chars = string.ascii_lowercase
    indexc = chars.index(c)
    nearest = min([abs(chars.index(c) - chars.index(i)) for i in 'aeiou'])
    nearl = chars[indexc - nearest]
    try:
        nearr = chars[indexc + nearest]
    except:
        nearr = nearl
    return nearl if nearl in 'aeiou' else nearr

