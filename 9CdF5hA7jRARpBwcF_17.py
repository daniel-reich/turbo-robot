"""


Given a word, create a dictionary that stores the indexes of each letter in a
list.

  * Make sure the letters are the keys.
  * Make sure the letters are symbols.
  * Make sure the indexes are stored in a list and those lists are values.

### Examples

    map_letters("dodo") ➞ { "d": [0, 2], "o": [1, 3] }
    
    map_letters("froggy") ➞ { "f":  [0], "r": [1], "o": [2], "g": [3, 4], "y": [5] }
    
    map_letters("grapes") ➞ { "g": [0], "r": [1], "a": [2], "p": [3], "e": [4], "s": [5] }

### Notes

All strings given will be lowercase.

"""

from collections import defaultdict
def map_letters(word):
  dic = defaultdict(list)
  for i,w in enumerate(word):
    dic[w].append(i)
  return dic

