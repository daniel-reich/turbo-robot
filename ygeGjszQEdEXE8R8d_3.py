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
    matt = [[c for c in row] for row in mat]
    rows, cols = len(matt), len(matt[0])
​
    def f(txt):
        if txt == 'stop':
            return matt
        rr, cc = 0, 0
        for r_idx, row in enumerate(matt):
            if 1 in row:
                rr = r_idx
                cc = row.index(1)
                break
        new_r, new_c = rr, cc
        if txt == 'up':
            new_r = (rr - 1) % rows
        elif txt == 'down':
            new_r = (rr + 1) % rows
        elif txt == 'left':
            new_c = (cc - 1) % cols
        elif txt == 'right':
            new_c = (cc + 1) % cols
        matt[rr][cc] = 0
        matt[new_r][new_c] = 1
        return f
    return f

