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
    xa, ya = p1
    xb, yb = p2
    xc, yc = p3
    xo, yo = test
    if (((xb-xo)*(yc-yo)-(xc-xo)*(yb-yo) >= 0 and 
        (xc-xo)*(ya-yo)-(xa-xo)*(yc-yo) >= 0 and 
        (xa-xo)*(yb-yo)-(xb-xo)*(ya-yo) >= 0) or
        ((xb-xo)*(yc-yo)-(xc-xo)*(yb-yo) <= 0 and 
        (xc-xo)*(ya-yo)-(xa-xo)*(yc-yo) <= 0 and 
        (xa-xo)*(yb-yo)-(xb-xo)*(ya-yo) <= 0)):
        return True
    else:
        return False

