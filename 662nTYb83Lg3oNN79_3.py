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

from itertools import permutations as p
def is_parallelogram(lst):
  slope = lambda p1, p2: abs(p1[0]-p2[0])/abs(p1[1]-p2[1])
  for A, B, C, D in p(lst,4):
    try:
      if slope(A, B) == slope(C, D) and slope(A, D) == slope(B, C):
        return True
    except:
      pass
  return False

