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

def lines(r, c, rows, cols, n):
    res = []
    if rows - r >= n:
        res.append([(r + i, c) for i in range(n)])
    if r >= n - 1:
        res.append([(r - i, c) for i in range(n)])
    if cols - c >= n:
        res.append([(r, c + i) for i in range(n)])
    if c >= n - 1:
        res.append([(r, c - i) for i in range(n)])
    if rows - r >= n and cols - c >= n:
        res.append([(r + i, c + i) for i in range(n)])
    if r >= n - 1 and c >= n - 1:
        res.append([(r - i, c - i) for i in range(n)])
    if rows - r >= n and c >= n - 1:
        res.append([(r + i, c - i) for i in range(n)])
    if r >= n - 1 and cols - c >= n:
        res.append([(r - i, c + i) for i in range(n)])
    return res
​
​
def count_word(grid, word):
    rows, cols, len_word, count = len(grid), len(grid[0]), len(word), 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c].upper() == word[0]:
                for line in lines(r, c, rows, cols, len_word):
                    tmp_word = ''.join(grid[tpl[0]][tpl[1]].upper()
                                       for tpl in line)
                    if tmp_word == word:
                        count += 1
                        for tpl in line:
                            grid[tpl[0]][tpl[1]] = grid[tpl[0]][tpl[1]].lower()
    return count, grid

