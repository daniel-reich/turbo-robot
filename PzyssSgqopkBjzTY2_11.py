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

def can_exit(lst, row=0, col=0):
    row_last = len(lst) - 1
    col_last = len(lst[0]) - 1
    cell_value = lst[row][col]
    wall = 1 #blocked cell
    visited = 3 #visited cell 
    if row == row_last and \
       col == col_last and \
       cell_value != wall:
        return True
    elif cell_value == wall or cell_value == visited: 
        return False
    lst[row][col] = 3 # mark as visited 
    #explore neighbours 
    if (row < row_last and can_exit(lst, row+1, col))\
        or (row > 0 and can_exit(lst, row - 1, col))\
        or (col < col_last and can_exit(lst, row, col + 1))\
        or (col > 0 and can_exit(lst, row, col - 1)):
        return True
    return False

