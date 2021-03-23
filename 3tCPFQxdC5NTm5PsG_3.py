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
def distance (tup1,tup2):
  return ((tup1[0]-tup2[0])**2 + (tup1[1]-tup2[1])**2)**.5
def find_triangles(lst):
  lst1,counter,keep=list(combinations(lst,3)),0,[]
  for k in range (len(lst1)):
    dist=[]
    for i in range (len(lst1[k])-1):
      for j in range(i+1,len(lst1[k])):
        dist.append(distance(lst1[k][i],lst1[k][j]))
    if len(dist)-len(set(dist))==1  and max(dist) < (sum([d for d in dist])-max(dist)) and lst1[k] not in keep:
      counter+=1
      keep.append(lst1[k])
  return counter

