"""


Write a function that accepts an integer `n` and returns an `n * n` spiral
matrix.

### Examples

    matrix(2) ➞ [
      [1, 2],
      [4, 3]
    ]
    
    matrix(3) ➞ [
      [1, 2, 3],
      [8, 9, 4],
      [7, 6, 5]
    ]
    
    matrix(4) ➞ [
      [1,  2,  3,  4],
      [12, 13, 14, 5],
      [11, 16, 15, 6],
      [10,  9,  8, 7]
    ]

### Notes

In the examples, traverse the matrix in the clock-wise direction to observe
the spiral pattern.

"""

def matrix(n):
  base = [[0]*n for _ in range(n)]
  dirs = [[0,1],[1,0],[0,-1],[-1,0]]
  x,y = 0,-1
  k = 0
  a,b = dirs[k]
  for i in range(1,n**2+1):
    if x+a>=n or y+b>=n or base[x+a][y+b]!=0:
      k+=1
      a,b = dirs[k%4]
    base[x+a][y+b] = i
    x+= a
    y+= b
  return base

