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
    highest_val = 0
    total_length = 0
    positions = []
    for i in range(len(lst)):
        if str(highest_val) < max(lst[i]):
            highest_val = int(max(lst[i]))
    while len(positions) < highest_val:
        for j in range(highest_val):
            for h in range(len(lst)):
                if lst[h].find(str(j+1)) >= 0:
                    positions.append([h,lst[h].find(str(j+1))])
    print(positions)
    for k in range(len(positions)-1):
        total_length += abs(positions[k][0]-positions[k + 1][0]) + abs(positions[k][1] - positions[k + 1][1])
    return total_length

