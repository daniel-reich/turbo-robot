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
  a = [list(range(i, i + n)) for i in range(n)]
  if d == 'ul':
    return a
  if d == 'ur':
    return [v[::-1] for v in a]
  if d == 'll':
    return a[::-1]
  if d == 'lr':
    return [v[::-1] for v in a[::-1]]

