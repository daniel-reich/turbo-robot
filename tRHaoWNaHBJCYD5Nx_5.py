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
​
    if len(txt1) != len(txt2):
        return False
    
    codes = {}
​
    for char1, char2 in zip(txt1, txt2):
        if char1 not in codes:
            codes[char1] = char2
        else:
            if codes[char1] != char2:
                return False
​
    return True

