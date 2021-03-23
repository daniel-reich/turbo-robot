"""


Create a function that takes an input (e.g. `"5 + 4"`) and returns `True` if
it's a mathematical expression or `False` if not.

### Examples

    math_expr("4 + 5") ➞ True
    
    math_expr("4*6") ➞ True
    
    math_expr("4*no") ➞ False

### Notes

  * Should only work with the following operations: `+, -, *, /, %`
  * You don't need to test for floats.
  * int1 and int2 will only be from 0-9.

"""

import re
def math_expr(expr):
  pattern = "[0-9]*\W*[0-9]"
  x = re.findall(pattern,expr)
  x = "".join(x)
  if x == expr:
   return True
  else:
   return False

