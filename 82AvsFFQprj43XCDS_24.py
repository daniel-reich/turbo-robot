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
    exclude = set(string.punctuation) - set(['\''])
    txt = ''.join(ch for ch in txt if ch not in exclude)
    dic, acquaint, friends = {}, [], []
    for word in txt.split(' '):
        word = word.lower()
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] +=1
            if dic[word] == 3:
                acquaint += [word]
            if dic[word] == 5:
                friends += [word]
                acquaint.remove(word)
​
    return [acquaint, friends]

