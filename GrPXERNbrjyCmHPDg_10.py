"""


Create a function that takes a string and returns the number of alphanumeric
characters that occur more than once.

### Examples

    duplicate_count("abcde") ➞ 0
    
    duplicate_count("aabbcde") ➞ 2
    
    duplicate_count("Indivisibilities") ➞ 2
    
    duplicate_count("Aa") ➞ 0
    # Case sensitive

### Notes

  * Duplicate characters are case sensitive.
  * The input string will contain only alphanumeric characters.

"""

def duplicate_count(txt):
  from collections import Counter
  counted = Counter(txt)
  return len([counted[k] for k in counted if k.isalnum() and counted[k] > 1])

