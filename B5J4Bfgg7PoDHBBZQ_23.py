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

def line_eq(p1, p2):
    #if x = cnt
    if p1[0] == p2[0]:
        return p1[0]
​
    def y(x):
        return x*(p1[1] - p2[1])/(p1[0] - p2[0]) + p1[1] - p1[0]*(p1[1] - p2[1])/(p1[0] - p2[0])
​
    return y
​
def same_side(p1, p2, line):
    #if x = cnt 
    if isinstance(line, int):
        return (p1[0] >= line and p2[0] >= line) or (p1[0] >= line and p2[0] >= line)
​
    if (p1[1] >= line(p1[0]) and p2[1] >= line(p2[0])) or (p1[1] <= line(p1[0]) and p2[1] <= line(p2[0])):
        return True
    return False
​
def within_triangle(p1, p2, p3, test):
    line1 = line_eq(p1, p2)
    line2 = line_eq(p1, p3)
    line3 = line_eq(p2, p3)
​
    if same_side(p1, test, line3) and same_side(p2, test, line2) and same_side(p3, test, line1):
        return True
    return False

