"""


Create a function which takes 2 parameters:

  * A matrix `mat` with `m` rows and `n` columns, containing data of any type.
  * An optional integer parameter `turns` giving the number of clockwise 90 degree rotations by which to transform the matrix (defaults to 1).

The function should return a new matrix with the elements rotated clockwise or
counter-clockwise by the number of turns given.

For positive integers: 1 turn = 90° clockwise, 2 turns = 180° clockwise, 3
turns = 270° clockwise, 4 turns = 360° clockwise, etc.

For negative integers: -1 turn = 90° counter-clockwise, -2 turns = 180°
counter-clockwise, -3 turns = 270° counter-clockwise, -4 turns = 360° counter-
clockwise, etc.

### Examples

    rotate_matrix([
      [1,  2,  3,  4],
      [5,  6,  7,  8],
      [9, 10, 11, 12]
    ]) ➞ [
      [ 9, 5, 1],
      [10, 6, 2],
      [11, 7, 3],
      [12, 8, 4]
    ]
    # A clockwise rotation.
    # Left to right columns become rows in bottom to top order.
    rotate_matrix([["+", "-"], ["*", "/"]], -1) ➞ [["-", "/"], ["+", "*"]]
    # A counter-clockwise rotation.
    # Right to left columns become rows in top to bottom order.
    rotate_matrix([[1, 2, 3], [4, 5, 6]], 4) ➞ [[1, 2, 3], [4, 5, 6]]
    # A 360° turn returns all elements to their original positions.

### Notes

  * All given matrices (2-dimensional lists) will have at least 1 row and at least 1 column.
  * Do not mutate the original matrix, the return value should be a new 2-dimensional list with values _copied_ from the original list.
  *  **Do not import any libraries** \- the challenge is to come up with your own solution.
  * Make sure your solution is efficient enough to cope with a large number of turns
  * You must provide a default value for the `turns` parameter.

"""

def rotate_matrix(mat, turns=1):
    m, n, turns = len(mat), len(mat[0]), turns%4
    if turns == 3:
        return [[mat[r][c] for r in range(m)] for c in range(n-1, -1, -1)]
    elif turns == 2:
        return [row[::-1] for row in mat[::-1]]
    elif turns == 1:
        return [[mat[r][c] for r in range(m-1, -1, -1)] for c in range(n)]
    else:
        return [row[::] for row in mat]

