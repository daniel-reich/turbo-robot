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

def edit_words(lst):
    res = []
    for w in lst:
        len_w = len(w)
        len_w2 = len_w // 2 + 1 if len_w % 2 else len_w // 2
        up_w = w.upper()[::-1]
        res.append("-".join([up_w[:len_w2], up_w[len_w2:]]))
    return res

