"""


Create a function that takes in parameter `n` and generates an `n x n` (where
`n` is odd) **concentric rug**.

The center of a concentric rug is `0`, and the rug "fans-out", as show in the
examples below.

### Examples

    generate_rug(1) ➞ [
      [0]
    ]
    
    generate_rug(3) ➞ [
      [1, 1, 1],
      [1, 0, 1],
      [1, 1, 1]
    ]
    
    generate_rug(5) ➞ [
      [2, 2, 2, 2, 2],
      [2, 1, 1, 1, 2],
      [2, 1, 0, 1, 2],
      [2, 1, 1, 1, 2],
      [2, 2, 2, 2, 2]
    ]
    
    generate_rug(7) ➞ [
      [3, 3, 3, 3, 3, 3, 3],
      [3, 2, 2, 2, 2, 2, 3],
      [3, 2, 1, 1, 1, 2, 3],
      [3, 2, 1, 0, 1, 2, 3],
      [3, 2, 1, 1, 1, 2, 3],
      [3, 2, 2, 2, 2, 2, 3],
      [3, 3, 3, 3, 3, 3, 3]
    ]

### Notes

  * `n >= 0`.
  * Always increment by 1 each "layer" outwards you travel.

"""

def distance(k, outer):
  return abs(outer - k)
​
def entry(k,i,j):
  return max(distance(k,i),distance(k,j))
​
def generate_rug(n):
  board = []
  k = n // 2
  for i in range(0,n):
    board.append([])
  for row in board:
    for i in range(0,n):
      row.append(0)
  for i in range(0,n):
    for j in range(0,n):
      board[i][j] = entry(k,i,j)
  return board

