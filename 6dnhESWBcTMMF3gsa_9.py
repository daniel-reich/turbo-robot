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
  stri = ""
  num = 0
  if type(a) == type(b) == int:
    stri += str(a)
    stri += str(b)
    print(stri)
    return stri
  if type(a) == type(b) == str:
    num += int(a)
    num += int(b)
    print(num)
    return num
  else:
    return None

