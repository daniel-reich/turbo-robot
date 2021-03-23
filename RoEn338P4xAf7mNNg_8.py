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

def shortest_path(grid):
    '''
    Returns the number of moves in the shortest path through the grid as per
    the instructions
    '''
    man_dist = lambda x,y: abs(x[1][0] - y[1][0]) + abs(x[1][1] - y[1][1])
    
    locs = sorted([(grid[i][j],(i,j)) for i in range(len(grid))
                   for j in range(len(grid[0]))
                   if grid[i][j] > '0'])
​
    
​
    return sum(man_dist(a,b) for a,b in zip(locs,locs[1:]))

