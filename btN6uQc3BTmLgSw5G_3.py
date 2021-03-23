"""


In this challenge, transform a string into a spiral contained inside a regular
square matrix. To build the matrix, you are given the dimension of its side:

  * If the side of the matrix is odd, the spiral starting point will be the exact center of the matrix.
  * If the side of the matrix is even, the spiral starting point will be placed in the lower columns half of the lower rows half.

    # "x" represents the matrix center
    
    side = 3 (odd)
    matrix = [
      [" ", " ", " "],
      [" ", "x", " "],
      [" ", " ", " "]
    ]
    
    side = 4 (even)
    matrix = [
      [" ", " ", " ", " "],
      [" ", "x", " ", " "],
      [" ", " ", " ", " "],
      [" ", " ", " ", " "],
    ]

The length of the string has to match exactly the number of cells inside the
matrix:

  * If the string length is greater than the number of cells, you have to cut off the unnecessary characters.
  * If the string length is lower than the number of cells, you have to add a series of `"+"` to the end of the string until its length match the number of cells.

    side = 3 (9 cells)
    string = "EDABITTEROUS"
    # You'll need only "EDABITTER", while "OUS" is discarded.
    string = "EDABITTER"
    
    side = 4 (16 cells)
    string = "EDABITTEROUS"
    # You'll need all the string plus 4 "+" to match the cells.
    string = "EDABITTEROUS++++"

Starting from the center that you found, you have to fill a regular square
matrix `side * side` placing the characters of the given string `str`,
following a clockwise spiral pattern (first move to the right).

    side = 3 (odd)
    string = "EDABITTEROUS"
    matrix = [
      ["T", "E", "R"],
      ["T", "E", "D"],
      ["I", "B", "A"]
    ]
    
    side = 4 (even)
    string = "EDABITTEROUS"
    matrix = [
      ["T", "E", "R", "O"],
      ["T", "E", "D", "U"],
      ["I", "B", "A", "S"],
      ["+", "+", "+", "+"],
    ]

### Examples

    spiral_matrix(2, "DOG") ➞ [
      ["D", "O"],
      ["+", "G"]
    ]
    
    spiral_matrix(3, "COPYRIGHTS") ➞ [
      ["G", "H", "T"],
      ["I", "C", "O"],
      ["R", "Y", "P"]
    ]
    
    spiral_matrix(4, "SUPERLUMBERJACK") ➞ [
      ["U", "M", "B", "E"],
      ["L", "S", "U", "R"],
      ["R", "E", "P", "J"],
      ["+", "K", "C", "A"]
    ]

### Notes

  * Remember, the first move from the center is to the right, and then you proceed clockwise and concentrically.
  * As given `side`, you can expect any valid value greater than `1`.

"""

def spiral_matrix(n, s):
    res = [[''] * n for _ in range(n)]
    if len(s) < n * n:
        s += '+' * (n * n - len(s))
    rc = cc = n // 2 if n % 2 else (n - 1) // 2
    res[rc][cc], res[rc][cc + 1] = s[0], s[1]
    res[rc + 1][cc + 1], res[rc + 1][cc] = s[2], s[3]
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    idx_dirs, r, c = 2, rc + 1, cc
    for i in range(4, n * n):
        if idx_dirs == 0:
            if not res[r + 1][c]:
                idx_dirs = (idx_dirs + 1) % 4
        elif idx_dirs == 1:
            if not res[r][c - 1]:
                idx_dirs = (idx_dirs + 1) % 4
        elif idx_dirs == 2:
            if not res[r - 1][c]:
                idx_dirs = (idx_dirs + 1) % 4
        elif idx_dirs == 3:
            if not res[r][c + 1]:
                idx_dirs = (idx_dirs + 1) % 4
        r, c = r + dirs[idx_dirs][0], c + dirs[idx_dirs][1]
        res[r][c] = s[i]
    return res

