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
    s, r = [], 0
    for h, i in enumerate(lst):
        for j, k in enumerate(i):
            if k != "0":
                add = [int(k), h, j]
                s.append(add)
                
    s = sorted(s, key=lambda x : x[0])
    if not s:
        return 0
    x, y = s[0][1], s[0][2]
    
    for z in range(1, len(s)):
        r += abs(x - s[z][1]) + abs(y - s[z][2])  
        x, y = s[z][1], s[z][2]
    return r

