"""


Create a function that takes a list of any _length_. Modify each element
**(capitalize, reverse, hyphenate)**.

### Examples

    edit_words(["new york city"]) ➞ ["YTIC KR-OY WEN"]
    
    edit_words(["null", "undefined"]) ➞ ["LL-UN", "DENIF-EDNU"]
    
    edit_words(["hello", "", "world"]) ➞ ["OLL-EH", "-", "DLR-OW"]
    
    edit_words([""]) ➞ ["-"]

### Notes

Input list values can be any _type_.

"""

import math
def edit_words(lst):
    lst = list(map(lambda x:''.join(list(x.upper())[::-1]),lst))
    return list(map(lambda x:x[:math.ceil(len(x)/2)]+'-'+ x[math.ceil(len(x)/2):],lst))

