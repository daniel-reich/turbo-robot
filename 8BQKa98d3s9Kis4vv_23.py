"""


Write a function that takes in three parameters: `r, c, i`, where:

  * `r` and `c` are the number of **rows** and **columns** to initialize a zero matrix.
  * `i` represents the **list of incrementing operations** (+1).

And returns the resulting matrix after applying all the increment operations.
Each increment operation will **add 1** to the rows or columns specified in
the **incrementing list**.

To illustrate:

    final(3, 3, ["2r", "2c", "1r", "0c"])
    
    # Initialize a 3 x 3 matrix of zeroes.
    
    [
      [0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]
    ]
    
    # Apply "2r" (increment index 2 row).
    
    [
      [0, 0, 0],
      [0, 0, 0],
      [1, 1, 1]
    ]
    
    # Apply "2c" (increment index 2 column).
    
    [
      [0, 0, 1],
      [0, 0, 1],
      [1, 1, 2]
    ]
    
    # Apply "1r" (increment index 1 row).
    
    [
      [0, 0, 1],
      [1, 1, 2],
      [1, 1, 2]
    ]
    
    # Apply "0c" (increment index 0 column).
    # This is the result you should return.
    
    [
      [1, 0, 1],
      [2, 1, 2],
      [2, 1, 2]
    ]

### Examples

    final(2, 2, ["0r", "0r", "0r", "1c"]) ➞ [
      [3, 4],
      [0, 1]
    ]
    
    final(2, 2, ["0c"]) ➞ [
      [1, 0],
      [1, 0]
    ]
    
    final(3, 3, ["1c", "2c", "2c", "3c", "3c", "3c"]) ➞ [
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3]
    ]
    
    final(3, 3, []) ➞ [
      [0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]
    ]

### Notes

  * The 2D matrix is 0-indexed.
  * The matrix created will have at least one row and one column.
  * All **increment operations** will be exactly `+1`.

"""

def final(r, c, i):
    M = [[0 for col in range(c)] for row in range(r)]
    col_inc, row_inc = {}, {}
    for inc in i:
        if inc[-1] == 'r':
            row = int(inc[:-1])
            row_inc[row] = row_inc.get(row, 0) + 1
        else:
            col = int(inc[:-1])
            col_inc[col] = col_inc.get(col, 0) + 1
    for row in row_inc:
        M[row] = [row_inc[row]] * c
    for col in col_inc:
        add = col_inc[col]
        for row in range(r):
            M[row][col] += add
    return M

