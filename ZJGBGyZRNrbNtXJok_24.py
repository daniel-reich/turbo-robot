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
    closest_vowel = [abs(ord(s) - ord('a')), 'a']
    for vowel in 'eiou':
        distance = abs(ord(s) - ord(vowel))
        if distance < closest_vowel[0]:
            closest_vowel[0] = distance
            closest_vowel[1] = vowel
    return closest_vowel[1]

