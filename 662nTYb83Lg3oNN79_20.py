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

import math
def distance(t1,t2):
  x1 = t1[0]
  x2 = t2[0]
  y1 = t1[1]
  y2 = t2[1]
  return math.hypot(x1-x2,y1-y2)
def is_parallelogram(lst):
  if distance(lst[0],lst[1]) == distance(lst[2],lst[3]):
    return True
  elif distance(lst[0],lst[2]) == distance(lst[1],lst[3]):
    return True
  elif distance(lst[0],lst[3]) == distance(lst[1],lst[2]):
    return True
  else:
    return False

