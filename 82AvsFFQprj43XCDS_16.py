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

import string
def no_strangers(txt):
  txt = ''.join([i.lower() for i in txt if i not in '.,"']).split()
  d = {}
  aquaintances = []
  friends = []
  for i in txt:
    if i not in d:
      d[i] = 1
    else:
      d[i] += 1
    if d[i] == 3 and d[i] not in aquaintances and d[i] not in friends:
      aquaintances.append(i)
    if d[i] == 5 and d[i] not in friends:
      friends.append(i)
      aquaintances.remove(i)
  return [aquaintances, friends]

