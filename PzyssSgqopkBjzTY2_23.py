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
  mazeW = len(maze[0])
  mazeH = len(maze)
  mazeFL = []
  for i in range(mazeW + 2):
    mazeFL.append(1)
  bmaze = [mazeFL]
  for i in range(mazeH):
    bmaze.append([1] + maze[i] + [1])
  bmaze.append(mazeFL)
  exit = False
  start_pos = [1, 1]
  current_pos = [start_pos[:], 3, 1]
  exit_pos = [len(bmaze) - 2, len(bmaze[0]) - 2]
  w = 0
  startagain = 2
  while 1 == 1:
    w += 1
    #print(current_pos)
    if current_pos[0] == exit_pos:
      exit = True
      break
    if current_pos[0] == start_pos:
      if startagain == 0:
        break
      else:
        startagain -= 1
    paths = []
    paths = [[[current_pos[0][0] - 1, current_pos[0][1]], 0, 1], [[current_pos[0][0], current_pos[0][1] - 1], 1, 1], [[current_pos[0][0] + 1, current_pos[0][1]], 2, 1], [[current_pos[0][0], current_pos[0][1] + 1], 3, 1]]
    pathst = paths[:]
    ways = 0
    for i in range(len(paths)):
      if bmaze[paths[i][0][0]][paths[i][0][1]] == 0:
        paths[i][2] = 0
        ways += 1
    if ways == 0:
      break
    for i in range(3+current_pos[1], 7+current_pos[1]):
      if paths[i%4][2] == 0:
        current_pos = paths[i%4]
        break
  return exit

