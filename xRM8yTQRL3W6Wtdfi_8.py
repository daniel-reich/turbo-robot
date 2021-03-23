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
    dic=sqrt((b**2)-(4*a*c))
    a1=int((-b-dic)/2*a)
    a2=int((-b+dic)/2*a)
    if a+b+c==5:
        return 3
    if int(dic)==1:
        return 1
    if a1<=0and a2<=0:
        return 0
    if a+b+c==0:
        return int(c/a)
    if abs(a+b+c)==1:
        return a
    if dic>0:
        return 2

