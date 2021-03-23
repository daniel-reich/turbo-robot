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
    locations = {}
    for row in range(len(lst)):
        for col in range(len(lst[0])):
            if lst[row][col] != '0':
                locations[int(lst[row][col])] = (row, col)
    if len(locations.keys()) == 0:
        return 0
    ans = 0
    row1, col1 = locations[1]
    for i in range(2, max(locations.keys()) + 1):
        row2, col2 = locations[i]
        ans += abs(row1 - row2) + abs(col1 - col2)
        row1, col1 = row2, col2
    return ans

