"""


Given a _string_ containing an _algebraic equation_ , calculate and **return
the value of x**. You'll only be given equations for simple **addition** and
**subtraction**.

### Examples

    eval_algebra("2 + x = 19") ➞ 17
    
    eval_algebra("4 - x = 1") ➞ 3
    
    eval_algebra("23 + 1 = x") ➞ 24

### Notes

  * There are spaces between every number and symbol in the string.
  * x may be a negative number.

"""

def eval_algebra(eq):
  eq = eq.replace('=', '==', 1)
  eq = eq.split('x')
  def check(val):
    return eval(str(val).join(eq))
  x = 0
  while True:
    if check(x):
      return x
    elif check(-x):
      return -x
    x += 1

