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
  deta=b**2-4*a*c
  if deta<0:return 0
  elif deta==0:
    x=-b/(2*a)
    return 0 if x<0 else 1 if x==0 else 2
  else:
    x2=(-b-deta**0.5)/(2*a)
    if x2>0:
      return 4
    elif x2==0:
      return 3
    else:
      x1=(-b+deta**0.5)/(2*a)
      return 0 if x1<0 else 1 if x1==0 else 2

