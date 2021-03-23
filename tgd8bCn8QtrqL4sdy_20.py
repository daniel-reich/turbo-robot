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
  field = grid
  maxx = len(grid) - 1
  for i in range(len(field)) :
    for j in range(len(field[i])) :
​
​
      if field[i][j] == '?' :
​
​
        bomb_counter = 0
        for X_cor_rel in range(-1,2) : 
          for Y_cor_rel in range(-1,2) : 
            X_cor = X_cor_rel + i
            Y_cor = Y_cor_rel + j
​
            if X_cor >= 0 and Y_cor >= 0 and X_cor <= maxx and Y_cor <= maxx :
              if field[X_cor][Y_cor] == '#' :
​
                bomb_counter += 1
​
        field[i][j] = str(bomb_counter)
  return field

