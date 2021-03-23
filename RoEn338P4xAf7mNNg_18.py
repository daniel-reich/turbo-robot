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
  A=[]
  for i in range(len(lst)):
    for j in range(len(lst[0])):
      if lst[i][j]!='0':
        A.append([int(lst[i][j]), (i,j)])
  A=sorted(A)
  B=[x[1] for x in A]
  C=[x for x in zip(B, B[1:])]
  return sum([abs(x[0][0]-x[1][0])+abs(x[0][1]-x[1][1]) for x in C])

