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
  ret = [0]*len(board)
  for i in range(len(ret)):
    ret[i]=[0]*len(board[0])
  for x in range(len(ret)):
    for y in range(len(ret[x])):
      if board[x][y]==1:
        ret[x][y] = 9
      else:
        temp = 0
        if x>0:
          temp+=board[x-1][y]
          if y>0: temp+=board[x-1][y-1]
          if y<len(ret[x])-1: temp+=board[x-1][y+1]
        if x<len(ret)-1:
          temp+=board[x+1][y]
          if y>0: temp+=board[x+1][y-1]
          if y<len(ret[x])-1: temp+=board[x+1][y+1]
        if y>0: temp+=board[x][y-1]
        if y<len(ret[x])-1: temp+=board[x][y+1]
        ret[x][y] = temp
  return ret

