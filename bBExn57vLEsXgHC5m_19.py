"""


Create a function that returns `True` if three points belong to the same line,
and `False` otherwise. Each point is represented by a list consisting of an x-
and y-coordinate.

### Examples

    same_line([[0, 0], [1, 1], [3, 3]]) ➞ True
    
    same_line([[-2, -1], [2, 1], [0, 0]]) ➞ True
    
    same_line([[-2, 0], [-10, 0], [-8, 0]]) ➞ True
    
    same_line([[0, 0], [1, 1], [1, 2]]) ➞ False
    
    same_line([[3, 4], [3, 5], [6, 6]]) ➞ False

### Notes

Note the special case of a vertical line.

"""

import math
def same_line(lst):
  a,b,c = lst
  ax,ay,bx,by,cx,cy = a[0],a[1],b[0],b[1],c[0],c[1]
  ab = math.sqrt((by-ay)**2 + (bx-ax)**2)
  ac = math.sqrt((cy-ay)**2 + (cx-ax)**2)
  bc = math.sqrt((cy-by)**2 + (cx-bx)**2)
  dist = [ab,ac,bc]
  s = 0
  for a in dist:
    if a != max(dist):
      s+=a
  return abs(s  - max(dist)) < 0.01

