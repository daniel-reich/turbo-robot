"""
Given a **unordered** list of the vertices of a **convex** polygon, find its
area.

### Examples

    polygon([[2, 5], [5, 1], [-4, 3]]) ➞ 15.0
    
    polygon([[-1, 1], [1, 1], [-1, -1], [1, -1]]) ➞ 4.0
    
    polygon([[2, 2], [11, 2], [4, 10], [9, 7]]) ➞ 45.5
    
    polygon([[5, 3], [3, 4], [12, 8], [5, 11], [9, 5]]) ➞ 39.0

### Notes

  * A convex polygon has all interior angles less than 180 degrees.
  * The first example has only 3 vertices so this list is ordered by default.

"""

import numpy as np
def lst_sorter(lst):
  sorted_list=[]
  x=[j[i] for j in lst for i in range(2) if i==0]
  y=[j[i] for j in lst for i in range(2) if i==1]
  sorted_list.append(lst[list(np.array(x)+y).index(max(np.array(x)+y))])
  nextpoint=lst[list(np.array(x)+y).index(max(np.array(x)+y))]
  lst.remove(lst[list(np.array(x)+y).index(max(np.array(x)+y))])
  while len(lst)>0:
    min_distance = 10**29
    for j in range(len(lst)):
      distance = ((lst[j][0]-nextpoint[0])**2 + (lst[j][1]-nextpoint[1])**2)**0.5
      if distance <= min_distance:
        min_distance=distance
        indexx=j
    nextpoint=lst[indexx]
    sorted_list.append(nextpoint)
    lst.remove(lst[indexx])
  return sorted_list
​
def polygon(lst):
  n,polyarea = len(lst),0
  lst1= lst_sorter(lst)
  for i in range(n):
    j = (i + 1) % n
    polyarea += lst1[i][0] * lst1[j][1]
    polyarea -= lst1[j][0] * lst1[i][1]
  polyarea = abs(polyarea) / 2.0
  return polyarea

