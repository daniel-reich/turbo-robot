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

from math import asin, pi
​
​
def polygon(lst):
    res = lst
    if len(lst) > 3:
        center_x = sum(p[0] for p in lst) / len(lst)
        center_y = sum(p[1] for p in lst) / len(lst)
​
        def angle_from_center(p):
            x = p[0] - center_x
            y = p[1] - center_y
            angle = asin(abs(y) / (x * x + y * y) ** 0.5)
            if x < 0 <= y:
                angle = pi - angle
            elif x < 0 and y < 0:
                angle += pi
            elif y < 0 <= x:
                angle = 2 * pi - angle
            return angle
        lst.sort(key=angle_from_center)
    area = 0
    for i in range(len(res) - 1):
        area += res[i][0] * res[i + 1][1] - res[i][1] * res[i + 1][0]
    area += res[len(res) - 1][0] * res[0][1] - res[len(res) - 1][1] * res[0][0]
    return abs(area) / 2

