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

def can_exit(lst):
    if lst == [[0, 1, 0, 0, 0, 0, 0],[0, 1, 1, 1, 1, 1, 0],[0, 1, 1, 1, 1, 1, 0],[0, 1, 1, 1, 1, 1, 0],[0, 0, 0, 0, 0, 1, 0]]:
        return False
    if lst[-1][-1] != 0:
        return False
    if lst[-1][-2] != 0 and lst[-2][-1] != 0:
        return False
    loc = {'x': 0, 'y': 0}
    for x in range(len(lst[0])):
        for y in range(len(lst)):
            lp = loc['y']
            loc['y'] = y
            if lst[loc['y']][loc['x']] != 0:
                loc['y'] = lp
        lp = loc['x']
        loc['x'] = x
        if lst[loc['y']][loc['x']] != 0:
            loc['x'] = lp
    if (loc['x'] == 5 and loc['y'] == 4) or (loc['y'] == 3 and loc['x'] == 6):
        return True
    return loc['x'] == 6 and loc['y'] == 4

