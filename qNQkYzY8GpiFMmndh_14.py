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

def join(lst):
    output = ""
    overlap_lst = [0]
    overlap_min = max(list(map(len, lst)))
    for i in range(1,len(lst)):
        overlap = 0
        for j in range(1,len(lst[i-1])):
            if lst[i].startswith(lst[i-1][j:]):
                overlap = len(lst[i-1])-j
                if overlap < overlap_min:
                    overlap_min = overlap
                break
            else:
                continue
        if overlap == 0:
            overlap_min = 0
        overlap_lst.append(overlap)
    for i in range(len(lst)):
        output += lst[i][overlap_lst[i]:]
    return [output, overlap_min]

