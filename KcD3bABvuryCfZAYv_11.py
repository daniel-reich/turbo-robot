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

import operator
def most_frequent_char(lst):
  adict = {}
  for i in range(len(lst)):
    for item in lst[i]:
      if item not in adict:
        adict[item] = 1
      else:
        adict[item] += 1
  a = max(adict.items(), key=operator.itemgetter(1))[1]
  result = []
  for k,v in adict.items():
    if v == a:
      result.append(k)
  return sorted(result)

