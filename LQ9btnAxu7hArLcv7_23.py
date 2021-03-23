"""


Write a function that diagonally orders numbers in a `n x n` matrix, depending
on which of the four corners you originate from: upper-left (`ul`), upper-
right (`ur`), lower-left (`ll`), lower-right (`lr`).

### Examples

    diagonalize(3, "ul") ➞ [
      [0, 1, 2],
      [1, 2, 3],
      [2, 3, 4]
    ]
    
    diagonalize(4, "ur") ➞ [
      [3, 2, 1, 0],
      [4, 3, 2, 1],
      [5, 4, 3, 2],
      [6, 5, 4, 3]
    ]
    
    diagonalize(3, "ll") ➞ [
      [2, 3, 4],
      [1, 2, 3],
      [0, 1, 2]
    ]
    
    diagonalize(5, "lr") ➞ [
      [8, 7, 6, 5, 4],
      [7, 6, 5, 4, 3],
      [6, 5, 4, 3, 2],
      [5, 4, 3, 2, 1],
      [4, 3, 2, 1, 0]
    ]

### Notes

N/A

"""

def diagonalize(n, d):
  mat = []
  for i in range(n):
    mat.append([])
    for j in range(n):
      mat[i].append(0)
  if d == 'ul':
    startX = 0
    startY = 0
    dirX = 1
    dirY = 1
  elif d == 'ur':
    startX = n - 1
    startY = 0
    dirX = -1
    dirY = 1
  elif d == 'll':
    startX = 0
    startY = n - 1
    dirX = 1
    dirY = -1
  elif d == 'lr':
    startX = n - 1
    startY = n - 1
    dirX = -1
    dirY = -1
  num = 0
  YPos = startY
  for i in range(n):
    XPos = startX
    tnum = num
    for j in range(n):
      mat[YPos][XPos] = tnum
      tnum += 1
      XPos += dirX
    YPos += dirY
    num += 1
  return mat

