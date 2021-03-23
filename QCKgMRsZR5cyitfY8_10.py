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
  return str(type(value))[8:-2]

