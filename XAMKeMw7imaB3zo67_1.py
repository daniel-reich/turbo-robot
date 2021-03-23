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
  lr = len(grid)
  lc = len(grid[0])
  for r in range(lr):
    for c in range(lc):
      if grid[r][c] == word[0]:
        coords = trace_word_recurse(word[1:], grid, r, c, [])
        if coords != None and coords[-1] != "Not present":
          return coords
  return "Not present"
​
def trace_word_recurse(word, grid, r, c, coords):
  lr = len(grid)-1
  lc = len(grid[0])-1
  if not word:
    return coords + [(r,c)]
  if r > 0:
    if grid[r-1][c] == word[0] and (r-1, c) not in coords:
      possible_coords = trace_word_recurse(word[1:], grid, r-1, c, coords + [(r, c)])
      if possible_coords[-1] != "Not present":
        return possible_coords
  if r < lr:
    if grid[r+1][c] == word[0] and (r+1, c) not in coords:
      possible_coords = trace_word_recurse(word[1:], grid, r+1, c, coords + [(r, c)])
      if possible_coords[-1] != "Not present":
        return possible_coords
  if c > 0:
    if grid[r][c-1] == word[0] and (r, c-1) not in coords:
      possible_coords = trace_word_recurse(word[1:], grid, r, c-1, coords + [(r, c)])
      if possible_coords[-1] != "Not present":
        return possible_coords
  if c < lc:
    if grid[r][c+1] == word[0] and (r, c+1) not in coords:
      possible_coords = trace_word_recurse(word[1:], grid, r, c+1, coords + [(r, c)])
      if possible_coords[-1] != "Not present":
        return possible_coords
  return coords + ["Not present"]

