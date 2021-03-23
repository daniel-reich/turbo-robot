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
    dic = {"a" : 97, "e" : 101, "i" : 105, "o" : 111, "u" : 117 }
    look = ord(s)
    off = [(abs(dic[key] - look), key) for key in dic]
    return min(off)[1]

