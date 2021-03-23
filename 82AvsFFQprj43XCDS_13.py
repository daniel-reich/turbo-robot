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
    txt = txt.lower().split()
    for x in range(len(txt)):
        for i in  '!?"",.':
            if i in txt[x]:
                txt[x] = txt[x].replace(i, "")
​
    dic = dict.fromkeys(set(txt), 0)
    acq, fri = [], []
    for x in txt:
        dic[x] += 1
        if dic[x] == 3:
            acq.append(x)
        if dic[x] == 5:
            fri.append(x)
            acq.remove(x)
    return [acq, fri]

