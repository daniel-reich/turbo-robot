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

import math
​
def quartic_equation(a, b, c):
    if c == 0:
        # 0 is a solution:
        return 1 if a * b >= 0 else 3
    D = b**2 - 4 * a * c
    if D < 0:
        return 0
    if D == 0:
        return 2
    z1 = (-b + math.sqrt(D)) / (2 * a)
    z2 = (-b - math.sqrt(D)) / (2 * a)
    if z1 < 0:
        return 0
    return 2 if z2 < 0 else 4

