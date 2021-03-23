"""


Create a function which takes a parameter `mat`, where `mat` is a matrix
(`list` of `list`s) such that all but one entry equals `0` (and the non-zero
entry equals `1`). The function, after being passed a matrix, should be
repeatedly callable with the following `str` commands:

  * `"up"` ➞ Move the `1` to the cell above it.
  * `"down"` ➞ Move the `1` to the cell below it.
  * `"left"` ➞ Move the `1` to the cell to the left of it.
  * `"right"` ➞ Move the `1` to the cell to the right of it.
  * `"stop"` ➞ Return the resulting matrix.

### Examples

    one = [
      [1]
    ]
    
    two = [
      [1, 0],
      [0, 0]
    ]
    
    # Should work for 1×1 matrices
    move(one)("up")("stop") ➞ [
      [1]
    ]
    
    # The 1 should wrap around
    move(two)("left")("stop") ➞ [
      [0, 1],
      [0, 0]
    ]
    
    # Should accept multiple commands
    move(two)("right")("down")("stop") ➞ [
      [0, 0],
      [0, 1]
    ]
    
    # Should return a function
    callable(move(two)) ➞ True

### Notes

  * The matrix can be of any size `m×n`, where `m ≥ 1` and `n ≥ 1`.
  * The `1` should be able to wrap around, e.g. if the non-zero entry is at the top of the matrix, calling the command `'up'` should move it to the bottom of the matrix.
  * The result of the original function `move` should be callable an arbitrary number of times.

"""

from copy import deepcopy
class Move:
  dirn = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
  
  def __init__(self, mat):
    self.height = len(mat)
    self.width = len(mat[0])
    for r, c in [(r,c) for r in range(self.height) for c in range(self.width)]:
      if mat[r][c] == 1:
        break
    self.r, self.c, self.mat = r, c, deepcopy(mat)
​
  def make_move(self, m):
    if m == 'stop':
      return self.mat
    if m in self.dirn:
      self.set_pos(self.r, self.c, 0)
      dr, dc = self.dirn[m]
      self.r = (self.r + self.height + dr) % self.height
      self.c = (self.c + self.width + dc) % self.width
      self.set_pos(self.r, self.c, 1)
      return self.make_move
​
  def set_pos(self, r, c, v):
    self.mat[r][c] = v
​
def move(mat):
  return Move(mat).make_move

