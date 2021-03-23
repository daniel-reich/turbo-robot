"""


This challenge concerns non-convex polygons, such as the two polygons depicted
below. ![Non-convex polygons](https://edabit-
challenges.s3.amazonaws.com/Polygon_sides_smaller+copy.png)

One special property of non-convex polygons is that, for some of their
vertices, the angle around that vertex that is contained inside the polygon is
a _reflex angle_ , i.e. an angle of more than 180 degrees. For this reason:

  * In the left polygon above we say that `(1, 1), (3, 1)` are _reflex vertices_ (since the angle inside the polygon is a reflex angle) while `(0, 0), (4, 0), (2, 5)` are _regular vertices_.
  * In the right polygon we say that `(1, 1)` is a reflex vertex while all the other vertices are regular vertices.

Write a function which given:

  * A polygon described as a list of vertices where each vertex connects to the next and the last connects to the first (e.g. the polygons above are described by `[(0, 0), (4, 0), (3, 1), (2, 5), (1, 1)]` and `[(0, 0), (4, 0), (3, 1), (1, 1), (2, 5)]`) and ...
  * One of the vertices of the polygon.

 **Determines if the given vertex is a`"regular"` vertex or a `"reflex"`
vertex.**

### Examples (using the polygons depicted above)

    which_side([(0, 0), (4, 0), (3, 1), (2, 5), (1, 1)], (3, 1)) ➞ "reflex"
    
    which_side([(0, 0), (4, 0), (3, 1), (2, 5), (1, 1)], (0, 0)) ➞ "regular"
    
    which_side([(0, 0), (4, 0), (3, 1), (1, 1), (2, 5)], (3, 1)) ➞ "regular"
    
    which_side([(0, 0), (4, 0), (3, 1), (1, 1), (2, 5)], (1, 1)) ➞ "reflex"

### Notes

  * The order of the vertices is important when specifying the polygon and thus affects whether each vertex is reflex or not (e.g. the two polygons above have the exact same vertices, but `(3,1)` is reflex in the left polygon and regular in the right polygon).
  * In both examples above the vertices of the polygons are listed in counter-clockwise order, but the tests will include both clockwise and counter-clockwise order cases.

"""

def which_side(poly, vert):
    # reverse order of vertices if orientation is clockwise
    if sum([(p2[0]-p1[0])*(p2[1]+p1[1]) for p1, p2 in zip(poly, (poly+[poly[0]])[1:])]) > 0:
        poly = poly[::-1]
    vi, pl = poly.index(vert), len(poly)
    # translate preceding, target and succeeding points so that preceding is origin (0, 0)
    x1, y1 = poly[vi-1][0], poly[vi-1][1]
    x2, y2, x3, y3 = vert[0] - x1, vert[1] - y1, poly[(vi+1)%pl][0] - x1, poly[(vi+1)%pl][1] - y1
    # determinant of succeeding and target point vectors determines whether target is 
    # left or right of line joining preceding (origin) to succeeding
    return 'reflex' if (x3 * y2 - y3 * x2) > 0 else 'regular'

