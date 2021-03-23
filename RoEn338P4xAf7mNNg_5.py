"""


Given a rectangular grid of m by n spaces, signaled by 0s, and a number of
points, signaled by 1, 2, 3..., return the number of moves for the shortest
path that starts at 1 and goes over all the other points in ascending order.

### Examples

    shortest_path([
      ("001"),
      ("002"),
      ("003")
    ]) ➞ 2
    
    shortest_path([
      ("00000"),
      ("01006"),
      ("02000"),
      ("30050"),
      ("00004")
    ]) ➞ 13
    
    shortest_path([
      ("00020000"),
      ("01000000")
    ]) ➞ 3

### Notes

  * Only horizontal and vertical movements are allowed.
  * All movements from one place to an adjacent one count as 1 regardless of direction.
  * The points range from 1 to at most 9 with no repeating or missing digits.

"""

from functools import reduce
def shortest_path(lst):
  p = sorted([(lst[r][c], r, c) for r in range(len(lst)) for c in range(len(lst[0])) if lst[r][c] > '0'])
  v, h = reduce(lambda m,i: (m[0]+abs(p[i][1]-p[i-1][1]), m[1]+abs(p[i][2]-p[i-1][2])), range(1, len(p)), (0,0))
  return v + h

