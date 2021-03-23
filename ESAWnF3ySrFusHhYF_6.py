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
    return [f(w) for w in lst]
​
def f(x):
    x = x[::-1].upper()
    ln = len(x) // 2
    if len(x) % 2 == 0:
        x = x[:ln] + '-' + x[ln:]
    else:
        x = x[:ln+1] + '-' + x[ln+1:]
    return x

