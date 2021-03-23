"""


You are presented with a rectangular grid of capital letters. Within this grid
a target word occurs a number of times. The word may be positioned
horizontally left to right, right to left; vertically down to up or up to down
and diagonally left to right downwards, right to left downwards, right to left
upwards or left to right upwards.

Write a function which takes two parameters:

  1. The rectangular grid of upper case letters.
  2. The target word.

Your function should return a tuple (count, grid) where count is the total
number of occurrences of the target word and the grid is the input grid with
each occurrence of the target word in lower case.

### Examples

    count_word([
      ["I", "W", "I", "S", "H"],
      ["Z", "H", "S", "I", "W"],
      ["R", "S", "A", "D", "I"],
      ["Z", "I", "R", "E", "S"],
      ["J", "W", "K", "F", "H"]
    ], "WISH") ➞ (4, [
      ["I", "w", "i", "s", "h"],
      ["Z"h, "s", "i", "w"],
      ["R", "s", "A", "D", "I"],
      ["Z", "i", "R", "E", "S"],
      ["J", "w", "K", "F", "H"]
     ])
    
    count_word([
      ["M", "I", "W", "S", "W", "I", "I", "M"],
      ["W", "M", "I", "W", "W", "S", "M", "I"],
      ["I", "S", "S", "I", "M", "I", "S", "W"],
      ["S", "W", "I", "M", "W", "M", "W", "S"],
      ["I", "I", "W", "M", "I", "W", "I", "S"],
      ["I", "M", "I", "S", "M", "S", "M", "W"],
      ["W", "W", "S", "M", "W", "I", "S", "I"],
      ["S", "I", "M", "M", "I", "W", "S", "M"]
    ], "SWIM") ➞ (9, [
      ["m", "i", "w", "s", "W", "I", "I", "m"],
      ["W", "M", "I", "w", "W", "S", "M", "i"],
      ["I", "s", "S", "i", "M", "I", "s", "w"],
      ["s", "w", "i", "m", "W", "M", "w", "s"],
      ["I", "i", "W", "m", "I", "W", "i", "s"],
      ["I", "m", "i", "S", "M", "S", "m", "w"],
      ["W", "w", "S", "M", "W", "I", "S", "i"],
      ["s", "I", "M", "m", "i", "w", "s", "m"]
    ])

### Notes

Diagonals can be any diagonal the target word can fit in, not just the main
diagonal. The target word will not be a palindrome.

"""

def count_word(grid, word):
  count = 0
  for x in range(len(grid)):
    for y in range(len(grid[x])):
      temp = checkLeft(grid,word,x,y)
      if temp:
        count+=1
        for i in temp:
          grid[x][i] = grid[x][i].lower()
      temp = checkRight(grid,word,x,y)
      if temp:
        count+=1
        for i in temp:
          grid[x][i] = grid[x][i].lower()
      temp = checkUp(grid,word,x,y)
      if temp:
        count+=1
        for i in temp:
          grid[i][y] = grid[i][y].lower()
      temp = checkDown(grid,word,x,y)
      if temp:
        count+=1
        for i in temp:
          grid[i][y] = grid[i][y].lower()
      temp = checkDiagLeftUp(grid,word,x,y)
      if temp:
        count+=1
        for i in temp:
          grid[i[0]][i[1]] = grid[i[0]][i[1]].lower()
      temp = checkDiagLeftDown(grid,word,x,y)
      if temp:
        count+=1
        for i in temp:
          grid[i[0]][i[1]] = grid[i[0]][i[1]].lower()
      temp = checkDiagRightUp(grid,word,x,y)
      if temp:
        count+=1
        for i in temp:
          grid[i[0]][i[1]] = grid[i[0]][i[1]].lower()
      temp = checkDiagRightDown(grid,word,x,y)
      if temp:
        count+=1
        for i in temp:
          grid[i[0]][i[1]] = grid[i[0]][i[1]].lower()
  return (count,grid)
    
def checkLeft(grid,word,x,y):
  ret = []
  for i in range(len(word)):
    if y-i<0 or grid[x][y-i].upper()!=word[i]:
      return False
    else:
      ret.append(y-i)
  return ret
  
def checkRight(grid,word,x,y):
  ret = []
  for i in range(len(word)):
    if y+i>=len(grid[x]) or grid[x][y+i].upper()!=word[i]:
      return False
    else:
      ret.append(y+i)
  return ret
  
def checkUp(grid,word,x,y):
  ret = []
  for i in range(len(word)):
    if x-i<0 or grid[x-i][y].upper()!=word[i]:
      return False
    else:
      ret.append(x-i)
  return ret
  
def checkDown(grid,word,x,y):
  ret = []
  for i in range(len(word)):
    if x+i>=len(grid) or grid[x+i][y].upper()!=word[i]:
      return False
    else:
      ret.append(x+i)
  return ret
  
def checkDiagLeftUp(grid,word,x,y):
  ret = []
  for i in range(len(word)):
    if x-i<0 or y-i<0 or grid[x-i][y-i].upper()!=word[i]:
      return False
    else:
      ret.append([x-i,y-i])
  return ret
  
def checkDiagLeftDown(grid,word,x,y):
  ret = []
  for i in range(len(word)):
    if x+i>=len(grid) or y-i<0 or grid[x+i][y-i].upper()!=word[i]:
      return False
    else:
      ret.append([x+i,y-i])
  return ret
  
def checkDiagRightUp(grid,word,x,y):
  ret = []
  for i in range(len(word)):
    if x-i<0 or y+i>=len(grid[x]) or grid[x-i][y+i].upper()!=word[i]:
      return False
    else:
      ret.append([x-i,y+i])
  return ret
  
def checkDiagRightDown(grid,word,x,y):
  ret = []
  for i in range(len(word)):
    if x+i>=len(grid) or y+i>=len(grid[x]) or grid[x+i][y+i].upper()!=word[i]:
      return False
    else:
      ret.append([x+i,y+i])
  return ret

