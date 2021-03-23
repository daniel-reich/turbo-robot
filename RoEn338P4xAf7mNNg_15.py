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
    steps = 0
    current = 1
    end = int(lst[0][0])
    for i in range(0,len(lst)):
        if "1" in lst[i]:
            row = i
            position = lst[i].index("1")
        if max([int(y) for y in lst[i]]) > end:
            end = max([int(y) for y in lst[i]])
    for step in range(1,end): 
        for i in range(0,len(lst)):
            if str(step+1) in lst[i]:
                steps += abs(row-i)+abs(position-lst[i].index(str(step+1)))
                row = i
                position = lst[i].index(str(step+1))
    return steps

