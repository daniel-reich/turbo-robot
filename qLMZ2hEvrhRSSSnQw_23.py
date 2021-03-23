"""


Graded lexicographic order (grlex order for short) is a way of ordering words
that:

  1. First orders words by length.
  2. Then orders words of the same size by their dictionary order.

For example, in grlex order:

  * "tray" < "trapped" since "tray" has length 4 while "trapped" has length 7.
  * "trap" < "tray" since both have length 4, but "trap" comes before "tray" in the dictionary.

Given a list of words, return that list in grlex order.

### Examples

    make_grlex(["small", "big"]) ➞ ["big", "small"]
    
    make_grlex(["cat", "ran", "for", "the", "rat"]) ➞ ["cat", "for", "ran", "rat", "the"]
    
    make_grlex(["this", "is", "a", "small", "test"]) ➞ ["a", "is", "test", "this", "small"]

### Notes

N/A

"""

import collections
def make_grlex(l):
    d = {}
    for item in l:
        if len(item) not in d:
            d[len(item)] = [item]
        else:
            d[len(item)].append(item)
    print(d)
    d = collections.OrderedDict(sorted(d.items()))
    return [i for key, val in d.items() for i in sorted(val)]

