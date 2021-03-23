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
    rows, cols, len_word = len(grid), len(grid[0]), len(word)
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == word[0]:
                idx_chain = [(r, c)]
                for idx_w in range(1, len_word):
                    row, col = idx_chain[-1]
                    letter_found = False
                    for tpl in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                        candidate = (row + tpl[0], col + tpl[1])
                        if (0 <= candidate[0] < rows and
                            0 <= candidate[1] < cols and
                            candidate not in idx_chain and
                            grid[candidate[0]][candidate[1]] == word[idx_w]):
                            idx_chain.append(candidate)
                            letter_found = True
                            break
                    if not letter_found:
                        break
                if len(idx_chain) == len_word:
                    return idx_chain
    return 'Not present'

