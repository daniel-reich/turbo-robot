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

from itertools import*
d=lambda x,y:((x[0]-y[0])**2+(x[1]-y[1])**2)**.5
f=lambda a,b,c,d,e,k:a*(d-k)+c*(k-b)+e*(b-d)==0
find_triangles=lambda l:sum(not f(a[0],a[1],b[0],b[1],c[0],c[1])and(d(a,b)==d(a,c)or d(a,b)==d(c,b)or d(a,c)==d(c,b))for a,b,c in combinations(l,3))

