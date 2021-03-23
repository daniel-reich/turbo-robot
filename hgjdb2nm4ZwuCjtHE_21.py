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
  return expr[0].isdigit() and expr[len(expr) // 2] in "+-*/%" and expr[-1].isdigit()

