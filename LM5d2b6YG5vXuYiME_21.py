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

def can_enter_cave(lst):
    rows = len(lst)
    cols = len(lst[0])
    
    start_col = 0
    end_col = cols - 1
    
    steps = [[1,0],[-1,0],[0,1],[0,-1]] 
    
    found = False
    for i in range(rows):
        stack = []
        if lst[i][start_col] == 0:
            stack.append([i,start_col])
        while len(stack) != 0:
            current = stack[-1]
            adj_available = False
            for step in steps:
                x = current[0] + step[0]
                y = current[1] + step[1]
                if (x >=0 and x <rows) and (y >=0 and y<cols):
                    if lst[x][y] == 0:
                        if y == end_col:
                            return True
                        lst[x][y] = 2
                        adj_available = True
                        
                        stack.append([x,y])
                        break
            if not adj_available:
                stack.pop()
                
    return False

