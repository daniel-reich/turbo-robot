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

is_anagram = lambda a, b: sorted(a.lower()) == sorted(b.lower())

