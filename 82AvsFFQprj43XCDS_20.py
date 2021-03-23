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

def no_strangers(txt):
  import re
  txt=txt.lower()
  txt=re.sub('[^a-zA-Z0-9 \n\']', '', txt)
  txt=txt.split()
  test={}
  accq = []
  friend = []
  for i in txt:
    test[i] = 1 if i not in test else test[i] + 1
    if test[i] == 3: accq.append(i)
    if test[i] == 5:
      friend.append(i)
      accq.remove(i)
  return [accq,friend]

