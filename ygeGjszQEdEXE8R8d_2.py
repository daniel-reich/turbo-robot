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

def move(mat):
    n, m = len(mat), len(mat[0])
    i = [sum(l) for l in mat].index(1)
    j = mat[i].index(1)
    print(n, m, i, j)
    return move_coor(n, m, i, j)
​
​
def move_coor(n, m, i, j):
    def meh(str):
        if str == 'stop':
            ans = [[0]*m for _ in range(n)]
            ans[i][j] = 1
            return ans
        if str == 'up':
            return move_coor(n, m, (i-1)%n, j)
        if str == 'down':
            return move_coor(n, m, (i+1)%n, j)
        if str == 'right':
            return move_coor(n, m, i, (j+1)%m)
        if str == 'left':
            return move_coor(n, m, i, (j-1)%m)
        return move_coor(n, m, i, j)
    return meh

