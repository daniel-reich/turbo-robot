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

from math import pi, atan2
from functools import reduce
def polygon(lst):
    # calculate avarage of points
    x,y = reduce(lambda p1, p2: (p1[0]+p2[0], p1[1]+p2[1]), lst)
    p0 = [x/len(lst), y/len(lst)]
    # sort by angle 
    lst.sort(key=lambda p: ((atan2(p0[1]-p[1], p0[0]-p[0]) * 180 / pi) + 360)%360)
    # apply polygon area formula 
    return abs(sum(p1[0]*p2[1] - p2[0]*p1[1] for p1, p2 in zip(lst, lst[1:] + [lst[0]]))) / 2

