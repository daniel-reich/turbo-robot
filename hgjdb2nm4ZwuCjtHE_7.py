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
  u = expr.split(' ')
  if len(u) == 1:
    if sum([(k in '+-*/%0123456789') for k in u[0]]) == 3:
        return True
  else:
    if sum([(k in '+-*/%0123456789') for k in u]) == 3:
      return True
  return False

