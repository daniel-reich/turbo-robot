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
  key = "1234567890+-*/%= "
  new_string = ""
  for ch in expr:
    if ch in key:
      new_string += ch
  if new_string == expr:
    return True
  else:
    return False

