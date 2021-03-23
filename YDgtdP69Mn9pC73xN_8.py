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
  x = [
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
      [0,0,0,0,0],
  ]
  a = []
  b = []
  for i in range(len(lst)):
    for j in range(len(lst[i])):
      if lst[i][j] == '#':
        x[i][j] = -100
        try:
          index1 = i
          index2 = j-1
          if index1 >=0 and index2 >=0:
            x[i][j-1] += 1
        except:
          pass
        try:
          index1 = i
          index2 = j+1
          if index1 >= 0 and index2 >=0:
            x[i][j+1] += 1
        except:
          pass
        try:
          index1 = i-1
          index2 = j
          if index1 >=0 and index2 >=0:
            x[i-1][j] += 1
        except:
          pass
        try:
          index1 = i+1
          index2 = j
          if index1 >=0and index2>=0:
            x[i+1][j] += 1
        except:
          pass
        try:
          index1 = i-1
          index2 = j-1
          if index1 >=0and index2>=0:
            x[i-1][j-1] +=1
        except:
          pass
        try:
          index1 = i-1
          index2 = j+1
          if index1 >=0and index2>=0:
            x[i-1][j+1] += 1
        except:
          pass
        try:
          index1 = i+1
          index2 = j-1
          if index1 >=0and index2>=0:
            x[i+1][j-1] += 1
        except:
          pass
        try:
          index1 = i+1
          index2 = j+1
          if index1 >=0and index2>=0:
            x[i+1][j+1] += 1
        except:
          pass
          
  for k in x:
    a = []
    for l in k:
      if l<0:
        a.append('#')
      else:
        a.append(str(l))
    b.append(a)
  return b

