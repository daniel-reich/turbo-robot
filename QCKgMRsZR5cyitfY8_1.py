"""


Create a function that takes a value as an argument and returns the type of
this value.

### Examples

    get_type(1) ➞ "int"
    
    get_type("a") ➞ "str"
    
    get_type(true) ➞ "bool"
    
    get_type([]) ➞ "list"
    
    get_type(None) ➞ "NoneType"

### Notes

N/A

"""

def get_type(value):
  type3 = str(type(value))
  type2 = ''
  isType = False
  for y in type3:
    if(y == '\'' and isType):
      break
    if(isType):
      type2 += y
    if(y == '\'' and not isType):
      isType = True
  return type2

