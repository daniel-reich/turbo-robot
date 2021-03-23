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
    result = [str(lst[0]), []]
    for word in lst[1:]:
        l = len(result[0])
        counter = 0
        print(result[0])
        for i in range(0,len(word)):
            if word[:i+1] ==result[0][len(result[0])-len(word[:i+1]):]:
                result[0] += word[i+1:]
                result[1].append(len(word)-len(word[i+1:]))
                break
        if l == len(result[0]) and word not in result[0]:
            result[0] += word
    if len(result[1]) == 0:
        return [result[0], 0]
    return [result[0], min(result[1])]

