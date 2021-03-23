"""


Write a function that takes in a string and returns all possible combinations.
Return the final result in **alphabetical order**.

### Examples

    unravel("a[b|c]") ➞ ["ab", "ac"]
    
    unravel("a[b|c]de[f|g]") ➞ ["abdef", "acdef", "abdeg", "acdeg"]
    
    unravel("a[b]c[d]") ➞ ["abcd"]
    
    unravel("a[b|c|d|e]f") ➞ ["abf", "acf", "adf", "aef"]
    
    unravel("apple [pear|grape]") ➞ ["apple grape", "apple pear"]

### Notes

Think of each element in every block (e.g. `[a|b|c]`) as a **fork in the
road**.

"""

import re
def unravel(txt):
    txt = re.split('\[|\]',txt)
    s = ['']
    for i in txt:
        if '|' not in i:
            s = [v + i for v in s]
        else:
            k = i.split('|')
            s1 = []
            for j in k:
                s1.extend([v + j for v in s])
            s = s1[:]
    return sorted(s)

