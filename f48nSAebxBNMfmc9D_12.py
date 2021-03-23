"""


Write a function that receives a list of words and a mask. Return a list of
words, sorted alphabetically, that match the given mask.

### Examples

    scrambled([”red”, “dee”, “cede”, “reed”, “creed”, “decree”], “*re**”) ➞ [“creed”]
    
    scrambled([”red”, “dee”, “cede”, “reed”, “creed”, “decree”], “***”) ➞ [“dee”, “ree”]

### Notes

The length of a mask will never exceed the length of the longest word in the
word list.

"""

import re
​
def scrambled(words, mask):
    mask = re.sub('\*', '.', mask) + '$'
    res1 = map(lambda x: re.match(mask, x), words)
    res2 = [x for x in map(lambda m: m.group(0)
                if m != None else None, res1) if x != None]
    return(res2)

