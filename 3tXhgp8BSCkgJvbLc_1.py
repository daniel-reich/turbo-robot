"""


A popular puzzle is where you are given a list of word fragments and have to
combine them to form a set of words such that each fragment is used only once.

For this challenge, write a function that takes a list of fragments and
returns a sorted list of 20 words which can be made from them.

### Example

    find_words(["er", "haw", "as", "dock", "yuc", "prim", "ia", "sy", "sy", "y", "i", "thorn", "bur", "weed", "snow", "sia", "tus", "cac", "pop", "clo", "chid", "pan", "ris", "dahl", "rose", "dai", "drop", "dog", "ver", "bind", "heath", "fuch", "mine", "ca", "lil", "ter", "jas", "wood", "py", "or"])
    ➞ ["aster", "bindweed", "burdock", "cactus", "clover", "dahlia", "daisy", "dogwood", "fuchsia", "hawthorn", "heather", "iris", "jasmine", "lily", "orchid", "pansy", "poppy", "primrose", "snowdrop", "yucca"]

### Notes

  * A dictionary is required to solve this puzzle. A set of words DICTIONARY is provided in the tests - it contains all the words required (plus a few more for luck and to make the task a little more challenging).
  * You always have to return a list of 20 words sorted in ascending order.
  * The input fragments list will contain either 40 or 60 fragments. There are two fragments per word if the list has 40 fragments, otherwise three fragments per word.
  * A word will always be just the combined fragments with no spaces or hyphens amongst them.
  * Fragments are not necessarily unique within a fragments list.

"""

from itertools import combinations, permutations
def find_words(f):
    f.sort()
    n_w = len(f) // 20
    res = set()
    for c in combinations(f, n_w):
        for p in permutations(c):
            w = ''.join(p)
            if w in DICTIONARY:
                res.add((w, p))
    res = sorted(res)
    for c in combinations(res, 20):
        chosen_frg = []
        chosen_words = []
        for tpl in c:
            chosen_frg += list(tpl[1])
            chosen_words.append(tpl[0])
        if sorted(chosen_frg) == f:
            return sorted(chosen_words)

