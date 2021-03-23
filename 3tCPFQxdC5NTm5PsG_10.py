"""


You are given a list of `(x, y)` co-ordinates. Any three of these could be the
vertices of an **isosceles triangle**. Create a function that determines how
many **isosceles triangles** can be drawn from this scattering of points.
Vertices can be shared by multiple triangles.

### Examples

    find_triangles([(0, 0), (0, 4), (2, 2)]) ➞ 1
    
    find_triangles([(-10, -10), (-7, 3), (-3, 3), (-2, 7), (9, -7)]) ➞ 0
    
    find_triangles([(7, -5), (-7, -4), (1, 8), (-7, 5), (1, -3), (3, 1), (-1, 2), (3, -1), (-1, 1), (6, 4)])) ➞ 3
    
    # The 3 isosceles triangles for the last example are:
    # ((1, 8), (3, 1), (-1, 1))
    # ((1, -3), (3, 1), (-1, 1))
    # ((1, -3), (3, -1), (-1, 1))

### Notes

An isosceles triangle has two sides of equal length.

"""

from itertools import combinations
​
def find_triangles(lst):
    triangles = 0
    for (x1, y1), (x2, y2), (x3, y3) in combinations(lst, 3):
        a = round(((x1-x2)**2 + (y1-y2)**2)**0.5, 2)
        b = round(((x1-x3)**2 + (y1-y3)**2)**0.5, 2)
        c = round(((x2-x3)**2 + (y2-y3)**2)**0.5, 2)
        collinear = 0.5 * (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) == 0
        if (a == b or b == c or a == c) and not collinear:
            triangles += 1
    return triangles

