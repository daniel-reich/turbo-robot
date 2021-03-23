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
  txt2 = ""
  
  for letter in txt:
    if letter.isalpha() or letter == " " or letter == "'":
      txt2 += letter.lower()
      
  lst = txt2.split()
  
  friends = []
  acquaintances = []
  strangers = {}
  result = []
  
  for l in lst:
    if not l in strangers.keys():
      strangers[l] = 1
    else:
      strangers[l] = strangers[l] + 1
      if strangers[l] == 3:
        acquaintances.append(l)
      elif strangers[l] == 5:
        acquaintances.pop(acquaintances.index(l))
        friends.append(l)
  
  result.append(acquaintances)
  result.append(friends)
  return result

