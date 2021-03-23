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
  count = {}
  for char in txt:
    count[char] = count.get(char, 0) + 1
  return len([char for char, num in count.items() if num > 1])

