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
  
  rows=len(grid)
  columns=len(grid[0])
  wlen=len(word)
  count=0
  locations=[]
  final_locations=[]
​
  for x in range(rows):
    for y in range(columns):
      if grid[x][y] == word[0]:
        locations.append([x,y])
​
  for item in locations:
    up, down, left, right = True, True, True, True
    if item[1]-wlen+1<0: left=False
    if item[1]+wlen>columns: right = False
    if item[0]-wlen+1<0: up=False
    if item[0]+wlen>rows: down=False
    if up or down or left or right:
      if up:
        for z in range(wlen):
          if grid[item[0]-z][item[1]]!=word[z]:
            break
          elif z==wlen-1:
            word_location=[item, [item[0]-z, item[1]]]
            final_locations.append(word_location)
      if down:
        for z in range(wlen):
          if grid[item[0]+z][item[1]]!=word[z]:
            break
          elif z==wlen-1:
            word_location=[item, [item[0]+z, item[1]]]
            final_locations.append(word_location)
      if right:
        for z in range(wlen):
          if grid[item[0]][item[1]+z]!=word[z]:
            break
          elif z==wlen-1:
            word_location=[item, [item[0], item[1]+z]]
            final_locations.append(word_location)
      if left:
        for z in range(wlen):
          if grid[item[0]][item[1]-z]!=word[z]:
            break
          elif z==wlen-1:
            word_location=[item, [item[0], item[1]-z]]
            final_locations.append(word_location)
      if up and left:
        for z in range(wlen):
          if grid[item[0]-z][item[1]-z]!=word[z]:
            break
          elif z==wlen-1:
            word_location=[item, [item[0]-z, item[1]-z]]
            final_locations.append(word_location)
      if up and right:            
        for z in range(wlen):                
          if grid[item[0]-z][item[1]+z]!=word[z]:
            break
          elif z==wlen-1:
            word_location=[item, [item[0]-z, item[1]+z]]
            final_locations.append(word_location)
      if down and left:
        for z in range(wlen):
          if grid[item[0]+z][item[1]-z]!=word[z]:
            break
          elif z==wlen-1:
            word_location=[item, [item[0]+z, item[1]-z]]
            final_locations.append(word_location)
      if down and right:
        for z in range(wlen):
          if grid[item[0]+z][item[1]+z]!=word[z]:
            break
          elif z==wlen-1:
            word_location=[item, [item[0]+z, item[1]+z]]
            final_locations.append(word_location)
​
  for item in final_locations:
    # down and right
    if item[1][0]-item[0][0]>0 and item[1][1]-item[0][1]>0:
      for x,y in zip(range(item[1][0]-item[0][0]+1),range(item[1][1]-item[0][1]+1)):
        grid[item[0][0]+x][item[0][1]+y]=grid[item[0][0]+x][item[0][1]+y].lower()
            # print(grid[item[0][0]+x][item[0][1]+y].lower())
​
    elif item[1][0]-item[0][0]>0 and item[0][1]-item[1][1]>0:
      for x,y in zip(range(item[1][0]-item[0][0]+1),range(item[0][1]-item[1][1]+1)):
        grid[item[0][0]+x][item[0][1]-y]=grid[item[0][0]+x][item[0][1]-y].lower()
            # print(grid[item[0][0]+x][item[0][1]-y].lower())
​
    elif item[0][0]-item[1][0]>0 and item[1][1]-item[0][1]>0:
      for x,y in zip(range(item[0][0]-item[1][0]+1),range(item[1][1]-item[0][1]+1)):
        grid[item[0][0]-x][item[0][1]+y]=grid[item[0][0]-x][item[0][1]+y].lower()
            # print(grid[item[0][0]-x][item[0][1]+y].lower())
​
    elif item[0][0]-item[1][0]>0 and item[0][1]-item[1][1]>0:
        # print(item[0][0])
      for x,y in zip(range(item[0][0]-item[1][0]+1),range(item[0][1]-item[1][1]+1)):
        grid[item[0][0]-x][item[0][1]-y]=grid[item[0][0]-x][item[0][1]-y].lower()
            # print(grid[item[0][0]-x][item[0][1]-y].lower())
            
    elif item[1][0]-item[0][0]>0:
      for x in range((item[1][0]-item[0][0])+1):
        grid[item[0][0]+x][item[0][1]]=grid[item[0][0]+x][item[0][1]].lower()
    elif item[0][0]-item[1][0]>0:
      for x in range((item[0][0]-item[1][0])+1):
            # print('hi')
        grid[item[0][0]-x][item[0][1]]=grid[item[0][0]-x][item[0][1]].lower()
    elif item[1][1]-item[0][1]>0:
      for y in range(item[1][1]-item[0][1]+1):
            # print('hi')
        grid[item[0][0]][item[0][1]+y]=grid[item[0][0]][item[0][1]+y].lower()
            # print(grid[item[0][0]][item[0][1]+y])
    elif item[0][1]-item[1][1]>0:
      for y in range(item[0][1]-item[1][1]+1):
            # print('hi')
        grid[item[0][0]][item[0][1]-y]=grid[item[0][0]][item[0][1]-y].lower()
            # print(grid[item[0][0]][item[0][1]+y])
​
  answer=(len(final_locations),grid)
  return(answer)

