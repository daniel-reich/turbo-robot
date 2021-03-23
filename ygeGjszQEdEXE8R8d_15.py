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

def row_1(m):
  return [i for i in range(len(m)) if 1 in m[i]][-1]
​
def move(mat):
  
  def clo(step):
    nonlocal mat
    r = len(mat)
    c = len(mat[0])
​
    if step in 'updown':
      i = row_1(mat)
      p = (i - 1, i + 1)[step == 'down']
      temp_row = mat[p % r]
      mat[p % r], mat[i] = mat[i], mat[p % r]
​
    if step in 'leftright':
      mat = list(zip(*mat))
      i = row_1(mat)
      p = (i - 1, i + 1)[step == 'right']
      temp_row = mat[p % c]
      mat[p % c], mat[i] = mat[i], mat[p % c]
      mat = list(list(r) for r in zip(*mat))
​
    return mat if step == 'stop' else clo
  
  return clo

