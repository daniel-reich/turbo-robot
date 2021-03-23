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

# turns = 0,1,-1
# heights =   0,1,-1
def num_grid (lst):
  num_mines   = 0 
  turns       = [0,1,-1]
  heights     = [0,1,-1]
  mem_turns   = [0,1,-1]
  mem_heights = [0,1,-1]
  for y in range  (len (lst)):
    if y-1 < 0: 
      # too_high = True
      heights.remove (-1)
​
    elif y + 1 > len (lst)-1:
      #too_low = True
      heights.remove (1)
    for x in range ( len (lst[0])):
      if x-1 <  0 :
        #too_left  = True
        turns.remove(-1)
      elif x+1 > len (lst[0])-1:
        #too_right = True
        turns.remove (1)
      if lst[y][x] == '-':
        for i in turns :
          for z in heights:
            if lst[y+z][x+i] == '#':
​
              num_mines+= 1
        lst [y][x] = str (num_mines) 
      num_mines = 0 
​
       
      turns = mem_turns[:]
    heights = mem_heights[:]
​
    
  for i in lst:
    print (i)
  return lst

