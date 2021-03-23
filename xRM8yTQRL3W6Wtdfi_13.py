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
    D = (b**2) - (4*a*c)
    x = [(-b-(D**0.5))/2*a, (-b+(D**0.5))/2*a]
    set1 = {j for i in x for j in (i**0.5,-(i**0.5)) if i>=0}
    return len(set1)

