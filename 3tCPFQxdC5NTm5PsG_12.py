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
from math import hypot
def is_isosceles(lst):
  lines = list(map(lambda x: hypot(x[0][0] - x[1][0],x[0][1]-x[1][1]),list(combinations(lst,2))))
  return len(set(lines)) == 2 and sum(sorted(lines)[:2]) > max(lines)
def find_triangles(lst):
  return len(list(filter(lambda x: is_isosceles(x),list(combinations(lst,3)))))

