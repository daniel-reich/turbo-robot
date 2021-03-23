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
  if len(txt) < 3:
    return False
  for i in range(1,len(txt) - 1):
    if ord(txt[i]) in range(97,123):
      print(txt[i])
      if txt[i-1] != '+' or txt[i+1] != '+':
        return False
  return True

