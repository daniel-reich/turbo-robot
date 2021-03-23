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
    vertical, horizontal = 0, 0
    coords = []
    
    for r in range(len(lst)):
        for c in range(len(lst[0])):
            if lst[r][c] != '0':
                coords.append((lst[r][c], r, c))
    coords.sort()
    
    for (_, r1, c1), (_, r2, c2) in zip(coords, coords[1:]):
        vertical += abs(r1 - r2)
        horizontal += abs(c1 - c2)
    
    return vertical + horizontal

