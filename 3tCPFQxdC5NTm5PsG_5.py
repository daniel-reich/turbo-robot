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
def is_iso(t):
    d, ang, comb, p1, p2 = [0, 0, 0], [0, 0], [[0,1],[1,2],[0,2]], 0, 0
    for i in comb:
        d[p1] = (t[i[0]][0]-t[i[1]][0])**2+(t[i[0]][1]-t[i[1]][1])**2
        p1 += 1
    if any(d[i[0]] == d[i[1]] for i in comb):
        for j in comb[:2]:
            if t[j[0]][0] == t[j[1]][0]: ang[p2] = float('inf')
            else: ang[p2] = (t[j[0]][1]-t[j[1]][1])/(t[j[0]][0]-t[j[1]][0])
            p2 += 1
    return ang[1] != ang[0]
​
def find_triangles(lst):
    comb, soma = combinations(range(len(lst)), 3), 0
    for i in comb: soma += is_iso([lst[i[0]], lst[i[1]], lst[i[2]]])
    return soma

