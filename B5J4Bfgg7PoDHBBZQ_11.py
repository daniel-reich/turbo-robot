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

def area(p1,p2,p3):
  return abs(p1[0]*(p2[1]-p3[1])+p2[0]*(p3[1]-p1[1])+p3[0]*(p1[1]-p2[1]))/2.0
​
def within_triangle(p1, p2, p3, test):
  A = area(p1,p2,p3)
  A1 = area(test,p2,p3)
  A2 = area(p1,test,p3)
  A3 = area(p1,p2,test)
  
  if A == A1+A2+A3:
    return True
  else:
    return False

