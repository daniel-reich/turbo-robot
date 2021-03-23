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
    if txt[0].isalpha() :
        return False
    return sum(map(lambda x : 1 if x.isalpha() else 0,txt))==sum(True for m in
      [r for r in enumerate( txt) if r[1].isalpha() ] if txt[m[0]-1]=='+' and txt[m[0]+1]=='+')

