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
  if txt[0].isalpha() or txt[len(txt) - 1].isalpha():
    return False
  
  for i in range(0, len(txt)):
    if txt[i].isalpha():
      previous = txt[i - 1]
      next = txt[i + 1]
      if previous != "+" or next != "+":
        return False
  
  return True

