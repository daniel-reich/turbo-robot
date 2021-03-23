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
  global pos,d
  pos=[0,0]
  d=[0,1,0,1]
  c=len(x)*len(x[0])
  while pos[0]!=len(x[0])-1:
    c-=1
    if c==0:
      return False
    if d[3]==1:
      if x[pos[1]][pos[0]+1]==0:
        right()
        continue
    if d[0]==1:
      if x[pos[1]-1][pos[0]]==0:
        up()
        continue
    if d[1]==1:
      if x[pos[1]+1][pos[0]]==0:
        down()
        continue
    if d[2]==1:
      if x[pos[1]][pos[0]-1]==0:
        left()
        continue
    [down(),up(),right(),left()][p]
    d[p]=0
  return True
def up():
  global pos,d,p
  pos[1]-=1
  d=[1,0,1,1]
  p=0
  print("up")
def down():
  global pos,d,p
  pos[1]+=1
  d=[0,1,1,1]
  p=1
  print("down")
def left():
  global pos,d,p
  pos[0]-=1
  d=[1,1,1,0]
  p=2
  print("left")
def right():
  global pos,d,p
  pos[0]+=1
  d=[1,1,0,1]
  p=3
  print("right")

