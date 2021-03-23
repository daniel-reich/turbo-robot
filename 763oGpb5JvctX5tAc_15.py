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
  em = sorted(s1.lower())
  im = sorted(s2.lower())
  
  if em == im:
    return True
  else:
    return False

