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
  matrix = {(i,j): num for j, line in enumerate(mat) for i, num in enumerate(line)}
  imax = max(key[0] for key in matrix.keys())+1
  jmax = max(key[1] for key in matrix.keys())+1
  def movement(string):
    one = [k for k,v in matrix.items() if v == 1][0]  
    if string == "right":
      matrix[one] = 0
      one = ((one[0]+1)%imax, one[1])
      matrix[one] = 1
      return movement
    if string == "left":
      matrix[one] = 0
      one = ((one[0]-1)%imax, one[1])
      matrix[one] = 1
      return movement
    if string == "up":
      matrix[one] = 0
      one = (one[0], (one[1]-1)%jmax)
      matrix[one] = 1
      return movement
    if string == "down":
      matrix[one] = 0
      one = (one[0], (one[1]+1)%jmax)
      matrix[one] = 1
      return movement
    else:
      return [[matrix[(i,j)]for i in range(imax)] for j in range(jmax)]
  return movement

