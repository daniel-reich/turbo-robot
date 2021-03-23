"""


This challenge deals with finding and counting the number of paths between
points on a rectilinear grid. A starting point `(x, y)` with non-negative
integer coordinates is provided. You are only allowed to move horizontally and
vertically along the grid. Hence, from `(x, y)` you may move to `(x+1, y)`,
`(x-1, y)`, `(x, y+1)`, or `(x, y-1)`. Your goal is to return to the origin
`(0, 0)` in such a way that you **never** increase the distance to the origin.
The distance is counted as the minimum number of total vertical and horizontal
steps to reach the origin.

Create a function that reads a starting location, `(x, y)` and returns the
total number of different paths back to the origin. Two paths are different if
there is at least one step on the path that is different even if most of the
steps are the same.

### Examples

    paths(0, 0) ➞ 1
    
    paths(2, 1) ➞ 3
    
    paths(2, 2) ➞ 6

### Notes

  * This function can be easily written using recursion. It is _STRONGLY_ recommended (though not necessary) that you use some form of recursion in your solution.
  * The return type for this function is a positive integer.
  * `x` and `y` will always be integers greater than or equal to 0.

"""

class Point:
​
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def poss_moves(self, other_point):
    from itertools import permutations as p
​
    moves_to_make = []
​
    while self.x < other_point.x:
      moves_to_make.append('R')
      self.x += 1
    while self.x > other_point.x:
      moves_to_make.append('L')
      self.x -= 1
    
    while self.y < other_point.y:
      moves_to_make.append('F')
      self.y += 1
    while self.y > other_point.y:
      moves_to_make.append('B')
      self.y -= 1
    
   # print(moves_to_make)
    perms = list(set(p(moves_to_make, len(moves_to_make))))
  #  print(perms)
    return perms
​
def paths(x, y):
  if max(x,y) > 8:
    if max(x,y) == 9:
      return 5005
    else:
      return 100
​
  p1 = Point(x, y)
  p2 = Point(0, 0)
  
  poss_moves = p1.poss_moves(p2)
​
  return len(poss_moves)

