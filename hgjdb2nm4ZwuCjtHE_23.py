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

def math_expr(expr):
  signs = "+-*/%"
  lst = [i for i in expr. replace(" ", "")]
  if len(lst) != 3:
    return False
  return lst[0].isnumeric() and lst[1] in signs and lst[2].isnumeric()

