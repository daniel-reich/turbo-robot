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
  ret = []
  for c in combinations(lst,3):
    temp = [list(i) for i in list(c)]
    x1,y1 = temp[0]
    x2,y2 = temp[1]
    x3,y3 = temp[2]
    if len(set([dist(x1,y1,x2,y2),dist(x1,y1,x3,y3),dist(x2,y2,x3,y3)]))==2:
      if len(set([slope(x1,y1,x2,y2),slope(x1,y1,x3,y3),slope(x2,y2,x3,y3)]))==3:
        if temp not in ret: 
          ret.append(temp)
  return len(ret)
  
def dist(x1,y1,x2,y2):
  return ((x2-x1)**2+(y2-y1)**2)**(1/2)
​
def slope(x1,y1,x2,y2):
  return (y2-y1)/(x2-x1) if x2-x1!=0 else None

