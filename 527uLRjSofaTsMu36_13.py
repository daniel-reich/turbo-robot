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

def get_middle(txt):
    if len(txt) == 0 :
        return txt
    
    if len(txt) % 2 == 0:
        return txt[int(len(txt)/2) -1] + txt[int((len(txt)/2))]
    elif len(txt) % 2 == 1:
        return txt[int(len(txt)//2)]

