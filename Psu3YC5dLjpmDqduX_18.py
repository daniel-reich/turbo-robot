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

import math
def angle(P1,P2):
    k=(P2[1]-P1[1])/((P1[0]-P2[0])**2+(P1[1]-P2[1])**2)**.5
    x1, x2=P1[0], P2[0]
    if k>=0:
        if x2>=x1:
            return 2*math.pi-math.asin(k)
        else:
            return math.pi+math.asin(k)
    else:
        if x2>=x1:
            return math.asin(-k)
        else:
            return math.pi-math.asin(-k)
def polygon(lst):
  rpt=[sum(x[0] for x in lst)/len(lst), sum(x[1] for x in lst)/len(lst)]
  lst=sorted(lst, key=lambda x: -angle(x, rpt))
  p=0
  n=0
  for i in range(len(lst)):
    sidx=(i+1)%len(lst)
    pd=lst[i][0]*lst[sidx][1]
    p+=pd
  for i in range(len(lst)):
    sidx=(i+1)%len(lst)
    pd=lst[sidx][0]*lst[i][1]
    n+=pd
  return (p-n)*.5

