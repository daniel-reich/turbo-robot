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
​
    def search(w, path):
        cr, cc = path[-1]
        # check all cells neighbouring last match in path
        for nr, nc in [(cr+1, cc), (cr, cc+1), (cr-1,cc), (cr, cc-1)]:
            if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc] == w[0] and not (nr, nc) in path:
                # found next letter @(nr, nc), append coordinates to path
                path.append((nr, nc))
                # last letter found return `done` flag
                if len(w) == 1: return True
                # recurse for remainder of word
                if search(w[1:], path): 
                    # successful search complete - return final path
                    return path
                else:
                    # unsuccessful search, remove last coord and try next candidate
                    path.pop();
        # no unvisited neighbours match next letter
        return False
    
    # find possible starting points
    for r,c in [(r, c) for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] == word[0]]:
        # recursive search for path to remeinder of word
        path = search(word[1:], [(r, c)])
        if path:
            return path
    return 'Not present'

