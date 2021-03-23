"""


Create a function that takes a string and returns the middle character(s). If
the word's length is odd, return the middle character. If the word's length is
even, return the middle two characters.

### Examples

    get_middle("test") ➞ "es"
    
    get_middle("testing") ➞ "t"
    
    get_middle("middle") ➞ "dd"
    
    get_middle("A") ➞ "A"

### Notes

All test cases contain a single word (as a string).

"""

def get_middle(s):
    if len(s) % 2 == 1:
        return s[int((len(s)-1)/2)]
    elif len(s) == 0:
        return ''
    else:
        return s[int(len(s)/2)-1:int(len(s)/2)+1]

