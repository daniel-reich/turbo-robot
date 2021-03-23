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
  upper1 = s1.upper()
  upper2 = s2.upper()
  ordre1 = sorted(upper1)
  ordre2 = sorted(upper2)
  if ordre1 == ordre2:
    return True
  else:
    return False

