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

def get_neighbours(grid, i, j):
    '''
    Returns the addresses of the vertical / horizontal neighbours of the cell at
    grid row i, column jin (row, col) format.
    '''
    possible_neighbours = (
                           (i-1,j),(i+1,j),(i,j-1),(i,j+1)
                          )
    addresses = []   # corresponding positions in the grid
    height = len(grid)
    width = len(grid[0])
    for neighbour in possible_neighbours:
        row = neighbour[0]
        col = neighbour[1]
        if 0 <= row < height and 0 <= col < width:
            addresses.append((row, col))
    #print('neighbours for', (i,j), addresses)
    return addresses
​
def trace_path(word, grid, current, path):
    '''
    Tries to trace a path from current through grid, seeing if it can match the
    corresponding letters of word. If it succeeds, returns the path as a list
    of (row, col) tuples otherwise False
    '''
    i, j = current
    
    if grid[i][j] != word[0]:
        return False   # letters don't match, abort
        
    if len(word) == 1:
        return path  # found the path to the word    
​
    addresses = get_neighbours(grid, i, j)
    for k in range(len(addresses)):
        if addresses[k] not in path:
            result = trace_path(word[1:], grid, addresses[k], path + [addresses[k]])
            if result:
                return result
        
    return False
​
def trace_word_path(word, grid):
    '''
    Checks each location in turn until it finds the path for word, or does not
    find it at all. Returns the path in the former case, 'Not present' in the
    latter.
    '''
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            path = trace_path(word, grid, (i, j), [(i,j)])
            if path:
                return path
​
    return 'Not present'

