"""


Create a function that takes a string as an argument and returns `True` if
each letter in the string is surrounded by a plus sign. Return `False`
otherwise.

### Examples

    plus_sign("+f+d+c+#+f+") ➞ True
    
    plus_sign("+d+=3=+s+") ➞ True
    
    plus_sign("f++d+g+8+") ➞ False
    
    plus_sign("+s+7+fg+r+8+") ➞ False

### Notes

For clarity, each **letter** must have a plus sign on both sides.

"""

def plus_sign(txt):
    text = [c for c in txt if c.isalpha()]
    r = [txt[char] for char in range(0,len(list(txt))-1) if txt[char].isalpha() and txt[char-1]=='+' and txt[char+1]=='+' and not txt[0].isalpha()]
    if len(r)==len(text):
        return True
    else:
        return False

