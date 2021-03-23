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
​
    def j_pos(grid, row, col, x, y, cnt, pos):
        if y+1 < col and cnt <= len(word)-1 and grid[x][y+1].upper() == word[0+cnt]:
            pos.append((x, y+1))
            j_pos(grid, row, col, x, y+1, cnt+1, pos)
        if len(pos) == len(word):
            for i in pos:
                grid[i[0]][i[1]] = grid[i[0]][i[1]].lower()
    def j_neg(grid, row, col, x, y, cnt, pos):
        if y-1 >= 0 and cnt <= len(word)-1 and grid[x][y-1].upper() == word[0+cnt]:
            pos.append((x, y-1))
            j_neg(grid, row, col, x, y-1, cnt+1, pos)
        if len(pos) == len(word):
            for i in pos:
                grid[i[0]][i[1]] = grid[i[0]][i[1]].lower()
    def i_pos(grid, row, col, x, y, cnt, pos):
        if x+1 < row and cnt <= len(word)-1 and grid[x+1][y].upper() == word[0+cnt]:
            pos.append((x+1, y))
            i_pos(grid, row, col, x+1, y, cnt+1, pos)
        if len(pos) == len(word):
            for i in pos:
                grid[i[0]][i[1]] = grid[i[0]][i[1]].lower()
    def i_neg(grid, row, col, x, y, cnt, pos):
        if x-1 >= 0 and cnt <= len(word)-1 and grid[x-1][y].upper() == word[0+cnt]:
            pos.append((x-1, y))
            i_neg(grid, row, col, x-1, y, cnt+1, pos)
        if len(pos) == len(word):
            for i in pos:
                grid[i[0]][i[1]] = grid[i[0]][i[1]].lower()
    def du_pos(grid, row, col, x, y, cnt, pos):
        if x-1 >= 0 and y+1 < col and cnt <= len(word)-1 and grid[x-1][y+1].upper() == word[0+cnt]:
            pos.append((x-1, y+1))
            du_pos(grid, row, col, x-1, y+1, cnt+1, pos)
        if len(pos) == len(word):
            for i in pos:
                grid[i[0]][i[1]] = grid[i[0]][i[1]].lower()
    def du_neg(grid, row, col, x, y, cnt, pos):
        if x-1 >= 0 and y-1 >= 0 and cnt <= len(word)-1 and grid[x-1][y-1].upper() == word[0+cnt]:
            pos.append((x-1, y-1))
            du_neg(grid, row, col, x-1, y-1, cnt+1, pos)
        if len(pos) == len(word):
            for i in pos:
                grid[i[0]][i[1]] = grid[i[0]][i[1]].lower()
    def dd_pos(grid, row, col, x, y, cnt, pos):
        if x+1 < row and y+1 < col and cnt <= len(word)-1 and grid[x+1][y+1].upper() == word[0+cnt]:
            pos.append((x+1, y+1))
            dd_pos(grid, row, col, x+1, y+1, cnt+1, pos)
        if len(pos) == len(word):
            for i in pos:
                grid[i[0]][i[1]] = grid[i[0]][i[1]].lower()
    def dd_neg(grid, row, col, x, y, cnt, pos):
        if x+1 < row and y-1 >= 0 and cnt <= len(word)-1 and grid[x+1][y-1].upper() == word[0+cnt]:
            pos.append((x+1, y-1))
            dd_neg(grid, row, col, x+1, y-1, cnt+1, pos)
        if len(pos) == len(word):
            for i in pos:
                grid[i[0]][i[1]] = grid[i[0]][i[1]].lower()
​
    row = len(grid)
    col = len(grid[0])
    pos = []
    res = 0
​
    for i in range(row):
        for j in range(col):
            if grid[i][j].upper() == word[0]:
                pos.append((i, j))
                j_pos(grid, row, col, i, j, 1, pos)
                if len(pos) == len(word): res += 1
                pos = []
                pos.append((i, j))
                j_neg(grid, row, col, i, j, 1, pos)
                if len(pos) == len(word): res += 1
                pos = []
                pos.append((i, j))
                i_pos(grid, row, col, i, j, 1, pos)
                if len(pos) == len(word): res += 1
                pos = []
                pos.append((i, j))
                i_neg(grid, row, col, i, j, 1, pos)
                if len(pos) == len(word): res += 1
                pos = []
                pos.append((i, j))
                du_pos(grid, row, col, i, j, 1, pos)
                if len(pos) == len(word): res += 1
                pos = []
                pos.append((i, j))
                du_neg(grid, row, col, i, j, 1, pos)
                if len(pos) == len(word): res += 1
                pos = []
                pos.append((i, j))
                dd_pos(grid, row, col, i, j, 1, pos)
                if len(pos) == len(word): res += 1
                pos = []
                pos.append((i, j))
                dd_neg(grid, row, col, i, j, 1, pos)
                if len(pos) == len(word): res += 1
                pos = []
​
    return((res, grid))

