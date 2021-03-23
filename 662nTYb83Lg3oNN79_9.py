"""
Given a list of four points in the plane, determine if they are the vertices
of a parallelogram.

### Examples

    is_parallelogram([(0, 0), (1, 0), (1, 1), (0, 1)]) ➞ True
    
    is_parallelogram([(0, 0), (2, 0), (1, 1), (0, 1)]) ➞ False
    
    is_parallelogram([(0, 0), (1, 1), (1, 4), (0, 3)]) ➞ True
    
    is_parallelogram([(0, 0), (1, 2), (2, 1), (3, 3)]) ➞ True
    
    is_parallelogram([(0, 0), (1, 0), (0, 1), (1, 1)]) ➞ True

### Notes

The points may be given in any order (compare examples #1 and #5).

"""

from itertools import permutations
def is_parallelogram(lst):
  lst = [list(i) for i in lst]
  perm = [list(p) for p in permutations(lst,2)]
  slopes = [slope(i) for i in perm]
  slopes = [str(i) for i in slopes if i!=None]
  slopes = list(set(slopes))
  return len(slopes)<=4
  
def slope(lst):
  x1,y1 = lst[0]
  x2,y2 = lst[1]
  return (y2-y1)/(x2-x1) if (x2-x1)!=0 else None

