"""


This challenge is based on the game Minesweeper.

Create a function that takes a grid of `#` and `-`, where each hash (#)
represents a mine and each dash (-) represents a mine-free spot. Return a list
where each dash is replaced by a digit indicating the number of mines
immediately adjacent to the spot (horizontally, vertically, and diagonally).

### Examples

    num_grid([
      ["-", "-", "-", "-", "-"],
      ["-", "-", "-", "-", "-"],
      ["-", "-", "#", "-", "-"],
      ["-", "-", "-", "-", "-"],
      ["-", "-", "-", "-", "-"]
    ]) ➞ [
      ["0", "0", "0", "0", "0"],
      ["0", "1", "1", "1", "0"],
      ["0", "1", "#", "1", "0"],
      ["0", "1", "1", "1", "0"],
      ["0", "0", "0", "0", "0"],
    ]
    
    num_grid([
      ["-", "-", "-", "-", "#"],
      ["-", "-", "-", "-", "-"],
      ["-", "-", "#", "-", "-"],
      ["-", "-", "-", "-", "-"],
      ["#", "-", "-", "-", "-"]
    ]) ➞ [
      ["0", "0", "0", "1", "#"],
      ["0", "1", "1", "2", "1"],
      ["0", "1", "#", "1", "0"],
      ["1", "2", "1", "1", "0"],
      ["#", "1", "0", "0", "0"]
    ]
    
    num_grid([
      ["-", "-", "-", "#", "#"],
      ["-", "#", "-", "-", "-"],
      ["-", "-", "#", "-", "-"],
      ["-", "#", "#", "-", "-"],
      ["-", "-", "-", "-", "-"]
    ]) ➞ [
      ["1", "1", "2", "#", "#"],
      ["1", "#", "3", "3", "2"],
      ["2", "4", "#", "2", "0"],
      ["1", "#", "#", "2", "0"],
      ["1", "2", "2", "1", "0"],
    ]

### Notes

N/A

"""

def num_grid(lst):
    height = len(lst)
    width = len(lst[0])
    print(height,width)
    for i in range(0,height):
        if len(lst[i]) != width:
            return
    for i in range(0,height):
        for j in range(0,width):
            if lst[i][j] == "-":
                lst[i][j] = 0
                if (i != height - 1) and (lst[i + 1][j] == "#"):
                    lst[i][j] += 1
                if (i != 0) and (lst[i - 1][j] == "#"):
                    lst[i][j] += 1
                if (j != width - 1) and (lst[i][j + 1] == "#"):
                    lst[i][j] += 1
                if (j != 0) and (lst[i][j - 1] == "#"):
                    lst[i][j] += 1
                if (j != 0) and (i != 0) and (lst[i - 1][j - 1] == "#"):
                    lst[i][j] += 1
                if (j != width - 1) and (i != height - 1) and (lst[i + 1][j + 1] == "#"):
                    lst[i][j] += 1            
                if (j != width - 1) and (i != 0) and (lst[i - 1][j + 1] == "#"):
                    lst[i][j] += 1                    
                if (j != 0) and (i != height - 1) and (lst[i + 1][j - 1] == "#"):
                    lst[i][j] += 1  
    for i in range(0,height):
        for j in range(0,width):
            lst[i][j] = str(lst[i][j])
    return(lst)

