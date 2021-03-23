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
  myDict = {}
  for c in txt:
    if c in myDict:
      myDict[c] += 1
    else:
      myDict[c] = 1
  sum = 0
  for v in myDict.values():
    if v > 1:
      sum += 1
  return sum

