"""


Create a function that takes two parameters and, if both parameters are
strings, **add them** as if they were integers or if the two parameters are
integers, **concatenate them**.

### Examples

    stupid_addition(1, 2) ➞ "12"
    
    stupid_addition("1", "2") ➞ 3
    
    stupid_addition("1", 2) ➞ None

### Notes

  * If the two parameters are different data types, return `None`.
  * All parameters will either be strings or integers.

"""

def stupid_addition(a, b):
  if type(a) is int and type(b) is int:
    return str(a) + str(b)
  if type(a) is str and type(b) is str:
    return int(a) + int(b)
  else:
    return None

