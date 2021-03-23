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
​
def distance_pow2(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
​
​
def find_triangles(lst):
    count = 0
    for comb in combinations(lst, 3):
        edges = [distance_pow2(*edge) for edge in combinations(comb, 2)]
        if len(set(edges)) == 2:
            a, b = 0, 0
            for x in set(edges):
                if edges.count(x) == 2:
                    a = x
                elif edges.count(x) == 1:
                    b = x
            if 2 * (a ** 0.5) > b ** 0.5:
                count += 1
    return count

