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
  l1 = [s1[i] for i in range(len(s1))]
  l2 = [s2[i] for i in range(len(s2))]
  return sorted(l1) == sorted(l2)

