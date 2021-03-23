"""


You will be given the location of a knight, and an end location. The knight
can move in a "L" shape. "L" shape movement means that the knight can change
it's `x` coordinate by 2 and it's `y` coordinate by 1 or it can change it's
`y` coordinate by 2 and it's `x` coordinate by 1 (you can add and subtract
from the x/y).

For example, if the knight is at the position (0, 0), it can move to:

    (1,2), (1,-2), (2,1), (2,-1), (-1,2), (-1,-2), (-2,1), (-2, -1)

Your job is to return the least amount of steps needed to go from the position
K (knight's start position) to E (end). You will only be given the knight
starter coordinates (x1, y1) and the end coordinates (x2, y2).

Constrains: `1 <= x1,y1,x2,y2 <= 8`

### Examples

    knight_bfs(1, 1, 8, 8) ➞ 6
    
    knight_bfs(1, 1, 3, 2) ➞ 1
    
    knight_bfs(8, 8, 3, 3) ➞ 4

### Notes

  * This is a simplified version of [this problem](https://www.spoj.com/problems/NAKANJ/).
  * This travel will always be possible.
  * The chess board is 8x8.

"""

def pos_add(x, y):
  return(x[0] + y[0], x[1] + y[1])
def in_bounds(p):
  return p[0] > 0 and p[0] < 9 and p[1] > 0 and p[1] < 9
​
knight_moves = [(1,2), (1,-2), (2,1), (2,-1), (-1,2), (-1,-2), (-2,1), (-2, -1)]
​
def knight_bfs(a, b, c, d):
  p0 = (a, b)
  pf = (c, d)
  bfs_queue  = [p0]
  dist_map = {p0 : 0}
  
  def bfs_visit(p):
    for np in filter(in_bounds, [pos_add(p, m) for m in knight_moves]):
      if np not in dist_map:
        dist_map[np] = dist_map[p] + 1
        bfs_queue.append(np)
  
  while (pf not in dist_map) and (len(bfs_queue) > 0):
    bfs_visit(bfs_queue.pop(0))
  
  return dist_map.get(pf, None)

