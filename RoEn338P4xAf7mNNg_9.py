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

def shortest_path(lst):
  target = 2
  times_moved = 0
  
  # Finds co-ords of all targets
  targets = {}
  for y, row in enumerate(lst):
    for x, col in enumerate(row):
      if col is not '0':
        targets[int(col)] = [x+1, y+1]
  
  # Finds number of moves (With no obsticals)
  while target in targets.keys():
    pos, tar_pos = targets[(target-1)], targets[target]
    
    times_moved += abs(abs(pos[0]-tar_pos[0]) + abs(pos[1]-tar_pos[1]))
    target += 1
    
  # Terribly inefficient
  return times_moved

