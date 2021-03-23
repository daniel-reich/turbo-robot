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

def unravel(txt):
    idx1 = txt.find('[')
    if idx1  < 0:
        return [txt]
    L = [txt[:idx1]]
    while len(txt) > 0:
        idx1 = txt.find('[')
        if idx1 < 0:
            L2 = [el + txt for el in L]
            break
        idx2 = txt.find(']')
        possibilities = txt[idx1+1:idx2].split('|')
        txt = txt[idx2+1:]
        L2 = []
        for el in L:
            for poss in possibilities:
                L2.append(el + poss)
        L = L2[:]
        if len(txt) == 0:
            break
        idx1 = txt.find('[')
        if idx1 < 0:
            L2 = [el + txt for el in L]
            break
        elif idx1 > 0:
            chunk = txt[:idx1]
            L2 = [el + chunk for el in L]
            txt = txt[idx1:]
        L = L2[:]
    return sorted(L2)

