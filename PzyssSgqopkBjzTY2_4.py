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
  m = len(lst)
  n = len(lst[0])
  if lst[0][0] != 0 or lst[m-1][n-1] != 0:
    return False
  else:
    coord = (0,0)
    saveCoords = []
    while coord != (n-1, m-1):
      x = coord[0]
      y = coord[1]
      lst[y][x] = 7
      option, newCoords = find_options(lst, coord)
      if option == 0:
        if saveCoords == []:
          return False
        else:
          coord = saveCoords[0]
          saveCoords = saveCoords[1:]
      if option == 1:
        coord = newCoords[0]
      if option > 1:
        saveCoords.append((x, y) * (option-1))
        coord = newCoords[0]
    return True
​
​
def find_options(lst, coord):
  x = coord[0]
  y = coord[1]
  option = 0
  
  newCoords = []
  
  if x+1 < len(lst[0]):
    if lst[y][x+1] == 0:
      option += 1
      newCoords.append((x+1, y))
  if y+1 < len(lst):
    if lst[y+1][x] == 0:
      option += 1
      newCoords.append((x, y+1))
  if y-1 >= 0:
    if lst[y-1][x] == 0:
      option += 1
      newCoords.append((x, y-1))
  if x-1 >= 0:
    if lst[y][x-1] == 0:
      option += 1
      newCoords.append((x-1, y))
  
  return option, newCoords

