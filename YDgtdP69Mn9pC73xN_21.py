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
  for y in range(len(lst)):
    for x in range(len(lst[y])):
      if lst[y][x] != "#":
        lst[y][x] = check_mines([y,x], lst)
  return lst
  
def check_mines(spot, lst):
  mines = 0
  mines += check_sides(spot,lst)
  mines += check_up_down(spot,lst)
  return str(mines)
​
def check_sides(spot,lst):
  mines = 0
  if spot[1] > 0 and lst[spot[0]][spot[1]-1] == '#':
    mines += 1
  if spot[1] < len(lst[0]) - 1 and lst[spot[0]][spot[1]+1] == '#':
    mines += 1
  return mines
  
def check_up_down(spot,lst):
  mines = 0
  if spot[0] > 0:
    if lst[spot[0]-1][spot[1]] == '#':
      mines += 1
    mines += check_sides([spot[0]-1,spot[1]],lst)
  if spot[0] < len(lst) - 1:
    if lst[spot[0]+1][spot[1]] == '#':
      mines += 1
    mines += check_sides([spot[0]+1,spot[1]],lst)
  return mines

