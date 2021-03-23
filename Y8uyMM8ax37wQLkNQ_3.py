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
  m = [[j for j in range(1,n+1)],[3*n - 2 - j for j in range(0,n)]]
  if n == 2:
    return m
  else:
    for i in range(1,n-1):
      m.insert(i,([0 for j in range(0,n-2)]))
      m[i].insert(0,4*(n-1)-i+1)
      m[i].append(n+i)
  
  m[0][0] = 1
  r,c = 1,0
  while m[r][c] < n * n:
    while m[r][c+1] == 0:
      c += 1
      m[r][c] = m[r][c-1] + 1 
    while m[r+1][c] == 0:
      r += 1
      m[r][c] = m[r-1][c] + 1 
    while m[r][c-1] == 0:
      c -= 1
      m[r][c] = m[r][c+1] + 1 
    while m[r-1][c] == 0:
      r -= 1
      m[r][c] = m[r+1][c] + 1 
  return m

