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

def find_words(fragments):
    '''
    Returns a sorted list of the 20 words in DICTIONARY made from the fragments
    in fragments
    '''
    from itertools import permutations, combinations
​
    fragset = sorted(fragments)
    size = 2 if len(fragments) == 40 else 3
​
    word_set = {}
    for combo in permutations(fragset, size):
        word = ''.join(combo)
        if word in DICTIONARY:
            word_set[word] = combo
​
    if len(word_set) == 20:
        return sorted(word_set)
​
    for combo in combinations(word_set, 20):
        frag_list = sorted([frag for word in combo for frag in word_set[word]])
        if frag_list == fragset:
            return sorted(combo)
​
    return 'Error - failed to find 20 words to fit!!'

