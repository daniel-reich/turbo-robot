"""


You are playing a video game. Your screen can be represented as a 2D array,
where `0`s represent **walkeable areas** and `1`s represent **unwalkeable
areas**. You are currently searching for the entrance to a cave that is
located on the right side of the screen. Your character starts anywhere in the
leftmost column.

Create a function that determines if you can enter the cave. You can only move
left, right, up, or down (not allowed to move diagonally).

To illustrate:

    [
      [0, 0, 1, 1, 1, 0, 0, 0],
      [0, 0, 0, 0, 1, 0, 0, 0],
      [0, 0, 1, 0, 0, 0, 0, 0],
      [0, 0, 1, 1, 1, 1, 1, 0]
    ]

You found the entrance! Function should output `True`.

    [
      [0, 0, 0, 1, 0, 0, 0, 0],
      [0, 0, 0, 1, 1, 0, 0, 0],
      [0, 0, 0, 0, 1, 1, 0, 0],
      [0, 0, 0, 1, 1, 1, 1, 0]
    ]

Nope, keep looking. Function should output `False`.

### Examples

    can_enter_cave([
      [0, 1, 1, 1, 0, 1, 1, 0],
      [0, 0, 1, 1, 0, 0, 0, 0],
      [0, 0, 0, 0, 1, 1, 1, 0],
      [0, 1, 1, 1, 1, 1, 1, 0]
    ]) ➞ False
    
    # You cannot walk diagonally!
    can_enter_cave([
      [0, 1, 1, 1, 0, 1, 1, 0],
      [0, 0, 1, 1, 0, 0, 0, 0],
      [1, 0, 0, 0, 0, 1, 0, 0],
      [1, 1, 1, 1, 1, 1, 1, 0]
    ]) ➞ True
    can_enter_cave([
      [0, 1, 1, 1, 1, 1, 1, 0],
      [0, 0, 0, 0, 1, 0, 0, 0],
      [0, 0, 1, 1, 1, 1, 1, 0],
      [0, 1, 1, 0, 0, 1, 1, 0]
    ]) ➞ False

### Notes

  * You are seeing the game screen from a birds-eye view. 
  * Another way of thinking about it: You can enter the cave if you can move from the **left** side of the screen to the **right** side by only walking up, down or right. 
  * The entrance is not necessarily the first square, you may have to search for it in the left hand column.

"""

def can_enter_cave(x):
  higth = len(x)
  width = len(x[0])
  i = 0
  j = 0
​
  # find start point
  while x[i][0] != 0:
    i += 1
​
  def check_vertically(x, start, stop, step, jj, horizontal_step):
    for ii in range(start, stop, step):
      if x[ii][jj]:
        return start, jj, False
      if x[ii][jj+horizontal_step] == 0:
        return ii, jj+horizontal_step, True
    return start, jj, False
​
  while j < width-1:
    # Check Down and Forward
    i, j, found_way = check_vertically(x, i, higth, 1, j, +1)
    if not found_way:
      # Check Up and Forward
      i, j, found_way = check_vertically(x, i - 1, -1, -1, j, +1)
    if not found_way:
      # Check Down and Backward
      i, j, found_way = check_vertically(x, i, higth, 1, j, -1)
    if not found_way:
      # Check Up and Backward
      i, j, found_way = check_vertically(x, i - 1, -1, -1, j, -1)
    if not found_way:
      return False
  return True

