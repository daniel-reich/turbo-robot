"""


Create a function that takes a 5x5 3D list and returns `True` if it has at
least one Bingo, and `False` if it doesn't.

### Examples

    bingo_check([
      [45, "x", 31, 74, 87],
      [64, "x", 47, 32, 90],
      [37, "x", 68, 83, 54],
      [67, "x", 98, 39, 44],
      [21, "x", 24, 30, 52]
    ]) ➞ True
    
    bingo_check([
      ["x", 43, 31, 74, 87],
      [64, "x", 47, 32, 90],
      [37, 65, "x", 83, 54],
      [67, 98, 39, "x", 44],
      [21, 59, 24, 30, "x"]
    ]) ➞ True
    
    bingo_check([
      ["x", "x", "x", "x", "x"],
      [64, 12, 47, 32, 90],
      [37, 16, 68, 83, 54],
      [67, 19, 98, 39, 44],
      [21, 75, 24, 30, 52]
    ]) ➞ True
    
    bingo_check([
      [45, "x", 31, 74, 87],
      [64, 78, 47, "x", 90],
      [37, "x", 68, 83, 54],
      [67, "x", 98, "x", 44],
      [21, "x", 24, 30, 52]
    ]) ➞ False

### Notes

Only check for diagnols, horizontals and verticals.

"""

def bingo_check(board):
    return row_check(board) or diag_check(board) or tf_check(board) 
    
def row_check(board):
    for row in board:
        check = 0
        for col in row:
            if col == 'x':
                check += 1
                if check == 5:
                    return True
    return False
​
def diag_check(board):
    check = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if row == col and board[row][col] == 'x':
                check += 1
    return check == 5
​
def tf_check(board):
    trans = [[],[],[],[],[]]
    flip = [[],[],[],[],[]]
    for row in range(len(board)):
        for col in range(len(board[row])):
            trans[col].append(board[row][col])
            flip[4-row].append(board[row][col])
    return row_check(trans) or diag_check(flip)

