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
  d=b*b-4*a*c
  l=[]
  if d>=0:
    x,y=(-b+d**.5)/2*a,(-b-d**.5)/2*a
    if x>=0:l+=[x**.5,-x**.5]
    if y>=0:l+=[y**.5,-y**.5]
    return len(set(l))
  return 0

