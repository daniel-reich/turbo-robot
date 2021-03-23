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
  vowels = "aeiou"
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  for i in range(0, len(alphabet)):
    if alphabet[i] == s:
      s_index = i
  min = len(alphabet)
  closest = ""
  for j in range(0, len(alphabet)):
    if alphabet[j] in vowels:
      if abs(j-s_index) < min:
        min = abs(j-s_index)
        closest = alphabet[j]
  return closest

