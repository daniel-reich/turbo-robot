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
  acq = []
  fr = []
  total = {}
  txt = txt.replace(".", "")
  txt = txt.replace(",", "")
  txt = txt.replace("\"", "")
  txt = txt.lower()
  words = txt.split(" ")
  for word in words:
    if (word in total):
      total[word] += 1
      if (total[word] == 3):
        acq.append(word)
      if (total[word] == 5):
        fr.append(word)
        acq.remove(word)
    else:
      total[word] = 1
  return [acq, fr]

