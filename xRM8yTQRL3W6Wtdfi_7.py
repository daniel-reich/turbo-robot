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
    d2 = b * b - 4 * a * c
    count = 0
    if d2 >= 0:
        d = pow(d2, 0.5)
        if -b + d > 0:
            count += 2
        if -b - d > 0:
            count += 2
        if -b + d == 0:
            count += 1
        if -b - d == 0:
            count += 1
    return count

