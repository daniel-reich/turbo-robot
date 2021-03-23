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
  for i in range(len(lst)):
    for j in range(len(lst[0])):
      count=0
      if (lst[i][j]!="#"):
        for k in range(i-1,i+2):
          for l in range(j-1,j+2):
            if (k>-1 and k<len(lst) and l>-1 and l<len(lst[0]) and lst[k][l]=="#"):
              count+=1
        lst[i][j]=str(count)
  return lst

