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
  a = len([txt[i] for i in range(1, len(txt)) if txt[i].isalpha() and txt[i-1] == '+' and txt[i+1] == '+'])
  b = sum([1 for i in txt if i.isalpha()])
  return a == b

