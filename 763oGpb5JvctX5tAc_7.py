"""


Create a function that takes two strings and returns either `True` or `False`
depending on whether they're anagrams or not.

### Examples

    is_anagram("cristian", "Cristina") ➞ True
    
    is_anagram("Dave Barry", "Ray Adverb") ➞ True
    
    is_anagram("Nope", "Note") ➞ False

### Notes

  * Should be case insensitive.
  * The two given strings can be of different lengths.

"""

def is_anagram(s1, s2):
  s1 = s1.lower()
  s2 = s2.lower()
  for eachletter in s2:
    x = s1.count(eachletter)
    y = s2.count(eachletter)
    if x == y:
      continue
    else:
      return False
  return True

