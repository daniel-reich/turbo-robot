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

import re
def join(lst):
    res, minsh = lst[0], 10**5
    for i in range(1, len(lst)):
        m = re.search(r'(\w+) \1', res + ' ' + lst[i])
        if m:
            ol = len(m.group(1))
            res += lst[i][ol:]
            if ol < minsh: 
                minsh = ol
        else:
            res += lst[i]
            minsh = 0
    return [res, minsh]

