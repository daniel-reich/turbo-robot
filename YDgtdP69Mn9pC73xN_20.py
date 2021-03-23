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

import collections
​
def num_grid(grid):
    x_limit = len(grid[0])
    y_limit = len(grid)
    board = map_board(grid)
    for key in board.keys():
        if board[key]['mine'] == True:
            x, y = key
            for i in range(max(0, x-1), min(x+2, x_limit)):
                for j in range(max(0, y-1), min(y+2, y_limit)):
                    board[(i,j)]['count'] += 1
    return convert_board(board, x_limit, y_limit)
        
def map_board(grid):
    d = collections.defaultdict(dict)
    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            d[(x,y)]['count']=0
            if value == "#":
                d[(x,y)]['mine'] = True
            else:
                d[(x,y)]['mine'] = False
    return d
​
def convert_board(board, x_limit, y_limit):
    output = [[0 for x in range(x_limit)]
             for y in range(y_limit)]
    for key in board.keys():
        x, y = key
        if board[key]['mine'] == True:
            output[y][x] ='#'
        else:
            output[y][x] = str(board[key]['count'])
    return output

