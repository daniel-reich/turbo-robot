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
  eq = eq.split()
  a, b, c = eq[::2] if eq[1] == '+' else eq[::2][::-1]
  if a == 'x':
    return int(c) - int(b)
  if b == 'x':
    return int(c) - int(a)
  if c == 'x':
    return int(a) + int(b)

