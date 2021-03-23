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

from collections import defaultdict
​
def trace_word_path(word, grid):
    global matrix
    global steps
    matrix = defaultdict(lambda: " ")
    steps = [(-1,0),(0,-1),(0,1),(1,0)]
​
    cells = {(i,j) : char for i, line in enumerate(grid) for j, char in enumerate(line)}
    imax = max([coord[0] for coord in cells.keys()])
    jmax = max([coord[1] for coord in cells.keys()])
    for coord in cells.keys():
        matrix[coord] = cells[coord]  
    for start in [coord for coord, val in matrix.items() if val == word[0]]:
        chemin = [start]
        res = next_letter(chemin, word[1:])
        if res == False:
            chemin = chemin[:-1]
        else:
            return res
    return "Not present" 
​
def next_letter(chemin, word):
    global matrix
    global steps
    print (chemin, word)
    if word == "":
        return chemin
    start = chemin[-1]
    for step in steps:
        coord = (start[0]+step[0], start[1]+step[1])
        if matrix[coord] == word[0] and coord not in chemin:
            chemin.append(coord)
            res = next_letter(chemin, word[1:])
            if res == False:
                chemin = chemin[:-1]
            else:
                return res
    return False
​
​
print(trace_word_path("UKULELE", [
  ['N', 'H', 'B', 'W'], 
  ['E', 'X', 'A', 'D'], 
  ['L', 'A', 'U', 'U'], 
  ['E', 'L', 'U', 'K']
]))
print([(0, 0), (1, 0), (2, 0), (2, 1), (1, 1), (0, 1), (0, 2)])

