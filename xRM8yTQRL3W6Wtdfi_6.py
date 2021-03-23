"""


Create a function that returns the number of (real) solutions of
`ax^4+bx^2+c=0`. The function will take three arguments: `a` as the
coefficient of `x^4`, `b` as the coefficient of `x^2`, and `c` as the constant
term.

### Examples

    quartic_equation(1, -5, 4) ➞ 4
    
    quartic_equation(4, 3, -1) ➞ 2
    
    quartic_equation(1, 10, 9) ➞ 0

### Notes

Hint: Try substitution `t=x^2`.

"""

from math import sqrt
def quartic_equation(a, b, c):
  if (b ** 2) - (4 * a * c) < 0:
    return 0
  elif c == 0 and b < 0:
    return 3
  elif c == 0 and b > 0:
    return 1
  else:
    sol1 = (-b+sqrt((b**2)-(4*a*c)))/(2*a)
    sol2 = (-b-sqrt((b**2)-(4*a*c)))/(2*a)
    if sol1 > 0 and sol2 > 0:
      return 4
    elif sol1 < 0 and sol2 < 0:
      return 0
    elif sol1 < 0 or sol2 < 0:
      return 2

