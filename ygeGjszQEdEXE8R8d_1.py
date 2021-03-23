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

res=[]
def move(mat):
  global res
  res = mat[:]
  def F(direction):
    global res
    if direction=='stop':return res
    elif direction=='up':
      res=res[1:]+[res[0]]
      return F
    elif direction=='down':
      res=[res[-1]]+res[:-1]
      return F
    elif direction=='left':
      for i in range(len(res)):
        res[i]=res[i][1:]+[res[i][0]]
      return F
    elif direction=='right':
      for i in range(len(res)):
        res[i]=[res[i][-1]]+res[i][:-1]
      return F
  return F

