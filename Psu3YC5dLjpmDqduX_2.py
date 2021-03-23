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

def polygon(lst):
  lst = [[e[0]-lst[0][0],e[1]-lst[0][1]] for e in lst]
  lst = sorted(lst[1:], key = lambda e: sum(e[0]*f[1]-e[1]*f[0]>0 for f in lst))
  lst = [[0,0]]+lst+[[0,0]]
  return abs(sum((lst[i][1]*lst[i-1][0]-lst[i][0]*lst[i-1][1])/2 for i in range(1,len(lst))))

