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
  matrix = []
  for row in range(n):
    matrix.append([])
  if d[0] == 'u' or d[0] == 'U':
    for i in range(n):
      for number in range(n):
        matrix[i].append(i + number)
      if d[1] == 'r' or d[1] == 'R':
        matrix[i].reverse()
  elif d[0] == 'l' or d[0] == 'L':
    count = 0
    for i in range(n - 1, -1, -1):
      for number in range(n):
        matrix[i].append(number + count)
      if d[1] == 'r' or d[1] == 'R':
        matrix[i].reverse()
      count += 1
  return matrix

