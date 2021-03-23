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
    v=len(lst)
    xc,yc=sum([lst[a][0] for a in range(v)])/v,sum([lst[a][1] for a in range(v)])/v
    lst=[[lst[a][0]-xc,lst[a][1]-yc] for a in range(v)]
    for a in range(v):
        lst[a].append(np.arctan2(lst[a][1],lst[a][0]))
    lst=sorted(lst,key=lambda h:h[2])
    lst.append(lst[0])    
    return abs(sum([lst[i][0]*lst[i+1][1]-lst[i][1]*lst[i+1][0] for i in range(v)])/2)

