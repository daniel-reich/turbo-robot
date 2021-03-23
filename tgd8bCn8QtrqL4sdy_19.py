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
    m=[(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
    for a in range(3):
        for b in range(3):
            if grid[a][b]=='?':
                k=0
                for i in range(8):
                    c,d=a+m[i][0],b+m[i][1]
                    if 3>c>-1 and 3>d>-1:
                        if grid[c][d]=='#':
                            k+=1
                grid[a][b]=str(k)
    return grid

