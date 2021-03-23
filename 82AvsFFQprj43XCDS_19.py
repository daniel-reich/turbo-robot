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

from collections import defaultdict
def no_strangers(words):
    counts, acquaintances, friends = defaultdict(int), [], []
    words = words.replace('"','').replace('.','').replace(',','')
    for word in words.lower().split():
        counts[word] += 1
        if counts[word] == 3:
            acquaintances.append(word)
        elif counts[word] == 5:
            friends.append(acquaintances.pop(acquaintances.index(word)))
    return [acquaintances, friends]

