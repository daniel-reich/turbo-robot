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

import math
def can_exit(arr):
  rows=len(arr)
  col=len(arr[0])
  for j in range(1,col):
    arr[0][j]+=arr[0][j-1]
  for i in range(1,rows):
    arr[i][0]+=arr[i-1][0]
  
  for i in range(1,rows):
    for j in range(1,col):
      arr[i][j]+=min(arr[i-1][j],arr[i][j-1])
  
  return not arr[rows-1][col-1]

