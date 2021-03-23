"""


Create a function that takes four tuples. The first three are (x, y)
coordinates of three corners of a triangle. Return `True` if the fourth tuple
— the (x, y) coordinates of a test point — lies within the triangle, `False`
if it doesn't.

### Examples

    within_triangle((1, 4), (5, 6), (6, 1), (4, 5)) ➞ True
    
    within_triangle((1, 4), (5, 6), (6, 1), (3, 2)) ➞ False
    
    within_triangle((-6, 2), (-2, -2), (8, 4), (4, 2)) ➞ True

### Notes

N/A

"""

def within_triangle(p1, p2, p3, test):
    a = (p2[0]-p1[0], p2[1]-p1[1])
    b = (p3[0]-p1[0], p3[1]-p1[1])
    v = (test[0]-p1[0], test[1]-p1[1])
    D = a[0] * b[1] - b[0] * a[1]
    Ds = v[0] * b[1] - b[0] * v[1]
    Dt = a[0] * v[1] - v[0] * a[1]
    s = Ds / D
    t = Dt / D
    return s >= 0 and t >= 0 and s + t <= 1

