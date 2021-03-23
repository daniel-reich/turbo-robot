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
  t1=(-b+(b*b-4*a*c)**.5)/(2*a)
  t2=(-b-(b*b-4*a*c)**.5)/(2*a)
  if t1>0 and t2>0:
    return 4
  elif (t1>0 and t2<0) or (t1<0 and t2>0):
    return 2
  elif (t1==0 and t2>0) or (t1>0 and t2==0):
    return 3
  elif t1==t2 and t1>0:
    return 1
  elif t1==t2==0:
    return 1
  elif (t1==0 and t2<0) or (t1<0 and t2==0):
    return 1
  else:
    return 0

