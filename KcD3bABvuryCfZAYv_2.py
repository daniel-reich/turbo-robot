"""


Write a function that returns the most frequent character in a list of words.

### Examples

    most_frequent_char(["apple", "bandage", "yodel", "make"])
    ➞ ["a", "e"]
    
    most_frequent_char(["music", "madness", "maniac", "motion"])
    ➞ ["m"]
    
    most_frequent_char(["the", "hills", "are", "alive", "with", "the", "sound", "of", "music"])
    ➞ ["e", "h", "i"]

### Notes

  * If multiple characters tie for most frequent, list all of them in alphabetical order.
  * Words will be in lower case.

"""

def most_frequent_char(lst):
  freq = {l: ''.join(lst).count(l) for l in set(''.join(lst))}
  return sorted([k for k, v in freq.items() if v == max(freq.values())])

