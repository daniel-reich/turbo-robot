"""
Given a **unordered** list of the vertices of a **convex** polygon, find its
area.

### Examples

    polygon([[2, 5], [5, 1], [-4, 3]]) ➞ 15.0
    
    polygon([[-1, 1], [1, 1], [-1, -1], [1, -1]]) ➞ 4.0
    
    polygon([[2, 2], [11, 2], [4, 10], [9, 7]]) ➞ 45.5
    
    polygon([[5, 3], [3, 4], [12, 8], [5, 11], [9, 5]]) ➞ 39.0

### Notes

  * A convex polygon has all interior angles less than 180 degrees.
  * The first example has only 3 vertices so this list is ordered by default.

"""

import numpy as np
def polygon(lst):
  Ox, Oy = (sum(coor[0] for coor in lst)/len(lst),sum(coor[1] for coor in lst)/len(lst))
  lst = sorted(lst,key=lambda x: np.angle(complex(x[0]-Ox,x[1]-Oy)))
  v1 = sum(lst[i][0]*lst[(i+1)%len(lst)][1] for i in range(len(lst)))
  v2 = sum(lst[i][1]*lst[(i+1)%len(lst)][0] for i in range(len(lst)))
  return (v1-v2)/2

