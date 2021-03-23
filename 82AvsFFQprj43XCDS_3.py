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
  txt_nopunc = ''
  str_punc = '!()-[]{};:"\,<>./?@#$%^&*_~'
  for i in txt:
    if i not in str_punc:
      txt_nopunc += i
  list1 = txt_nopunc.lower().split()
  list2a, list2b = [], []
  dict1 = {}
  for item in list1:
    if item not in dict1.keys():
      dict1[item] = 1
    else:
      dict1[item] += 1
    if dict1[item] >= 3 and dict1[item] < 5 and item not in list2a:
      list2a.append(item)
    elif dict1[item] >=5 and item not in list2b:
      list2b.append(item)
      list2a.remove(item)
  return [list2a, list2b]

