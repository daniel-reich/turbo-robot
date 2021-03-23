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

def overlap(w1, w2):
    lap = 0
    for i in range(min(len(w1), len(w2))):
        if w1[-(i + 1):] == w2[:i + 1]:
            lap = i + 1
    word = w1[:-lap] + w2 if lap else w1 + w2
    return word, lap
​
def join(lst):
    joint = lst[0]
    del lst[0]
    laps = []
    for i in lst:
        joint, lap = overlap(joint, i)
        laps.append(lap)
    return [joint, min(laps)]

