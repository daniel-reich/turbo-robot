"""
Given a list of four points in the plane, determine if they are the vertices
of a parallelogram.

### Examples

    is_parallelogram([(0, 0), (1, 0), (1, 1), (0, 1)]) ➞ True
    
    is_parallelogram([(0, 0), (2, 0), (1, 1), (0, 1)]) ➞ False
    
    is_parallelogram([(0, 0), (1, 1), (1, 4), (0, 3)]) ➞ True
    
    is_parallelogram([(0, 0), (1, 2), (2, 1), (3, 3)]) ➞ True
    
    is_parallelogram([(0, 0), (1, 0), (0, 1), (1, 1)]) ➞ True

### Notes

The points may be given in any order (compare examples #1 and #5).

"""

def is_parallelogram(lst):
  A, B, C, D = lst
  p1 = slope(A,B) == slope(C,D)
  p2 = slope(A,C) == slope(B,D)
  p3 = slope(A,D) == slope(B, C)
  return p1 + p2 + p3 == 2
​
def slope(a, b):
  rise = b[1] - a[1]
  run = b[0] - a[0]
  return rise/run if run else rise

