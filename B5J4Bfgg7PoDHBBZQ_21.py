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
  area = abs((p1[0]*(p2[1] - p3[1]) + p2[0]*(p3[1] - p1[1]) + p3[0]*(p1[1]-p2[1]))/2)
  a1 = abs((test[0]*(p2[1] - p3[1]) + p2[0]*(p3[1] - test[1]) + p3[0]*(test[1]-p2[1]))/2)
  a2 = abs((p1[0]*(test[1] - p3[1]) + test[0]*(p3[1] - p1[1]) + p3[0]*(p1[1]-test[1]))/2)
  a3 = abs((p1[0]*(p2[1] - test[1]) + p2[0]*(test[1] - p1[1]) + test[0]*(p1[1]-p2[1]))/2)
  return a1 + a2 + a3 == area

