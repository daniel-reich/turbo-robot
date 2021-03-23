"""


Create a function that returns `True` if an input string contains only
uppercase or only lowercase letters.

### Examples

    same_case("hello") ➞ True
    
    same_case("HELLO") ➞ True
    
    same_case("Hello") ➞ False
    
    same_case("ketcHUp") ➞ False

### Notes

N/A

"""

def same_case(txt):
  if txt.upper() == txt or txt.lower() == txt:
    return True
  else:
    return False

