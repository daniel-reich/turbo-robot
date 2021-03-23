"""


Create a function that replaces all consecutively repeated letters in a word
with single letters.

### Examples

    remove_repeats("aaabbbccc") ➞ "abc"
    
    remove_repeats("bookkeeper") ➞ "bokeper"
    
    remove_repeats("nananana") ➞ "nananana"

### Notes

N/A

"""

def remove_repeats(txt):
    ret_txt = txt[0]
    for i, j in enumerate(txt[1:]):
        if txt[i] != j:
            ret_txt += j
    return ret_txt

