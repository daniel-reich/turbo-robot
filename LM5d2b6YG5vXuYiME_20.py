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

def can_enter_cave(screen):
    # rotate the map so that it is traversed top to bottom (makes it easier to think).
    screen = [list(elem) for elem  in list(zip(*screen))]
    # Assume nowhere is reachable:
    is_reachable = [[0 for elem in row] for row in screen]
​
    for iteration in range(len(screen) - 2):
        for row in range(len(screen)):
            for col in range(len(screen[row])):
                if row == 0:  # First row test
                    if screen[row][col] == 0:
                        is_reachable[row][col] = 1
                else:  # All other rows
                    if screen[row][col] == 0 and is_reachable[row - 1][col] == 1:  # Look back
                        is_reachable[row][col] = 1
                    elif row < len(screen) - 1 and screen[row][col] == 0 and is_reachable[row + 1][col] == 1:  # Look forwards
                        is_reachable[row][col] = 1
                    for col2 in range(len(screen[row])):
                        try:
                            if screen[row][col2] == 0 and is_reachable[row][col2 - 1] == 1:
                                is_reachable[row][col2] = 1
                            elif screen[row][col2] == 0 and is_reachable[row][col2 + 1] == 1:
                                is_reachable[row][col2] = 1
                        except IndexError:
                            pass
​
    return any(is_reachable[-1])

