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
    lst = re.split(r"(\[.+?\])",txt)
    if len(lst) == 1 and lst[0].isalpha():
        return [txt]
    else:
        final = []
        for i in lst:
            result = comp(i)
            if final == []:
                for i in result:
                    final.append(i)
            else:
                newlst = []
                for i in final:
                    for j in result:
                        elem = i + j
                        newlst.append(elem)
                final = newlst
        return list(sorted(final))
​
def comp(i):
    if len([x for x in i if x not in '[]|']) == len(i):
        return [i]
    elif '|' not in i:
        return [i[1:-1]]
    elif '|' in i:
        lst = i[1:-1].split('|')
        return lst

