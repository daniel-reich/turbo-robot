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
​
  class Polygon:
    
    def __init__(self, verts):
      self.verts = verts
    
    def is_reflex(self, vert):
      def area_finder(verts):
        to_add1 = []
        to_add2 = []
​
        for n in range(len(verts)):
          x1 = verts[n][0]
          y1 = verts[n][1]
          try:
            x2 = verts[n+1][0]
            y2 = verts[n+1][1]
          except IndexError:
            x2 = verts[0][0]
            y2 = verts[0][1]
​
          to_add1.append(x1*y2)
          to_add2.append(x2*y1)
        
        in_brackets = sum(to_add1) - sum(to_add2)
​
        area = in_brackets / 2
​
        return abs(area)
      
      without_vert = []
​
      for point in self.verts:
        if point != vert:
          without_vert.append(point)
      
      with_vert_area = area_finder(self.verts)
      without_vert_area = area_finder(without_vert)
​
      return without_vert_area > with_vert_area
​
  polygon = Polygon(poly)
​
  if polygon.is_reflex(vert) == True:
    return 'reflex'
  else:
    return 'regular'

