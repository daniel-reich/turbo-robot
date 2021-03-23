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

import itertools
import math
​
def get_sq_distance(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
​
def find_triangles(lst):
    ans = 0
    for comb in itertools.combinations(lst, 3):
        p1, p2, p3 = comb
        v1 = [p1[0] - p2[0], p1[1] - p2[1]]
        v2 = [p3[1] - p1[1], p3[0] - p1[0]]
        dists = [get_sq_distance(p1, p2), get_sq_distance(p2, p3), get_sq_distance(p1, p3)]
        a, b, c = [math.sqrt(d) for d in dists        ]
        if len(set(dists)) < 3 and \
           a+b > c and b+c > a and a+c >b:
            ans += 1
    return ans

