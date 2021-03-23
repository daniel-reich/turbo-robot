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
  if(type(value) == str): 
    return "str"
  if(type(value) == bool):
    return "bool"
  if(type(value) == int):
    return "int"
  if(type(value) == list):
    return "list"
  if(type(value) == set):
    return "set"
  if(type(value) == tuple):
    return "tuple"
  if(type(value) == dict):
    return "dict"
  else:
    return "NoneType"

