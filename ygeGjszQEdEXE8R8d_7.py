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

from random import randrange as rand
import copy
​
def get_one_pos(M, H, W):
    for r in range(H):
        for c in range(W):
            if M[r][c] == 1:
                return r, c
​
def move(mat):
    return lambda x: move_it(copy.deepcopy(mat), x)
​
def move_it(Matrix, op):
    H, W = len(Matrix), len(Matrix[0])
    r1, c1 = get_one_pos(Matrix, H, W)
    if op == 'stop':
        return Matrix
    elif op == 'up':
        Matrix[r1][c1] = 0
        Matrix[(r1 - 1) % H][c1] = 1
    elif op == 'down':
        Matrix[r1][c1] = 0
        Matrix[(r1 + 1) % H][c1] = 1
    elif op == 'left':
        Matrix[r1][c1] = 0
        Matrix[r1][(c1 - 1) % W] = 1
    elif op == 'right':
        Matrix[r1][c1] = 0
        Matrix[r1][(c1 + 1) % W] = 1
    return lambda x: move_it(Matrix[:], x)

