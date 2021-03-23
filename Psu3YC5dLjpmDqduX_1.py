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
import functools
​
def poly_area(polygon, M):
    A = 0
    for i in range(M):
        x1, y1 = polygon[i][0], polygon[i][1]
        x2, y2 = polygon[(i+1)%M][0], polygon[(i+1)%M][1]
        A += (x1 * y2 - x2 * y1)
    return abs(A / 2.)
​
def compare(p1, p2):
    angle1 = (360 + math.atan2(p1[0], p1[1])) % 360
    angle2 = (360 + math.atan2(p2[0], p2[1])) % 360
    if angle1 == angle2:
        return 0
    return 1 if angle1 > angle2 else -1
    
def polygon(lst):
    # determine centroid coordinates:
    n = len(lst)
    cx = sum([p[0] for p in lst])/ n
    cy = sum([p[1] for p in lst])/ n
    points = []
    for [x, y] in lst:
        points.append([x - cx, y - cy])
    points.sort(key=functools.cmp_to_key(compare))
    return round(poly_area(points, len(points)), 1)

