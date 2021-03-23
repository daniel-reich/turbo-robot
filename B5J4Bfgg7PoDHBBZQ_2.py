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
    (x1, y1), (x2, y2), (x3, y3) = sorted((p1, p2, p3), key=lambda x:(x[1]))
    d1 = (y2 - y1)*(test[0] - x1) + (-x2 + x1)*(test[1] - y1)
    d2 = (y3 - y2)*(test[0] - x2) + (-x3 + x2)*(test[1] - y2)
    d3 = (y1 - y3)*(test[0] - x3) + (-x1 + x3)*(test[1] - y3)
    return all(i >= 0 for i in (d1, d2, d3))

