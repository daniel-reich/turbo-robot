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

def cp(first, second, sig):
    return "regular" if first * sig >= second * sig else "reflex"
​
def which_side(po, ve):
    c1 = min (po,key = lambda x:x[0] )
    c2 = max (po,key = lambda x:(x[0],-1*x[1]))
    c3 = max (po,key = lambda x:x[1] )
    p_c1, p_ve = po.index(c1), po.index(ve)
    new_lst, s21 = po[p_c1:]+po[:p_c1], c2[1]-c1[1]
    k2, k3, s31 = new_lst.index(c2), new_lst.index(c3), c3[1]-c1[1]
    i2 = s21/(c2[0]-c1[0]) if c2[0] !=c1[0] else s21*float("inf")
    i3 = s31/(c3[0]-c1[0]) if c3[0] !=c1[0] else s31*float("inf")
    sig = -1 if i2>i3 and k2<k3 or i2<i3 and k2>k3 else 1
    p1, p2, p3=po[p_ve-1], po[p_ve], po[p_ve+1] if p_ve+1<len(po) else po[0]
    if p2[0] == p1[0]:
        return cp(p2[0],p3[0],sig) if p3[1]>p2[1] else cp(p3[0],p2[0],sig)
    else:
        a = (p2[1]-p1[1])/(p2[0]-p1[0]); b = p1[1] - a * p1[0]
        y_t = a*p3[0]+b
        return cp(p3[1],y_t,sig) if p2[0]>p1[0] else cp(y_t,p3[1],sig)

