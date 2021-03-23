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

def in_triangle(l1,l2,l3,p0):
    return (above_line(l1,p0),above_line(l2,p0),above_line(l3,p0))
def above_line(l,p):
    x= p[0];y=p[1]
    m=l[0];c=l[1]
    if y >= m*x +c:
        return True
    else:
        return False
​
def Line(p1, p2):
    m = (p2[1] - p1[1])/(p2[0] - p1[0])
    c = p1[1] - p1[0]*m
    return (m, c)
​
def within_triangle(p1, p2, p3, test):
    l1 = Line(p1,p2)
    l2 = Line(p2,p3)
    l3 = Line(p1,p3)
    mid = (((p1[0]+p2[0]+p3[0]) /3),((p1[1]+p2[1]+p3[1])/3))
​
    ideal = in_triangle(l1,l2,l3,mid)
​
    if in_triangle(l1,l2,l3,test) == ideal:
        return True
    else:
        return False

