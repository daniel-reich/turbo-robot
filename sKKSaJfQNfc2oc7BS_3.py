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
  a1 = m[0][0]
  b1 = m[0][1]
  c1 = m[0][2] * -1
  a2 = m[1][0]
  b2 = m[1][1]
  c2 = m[1][2] * -1
  if a1 / a2 != b1 / b2:
    x = (b1 * c2 - b2 * c1) // (a1 * b2 - a2 * b1)
    y = (c1 * a2 - c2 * a1) // (a1 * b2 - a2 * b1)
    return (x, y)
  else:
    return False

