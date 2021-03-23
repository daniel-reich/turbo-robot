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
    pnts = []
    for y, row in enumerate(lst):
        for x, n in enumerate(row):
            if n != '0':
                pnts.append((int(n), x, y))
    pnts.sort()
    return sum(abs(x2-x1)+abs(y2-y1) for (n1,x1,y1), (n2,x2,y2) in
               zip(pnts, pnts[1:]))

