"""


Write a function that connects each previous word to the next word by the
shared letters. Return the resulting string (removing **duplicate characters**
in the overlap) and the **minimum** number of shared letters across all pairs
of strings.

### Examples

    join(["oven", "envier", "erase", "serious"]) ➞ ["ovenvieraserious", 2]
    
    join(["move", "over", "very"]) ➞ ["movery", 3]
    
    join(["to", "ops", "psy", "syllable"]) ➞ ["topsyllable", 1]
    
    # "to" and "ops" share "o" (1)
    # "ops" and "psy" share "ps" (2)
    # "psy" and "syllable" share "sy" (2)
    # the minimum overlap is 1
    
    join(["aaa", "bbb", "ccc", "ddd"]) ➞ ["aaabbbcccddd", 0]

### Notes

More specifically, look at the overlap between the previous words **ending
letters** and the next word's **beginning letters**.

"""

def get_overlap(word1, word2):
    if len(word2) < len(word1) and word1[-len(word2):] == word2:
        return len(word2)
    L = min(len(word1), len(word2))
    for k in range(L):
        if word1[-k:] == word2[:k]:
            return k
    return 0
​
def join(lst):
    min_ov = min([get_overlap(lst[i-1], lst[i]) for i in range(1, len(lst))])
    if min_ov == 0:
        return [''.join(lst), 0]
    concat = lst[0]
    prev = lst[0]
    for word in lst[1:]:
        ov = get_overlap(prev, word)
        if ov == 0:
            concat += word
        else:
            concat += word[ov:]
        prev = word
    return [concat, min_ov]

