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
  flag = txt[0].isupper()
  for i in range (1, len(txt)):
    if flag != txt[i].isupper():
      return False
  return True

