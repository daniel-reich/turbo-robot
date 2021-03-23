"""


A grid of letters may contain a word hidden somewhere within it. The letters
of the word may be traced from the starting letter by moving a single letter
at a time, up, down, left or right. For example, suppose we are looking for
the word BISCUIT in this grid:

    [
      ["B","I","T","R"],
      ["I","U","A","S"],
      ["S","C","V","W"],
      ["D","O","N","E"]
    ]

The word starts in the top left corner, continues downwards for 2 more
letters, then the letter to the right followed by 2 letters moving upwards,
the final letter at the right of the penultimate one.

Write a function which takes in a target word and a grid of letters and
returns a list of tuples, each tuple being the row and column of the
corresponding letter in the grid (numbered from 0). If the word cannot be
found, output the string "Not present".

### Examples

    trace_word_path("BISCUIT", [
      ["B", "I", "T", "R"],
      ["I", "U", "A", "S"],
      ["S", "C", "V", "W"],
      ["D", "O", "N", "E"]
    ]) ➞ [(0, 0), (1, 0), (2, 0), (2, 1), (1, 1), (0, 1), (0, 2)]
    
    trace_word_path("HELPFUL", [
      ["L","I","T","R"],
      ["U","U","A","S"],
      ["L","U","P","O"],
      ["E","F","E","H"]
    ]) ➞ "Not present"

### Notes

  * The target word will never be longer than the grid of letters.
  * Target word and the letters grid will be in upper case.

"""

def trace_word_path(word, grid):
  x, y = len(grid), len(grid[0])
  target = len(word)
​
  for row in range(x):
    for col in range(y):
      if grid[row][col] == word[0]:
        indices = get_index(word, word[1:], grid, x, y, row, col, [(row, col)], target)
        if len(indices) == target:
          return indices
  return 'Not present'
​
def get_index(word, start, grid, x, y, row, col, indices, target):
  if len(indices) == target:
    return indices
  moves = [(1,0),(0,1),(-1,0),(0,-1)]
  neighbors = [(row+i,col+j) for i, j in moves if 0 <= row+i < x and 0 <= col+j < y]
  neighbors = [(i,j) for i,j in neighbors if grid[i][j] == start[0]]
  for a, b in neighbors:
    if (a, b) not in indices:
      n_indices = indices + [(a, b)]
      if len(n_indices) == target:
        return n_indices
      indices_r = get_index(word, start[1:], grid, x, y, a, b, n_indices, target)
      if len(indices_r) == target:
        return indices_r
  return indices

