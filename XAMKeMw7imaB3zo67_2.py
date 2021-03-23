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

def dfs(word, s, grid, H, W, row, col, chain):
    if len(chain) == len(word):
        return chain
    for [row2, col2] in [[row - 1, col], [row + 1, col], [row, col + 1], [row, col - 1]]:
        if 0 <= row2 < H and 0 <= col2 < W and grid[row2][col2] == s[0] and \
           (row2, col2) not in chain:
            new_chain = chain[:]
            new_chain.append((row2, col2))
            if len(new_chain) == len(word):
                return new_chain
            chain2 = dfs(word, s[1:], grid, H, W, row2, col2, new_chain)
            if len(chain2) == len(word):
                return chain2
    return chain
​
def trace_word_path(word, grid):
    H, W = len(grid), len(grid[0])
    for row in range(H):
        for col in range(W):
            if grid[row][col] == word[0]:
                chain = dfs(word, word[1:], grid, H, W, row, col, [(row, col)])
                if len(chain) == len(word):
                    return chain
    return 'Not present'

