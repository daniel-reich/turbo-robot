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

def quartic_equation(a, b, c):
  roots = 0
  d = b ** 2 - 4 * a * c
  if d > 0:
    t1 = (-1 * b + d ** (0.5)) / (2 * a)
    t2 = (-1 * b - d ** (0.5)) / (2 * a)
    if t1 > 0:
      roots += 2
    elif t1 == 0:
      roots += 1
    else:
      roots += 0
    if t2 > 0:
      roots += 2
    elif t2 == 0:
      roots += 1
    else:
      roots += 0
  elif d == 0:
    t1 = (-1 * b) / (2 * a)
    if t1 > 0:
      roots += 2
    elif t1 == 0:
      roots += 1
    else:
      roots += 0
  return roots

