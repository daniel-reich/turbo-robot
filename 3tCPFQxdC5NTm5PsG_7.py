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
def find_triangles(lst):
  side = lambda p1, p2: (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
​
  count = 0
  for perm in combinations(lst, 3):
    A, B, C = perm
    if (B[1] - A[1]) * (C[0] - A[0]) != (C[1] - A[1]) * (B[0] - A[0]):
      s1, s2, s3 = side(A, B), side(B, C), side(C, A)
      if s1 == s2 or s2 == s3 or s3 == s1:
        count += 1
  return count

