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
def no_strangers(txt):
  mem = {}
  words = re.split('[^\w\']+', txt.lower())
  for i,word in enumerate(words):
    if word not in mem:
      mem[word] = {'count':0}
    mem[word]['count'] += 1
    if mem[word]['count'] in (1,3,5):
      mem[word]['index'] = i
  
  acquaintance = []
  friend = []
  for word in mem:
    if 2 < mem[word]['count'] < 5: acquaintance.append(word)
    elif mem[word]['count'] >= 5: friend.append(word)
    mem[word] = mem[word]['index']
  return [sorted(group, key = mem.get) for group in (acquaintance, friend)]

