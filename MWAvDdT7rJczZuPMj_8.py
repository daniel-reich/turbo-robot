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

from copy import deepcopy
​
def count_word(table, word):
    cnt = 0
    ans = deepcopy(table)
    H, W = len(table), len(table[0])
    for i in range(H):
        table[i] = ''.join(table[i])
    ttable = [''.join(list(i)) for i in zip(*table)]
    L = len(word)
    # find horizontal words:
    for r in range(H):
        row = table[r]
        for idx in range(W - L + 1):
            if word in [row[idx:idx+L], row[idx:idx+L][::-1]]:
                cnt += 1
                for c in range(idx, idx + L):
                    ans[r][c] = ans[r][c].lower()
    # find vertical words:
    for r in range(W):
        row = ttable[r]
        for idx in range(H - L + 1):
            if word in [row[idx:idx+L], row[idx:idx+L][::-1]]:
                cnt += 1
                for c in range(idx, idx + L):
                    ans[c][r] = ans[c][r].lower()
    # find diagonal words, upper left to lower right:
    for row in range(H):
        for col in range(W):
            for dr, dc in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
                r, c = row, col
                diag = ""
                while 0 <= r < H and 0 <= c < W and len(diag) < L:
                    diag += table[r][c]
                    r += dr
                    c += dc
                if word == diag:
                    cnt += 1
                    r, c = row, col
                    for i in range(L):
                        ans[r][c] = ans[r][c].lower()
                        r += dr
                        c += dc
    return (cnt, ans)

