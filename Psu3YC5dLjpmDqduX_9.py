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

from math import atan, pi
​
​
def get_bearing(p1, p2):
    p1x, p1y = p1
    p2x, p2y = p2
​
    deg = atan((p2y - p1y) / (p2x - p1x))
    if p2y > p1y:
        return deg if p2x > p1x else pi + deg
    elif p2y < p1y:
        return 2*pi + deg if p2x > p1x else pi + deg
    elif p2y == p1y:
        return 0 if p2x > p1x else pi
​
​
def shoelace(vert):
    vert.append(vert[0])
    return (1/2) * abs(sum([vert[i][0] * vert[i+1][1] for i in range(len(vert) - 1)]) - sum([vert[i][1] * vert[i+1][0] for i in range(len(vert) - 1)]))
​
​
def vertices_sort(vert):
    """Vertices sorted with their angle bearing from the East, anticlockwise"""
    center = sum([x[0] for x in vert])/len(vert), sum([y[1] for y in vert])/len(vert)
    return sorted(vert, key=lambda v: get_bearing(center, v))
​
​
def polygon(lst):
    return shoelace(vertices_sort(lst))

