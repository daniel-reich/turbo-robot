"""


Given a 2D array of mines, replace the **question mark** with the number of
mines that immediately surround it. This includes the diagonals, meaning it is
possible for it to be surrounded by **8 mines maximum**.

The key is as follows:

  * An empty space: **"-"**
  * A mine: **"#"**
  * Number showing number of mines surrounding it: **"?"**

###  Examples

    minesweeper([
      ["-", "#", "-"],
      ["-", "?", "-"],
      ["-", "-", "-"]
    ]) ➞ [
      ["-", "#", "-"],
      ["-", "1", "-"],
      ["-", "-", "-"]
    ]
    
    minesweeper([
      ["-", "#", "-"],
      ["#", "-", "?"],
      ["#", "#", "-"]
    ]) ➞ [
      ["-", "#", "-"],
      ["#", "-", "2"],
      ["#", "#", "-"]
    ]
    
    minesweeper([
      ["-", "#", "#"],
      ["?", "#", ""],
      ["#", "?", "-"]
    ]) ➞ [
      ["-", "#", "#"],
      ["3", "#", ""],
      ["#", "2", "-"]
    ]
    
    minesweeper([
      ["-", "-", "#"],
      ["?", "-", "-"],
      ["-", "-", "-"]
    ]) ➞ [
      ["-", "-", "#"],
      ["0", "-", "-"],
      ["-", "-", "-"]
    ]

### Notes

  * You will only be given **3x3** grids.
  * The question mark is not limited to the centre (there may be multiple question marks).

"""

def minesweeper(grid):
    '''
    Returns updated grid to show how many mines surround any '?' cells, as
    per the instructions.
    '''
    def mines(grid, i, j):
        '''
        Returns a count of mines surrounding grid[i][j] where a mine is
        identified as a '#'
        '''
        count = 0
        locs = ((i-1,j-1), (i-1,j), (i-1,j+1),(i,j-1),
                (i,j+1), (i+1,j-1), (i+1,j), (i+1,j+1)) # possible neighbours
​
        for r, c in locs:
            if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                if grid[r][c] == '#':
                    count += 1
​
        return str(count)
​
    return [[mines(grid,i,j) if grid[i][j] == '?' else grid[i][j] \
             for j in range(len(grid[0]))] for i in range(len(grid))]

