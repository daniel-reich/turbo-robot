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
  lst1=[];lst2=[]
  word=''.join(c if c.isalnum() or c=="'" else ' ' for c in txt.lower()).split()
  for i in set(word):
    if word.count(i)>=5:lst2+=[i]
    elif word.count(i)>=3:lst1+=[i]
  for i in lst1:
    for j in range(2):word.remove(i)
  for i in lst2:
    for j in range(4):word.remove(i)
  return [sorted(lst1,key=word.index),sorted(lst2,key=word.index)]

