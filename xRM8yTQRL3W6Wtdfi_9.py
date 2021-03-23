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

def quartic_equation(a,b,c):
  disc = b**2 - 4*a*c
  if disc<0:
    return 0
  if disc>0:
    if c < 0:
      return 2
    elif c>0:
      if b<0:
        return 4
      if b>0:
        return 0
    else:
      if b<0:
        return 3
      else:
        return 1

