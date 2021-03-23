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

def spiral_matrix(side, string):
    n = side**2
    if len(string) < n:
        string += '+' * (n - len(string))
    if len(string) > n:
        string = string[:n]
    S = [c for c in string]
    empty = ' '
    M = [[empty for _ in range(side)] for __ in range(side)]
    if side % 2 == 0:
        row, col = side // 2 - 1, side // 2 - 1
    else:
        row, col = side // 2, side // 2
    M[row][col] = S.pop(0)
    col += 1
    M[row][col] = S.pop(0)
    direction = 0       # directions: 0=right, 1=down, 2=left, 3=up
    while len(S) > 0:
        cur_dir = direction
        if cur_dir == 0:
            # currently moving right:
            if row < side - 1 and M[row+1][col] == empty:
                # turn right, i.e. go down:
                row += 1
                direction = 1
            else:
                # keep going right:
                col += 1
        elif cur_dir == 1:
            # currently moving down:
            if col > 0 and M[row][col-1] == empty:
                # turn right, i.e. go left:
                col -= 1
                direction = 2
            else:
                # keep going down:
                row += 1
        elif cur_dir == 2:
            # currently moving left:
            if row > 0 and M[row-1][col] == empty:
                # turn right, i.e. go up:
                row -= 1
                direction = 3
            else:
                # keep going right:
                col -= 1
        elif cur_dir == 3:
            # currently moving up:
            if col < side - 1 and M[row][col+1] == empty:
                # turn right, i.e. go right:
                col += 1
                direction = 0
            else:
                # keep going up:
                row -= 1
        M[row][col] = S.pop(0)
    return M

