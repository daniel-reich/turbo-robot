"""


Given two simultaneous linear equations in this form: `a*x + b*y = c`, `d*x +
e*y = f`, devise a function that returns the values of `x` and `y` as `(x,
y)`. The numbers `a` through `f` are non-zero integers. If there is not a
unique solution or if there is no solution at all, return `False`. Input is
given as: `[[a, b, c], [d, e, f]]`. Solutions, if they exist, will be
integers.

### Examples

    sle([[3, 4, 19], [2, -1, 9]]) ➞ (5, 1)
    
    sle([[3, 2, -2], [2, 5, -5]]) ➞ (0, -1)
    
    sle([[4, -3, 18], [8, -6, 36]]) ➞ False
    
    sle([[2, 3, 13], [5, -1, 7]]) ➞ (2, 3)

### Notes

Can you do this without using numpy?

"""

def sle(m):
    a = m[0][0]
    b = m[0][1]
    c = m[0][2]
    d = m[1][0]
    e = m[1][1]
    f = m[1][2]
    D = a * e - b * d
    Dx = c * e - b * f
    Dy = a * f - c * d
    if D == 0:
        return False
    else:
        x = Dx / D
        y = Dy / D
        return (x, y)

