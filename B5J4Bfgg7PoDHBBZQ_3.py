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

def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)
​
​
def within_triangle(p1, p2, p3, test):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = test
    a = area(x1, y1, x2, y2, x3, y3)
    a1 = area(x1, y1, x2, y2, x4, y4)
    a2 = area(x1, y1, x3, y3, x4, y4)
    a3 = area(x2, y2, x3, y3, x4, y4)
    return a1 + a2 + a3 == a

