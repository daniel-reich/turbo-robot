"""


For this challenge, the input will be a (long) string.

A word encountered for the first time is a stranger. A word encountered thrice
becomes an acquaintance. A word encountered 5 times becomes a friend.

Create a function that takes the string and returns a list of two lists. The
first is a list of acquaintances in the order they became an acquaintance (see
example). The second is a list of friends in the order they became a friend.
Words on the friend list should no longer be on the acquaintance list.

### Examples

    no_strangers("See Spot run. See Spot jump. Spot likes jumping. See Spot fly.")
    ➞ [["spot", "see"], []]
    # "see" was encountered first, but "spot" became an acquaintance earlier.

### Notes

  * All words should be in lowercase.
  * Punctuation should be stripped except for apostrophes (e.g. doesn't, aren't, etc).

"""

import re
from collections import Counter
​
def no_strangers(txt):
  word_list = [i.lower() for i in re.findall(r'[a-z\']+',txt,re.I)]
  word = Counter(word_list)
  friend = [k for k,v in word.items() if v>= 5]
  # friend = [i[1] for i in friend]
  acq = [k for k,v in word.items() if 3<=v< 5]
  def sort_list(li,freq):
      sorted_list = []
      for i in li:
          counter = 0
          for ind, w in enumerate(word_list):
              if w == i:
                  counter += 1
                  if counter == freq:
                      sorted_list.append((ind,w))
                      break
      sorted_list = [i[1] for i in sorted(sorted_list)]
      return sorted_list
  return [sort_list(acq,3),sort_list(friend,5)]

