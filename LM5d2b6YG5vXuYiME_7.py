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

def can_enter_cave(listString):
    listA = listString
    A = listA[0]
    B = listA[1]
    C = listA[2]  
    D = listA[3]
    if len(listA) == 5:
        E = listA[4]     
    a = False
    b = 1
    for i in range(len(A) - 1):
        if len(listA) == 5:
            if A[i] + A[b] == 0 or B[i] + B[b] == 0 or C[i] + C[b] == 0 or D[i] + D[b] == 0 or E[i] + E[b] == 0:
                a = True
            else:
                a = False
                break
            b += 1
        else:
            if A[i] + A[b] == 0 or B[i] + B[b] == 0 or C[i] + C[b] == 0 or D[i] + D[b] == 0:
                a = True
            else:
                a = False
                break
            b += 1    
    return a

