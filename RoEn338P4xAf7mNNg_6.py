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
  def string(i):
    return lst[i]
  def row(n):
    return list(filter(lambda x: str(n) in string(x),range(0,len(lst))))[0]
  def col(n):
    return string(row(n)).index(str(n))
  def distance(a,b):
    return abs(row(a)-row(b)) + abs(col(a)-col(b))
  i = 1;
  total = 0;
  while i < 9:
    try:
      total += distance(i,i+1)
      i += 1
    except IndexError:
      return total
  return total

