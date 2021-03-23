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

def Inpath(path,i,j):
  for pt in path:
    if pt == (i,j):
      return True
  path.append((i,j))
  return False
​
def getNext(path,lst,i,j):
  #move right,down,up ,left (i,j) = (x,y)
  #m,n = maxX,MaxY
  m = len(lst) - 1
  n = len(lst[0]) - 1 
  exitPt = (m,n)
  if exitPt == (i,j):
    return True
  
  returnBool =  False
  if (m >= i+1) and lst[i+1][j] == 0 and not Inpath(path,i+1,j):
    returnBool = returnBool or getNext(path,lst,i+1,j)
  
  if (n >= j+1) and lst[i][j+1] == 0 and not Inpath(path,i,j+1):
    returnBool = returnBool or getNext(path,lst,i,j+1)
  
  if (j-1 >= 0) and lst[i][j-1] == 0 and not Inpath(path,i,j-1):
    returnBool = returnBool or  getNext(path,lst,i,j-1)
  
  if (i-1 >= 0) and lst[i-1][j] == 0 and not Inpath(path,i-1,j):
    returnBool = returnBool or getNext(path,lst,i-1,j)
  
  return returnBool
​
def can_exit(lst):
  path = []
  path.append((0,0))
  return getNext(path,lst,0,0)

