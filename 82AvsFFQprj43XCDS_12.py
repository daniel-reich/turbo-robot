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
  bad_chars = ',".'
​
  for c in bad_chars: txt = txt.replace(c, "").lower()
  words = [word for word in txt.split(" ")]
  count_map = {word: 0 for word in set(words)}
  
  aqs = []
  frds = []
  for word in words:
    count_map[word] += 1
    
    if count_map[word] == 3:
      aqs.append(word)
    elif count_map[word] == 5:
      aqs.pop(aqs.index(word))
      frds.append(word)
  return [aqs, frds]

