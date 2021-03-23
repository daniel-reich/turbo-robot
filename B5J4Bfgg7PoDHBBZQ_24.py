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

def within_triangle(p0,p1,p2,tr):
    t = abs((p0[0] * (p1[1] - p2[1]) + p1[0] * (p2[1] - p0[1]) + p2[0]
            * (p0[1] - p1[1])) / 2)
    t1 = abs((tr[0] * (p1[1] - p2[1]) + p1[0] * (p2[1] - tr[1]) + p2[0]
             * (tr[1] - p1[1])) / 2)
    t2 = abs((p0[0] * (tr[1] - p2[1]) + tr[0] * (p2[1] - p0[1]) + p2[0]
             * (p0[1] - tr[1])) / 2)
    t3 = abs((p0[0] * (p1[1] - tr[1]) + p1[0] * (tr[1] - p0[1]) + tr[0]
             * (p0[1] - p1[1])) / 2)
    return t == t1 + t2 + t3

