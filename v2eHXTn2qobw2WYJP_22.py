"""


Create a function that takes a list representation of a Minesweeper board, and
returns another board where the value of each cell is the amount of its
neighbouring mines.

### Examples

The input may look like this:

    [
      [0, 1, 0, 0],
      [0, 0, 1, 0],
      [0, 1, 0, 1],
      [1, 1, 0, 0]
    ]

The `0` represents an **empty space** . The `1` represents a **mine**.

You will have to replace each **mine** with a `9` and each **empty space**
with the number of adjacent mines, the output will look like this:

    [
      [1, 9, 2, 1],
      [2, 3, 9, 2],
      [3, 9, 4, 9],
      [9, 9, 3, 1]
    ]

### Notes

  * Since in the output the numbers `0-8` are used to determine the amount of adjacent mines, the number `9` will be used to identify the mines instead.
  * A wikipedia page explaining how Minesweeper works is available in the **Resources** tab.

"""

def minesweeper_numbers(board):
    board2= [[i for i in j] for j in board]
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 1:
                board2[row][col] = 9
            else:
                board2[row][col] = check(board,row,col)
    return board2
​
def check(board,row,col):
    around = [1,0,-1]
    count = 0
    for i in around:
        for j in around:
            if 0 <= row + i < len(board) and 0 <= col + j < len(board[0]):
                if board[row + i][col + j] == 1:
                    count += 1  
    return count

