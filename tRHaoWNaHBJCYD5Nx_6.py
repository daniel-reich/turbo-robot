"""


Create a function that returns `True` if two strings share the same letter
pattern, and `False` otherwise.

### Examples

    same_letter_pattern("ABAB", "CDCD") ➞ True
    
    same_letter_pattern("ABCBA", "BCDCB") ➞ True
    
    same_letter_pattern("FFGG", "CDCD") ➞ False
    
    same_letter_pattern("FFFF", "ABCD") ➞ False

### Notes

N/A

"""

def same_letter_pattern(txt1, txt2):
    index1 = ""
    index2 = ""
    for i in txt1:
        index1 += str(txt1.index(i))
    for i in txt2:
        index2 += str(txt2.index(i))
    return index1 == index2

