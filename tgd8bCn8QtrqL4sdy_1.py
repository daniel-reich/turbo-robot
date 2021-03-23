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
    index = get_index(grid)
    for i in index:
        to_check =(coor(i))
        to_check.remove(i)
        result = sum([1 for y, x in to_check if grid[y][x] == "#"])
        grid[i[0]][i[1]] = str(result)
    return grid
    
def get_index(grid): 
    index = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "?":
                add = [y, x]
                index.append(add)
    return index
    
def coor(index):
    to_check = []
    for i in range(-1, 2):
        for j in range(-1, 2): 
            if -1 < (i + index[0]) < 3 and -1 < (j + index[1]) < 3:
                add = [i + index[0], j + index[1]]
                to_check.append(add)
    return to_check

