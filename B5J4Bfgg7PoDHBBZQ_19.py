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
  return area(p1,p2,p3) == (area(p1,p2,test)+area(p1,p3,test)+area(p2,p3,test))
  
def area(a,b,c):
  x1,y1 = a
  x2,y2 = b
  x3,y3 = c
  return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2)

