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

def modify(word):
    word = word.upper()[::-1]
    n = len(word)
    n2 = n // 2
    if n % 2 == 0:
        return word[:n2] + "-" + word[n2:]
    else:
        return word[:n2+1] + "-" + word[n2+1:]
    
def edit_words(lst):
    return [modify(w) for w in lst]

