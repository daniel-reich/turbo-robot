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
  if isinstance(a, str) and isinstance(b, str):
    return int(a) + int(b)
  elif isinstance(a, int) and isinstance(b, int):
    return str (a) + str (b)

