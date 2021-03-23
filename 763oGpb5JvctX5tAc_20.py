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
  lower_s1 = s1.lower()
  lower_s2 = s2.lower()
  lower_s1_sorted = ''.join(sorted(lower_s1))
  lower_s2_sorted = ''.join(sorted(lower_s2))
  if lower_s1_sorted == lower_s2_sorted:
    return True
  else:
    return False

