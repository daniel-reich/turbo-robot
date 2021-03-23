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

import numpy as np
from itertools import combinations
​
def slope(p1,p2):
    if p2[0]==p1[0]: return 'inf'
    return (p2[1]-p1[1])/(p2[0]-p1[0])
​
def istri(lst):
    return len({slope(lst[0],lst[1]), slope(lst[1],lst[2]), slope(lst[2],lst[0])}) == 3
​
def sqdist(p1, p2):
    return (p1[0]-p2[0])**2+(p1[1]-p2[1])**2
​
def isiso(lst):
    return len({sqdist(lst[0],lst[1]),sqdist(lst[1],lst[2]),sqdist(lst[2],lst[0])}) < 3
def find_triangles(lst):
    return sum(map(lambda x: isiso(x) and istri(x),combinations(lst,3)))

