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
    stored, distance = [], 0
    for l,line in enumerate(lst):
        for c,v in enumerate(line):
            if v!= "0":
                stored.append([int(v),l,c])
    if len(stored) < 2:
        return 0
    stored.sort()
    _, s_li, s_co = stored.pop(0)
    for _,li,co in stored:
        distance += abs(s_li-li)+abs(s_co-co)
        s_li, s_co = li, co
    return distance

