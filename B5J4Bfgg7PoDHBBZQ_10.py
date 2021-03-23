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
  return area([p1,p2,p3])==area([test,p1,p2])+area([test,p2,p3])+area([test,p1,p3])
    
def area(p_l):
  return abs(sum(p_l[i%3][0]*(p_l[(i+1)%3][1]-p_l[(i+2)%3][1]) for i in range(3)))

