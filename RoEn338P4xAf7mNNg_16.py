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
    pos, max_char = dict(), 0
    for r, tpl in enumerate(lst):
        for c, char in enumerate(tpl):
            if char in '123456789':
                pos[int(char)] = (r, c)
                if int(char) > max_char:
                    max_char = int(char)
    return sum(abs(pos[i][1] - pos[i - 1][1]) + abs(pos[i][0] - pos[i - 1][0])
               for i in range(2, max_char + 1))

