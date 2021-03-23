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

def areaTri(x1,y1,x2,y2,x3,y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)
                + x3 * (y1 - y2)) / 2)
​
def within_triangle(p1, p2, p3, test):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    x3 = p3[0]
    y3 = p3[1]
    x = test[0]
    y = test[1]
​
    A = areaTri (x1, y1, x2, y2, x3, y3)
    A1 = areaTri (x, y, x2, y2, x3, y3)
    A2 = areaTri (x1, y1, x, y, x3, y3)
    A3 = areaTri (x1, y1, x2, y2, x, y)
    return A == A1+A2+A3

