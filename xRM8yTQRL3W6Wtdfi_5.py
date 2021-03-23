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
    s=(4,2,0,3,1)
    r=(b*b-4*a*c)**.5
    x1=(-b+r)/2*a
    x2=(-b-r)/2*a
    return s[(x1<0)+(x2<0)+3*((x1==0) or (x2==0))]

