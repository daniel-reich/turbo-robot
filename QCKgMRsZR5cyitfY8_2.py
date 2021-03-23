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
  if isinstance(value, bool):
    return "bool"
  elif isinstance(value, str):
    return "str"
  elif isinstance(value, int):
    return "int"
  elif isinstance(value, list):
    return "list"
  elif isinstance(value, set):
    return "set"
  elif isinstance(value, tuple):
    return "tuple"
  elif isinstance(value, dict):
    return "dict"
  else:
    return "NoneType"

