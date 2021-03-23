"""


A maze can be represented by a 2D matrix, where `0`s represent **walkeable**
areas, and `1`s represent walls. You start on the upper left corner and the
exit is on the most lower right cell.

Create a function that returns `true` if you can walk from one end of the maze
to the other. You can only move up, down, left and right. You **cannot move
diagonally**.

### Examples

    can_exit([
      [0, 1, 1, 1, 1, 1, 1],
      [0, 0, 1, 1, 0, 1, 1],
      [1, 0, 0, 0, 0, 1, 1],
      [1, 1, 1, 1, 0, 0, 1],
      [1, 1, 1, 1, 1, 0, 0]
    ]) ➞ true
    
    can_exit([
      [0, 1, 1, 1, 1, 1, 1],
      [0, 0, 1, 0, 0, 1, 1],
      [1, 0, 0, 0, 0, 1, 1],
      [1, 1, 0, 1, 0, 0, 1],
      [1, 1, 0, 0, 1, 1, 1]
    ]) ➞ false
    
    # This maze only has dead ends!
    
    can_exit([
      [0, 1, 1, 1, 1, 0, 0],
      [0, 0, 0, 0, 1, 0, 0],
      [1, 1, 1, 0, 0, 0, 0],
      [1, 1, 1, 1, 1, 1, 0],
      [1, 1, 1, 1, 1, 1, 1]
    ]) ➞ false
    
    # Exit only one block away, but unreachable!
    
    can_exit([
      [0, 1, 1, 1, 1, 0, 0],
      [0, 0, 0, 0, 1, 0, 0],
      [1, 1, 1, 0, 0, 0, 0],
      [1, 0, 0, 0, 1, 1, 0],
      [1, 1, 1, 1, 1, 1, 0]
    ]) ➞ true

### Notes

  * In a maze of size `m x n`, you enter at `[0, 0]` and exit at `[m-1, n-1]`.
  * There can be dead ends in a maze - one exit path is sufficient.

"""

def can_exit(maze):
  if maze[0][0]!=0:
    return False
  row = 0
  column = 0
  while True:
    if row==len(maze)-1 and column==len(maze[0])-1:
      return True
    maze[row][column] = 2
    if row > 0 and maze[row-1][column]==0:
      row -= 1
    elif column < len(maze[0])-1 and maze[row][column+1]==0:
      column += 1
    elif row < len(maze)-1 and maze[row+1][column]==0:
      row += 1
    elif column > 0 and maze[row][column-1]==0:
      column -= 1
    else:
      all_dead_ends = 1
      for i in range (len(maze)):
        if all_dead_ends==0:
          break
        for j in range (len(maze)):
          if maze[i][j]==2 and ((i > 0 and maze[i-1][j]==0) or (i < len(maze)-1 and maze[i+1][j]==0) or (j > 0 and maze[i][j-1]==0) or (j < len(maze[0])-1 and maze[i][j+1]==0)):
            row = i
            column = j
            all_dead_ends = 0
            break
      else:
        return False

