"""


In this challenge you will be given a rectangular list representing a "map"
with three types of spaces:

  *  **"+" bombs:** When activated, their explosion activates any bombs directly above, below, left, or right of the "+" bomb.
  *  **"x" bombs:** When activated, their explosion activates any bombs placed in any of the four diagonal directions next to the "x" bomb.
  * Empty spaces "0".

Consider the grid:

    [
      ["+", "+", "0", "x", "x", "+", "0"],
      ["0", "+", "+", "x", "0", "+", "x"]
    ]

If the top left "+" bomb explodes, the resulting chain reaction will blow up
bombs in the order given by the numbers below:

    [
      ["1", "2", "0", "x", "6", "8", "0"],
      ["0", "3", "4", "5", "0", "7", "8"]
    ]

Note that there are two 8's since two of the bombs explode at the same time.
Also, note that one of the "x" bombs in the top row does not explode.

Write a function that determines if the chain reaction started when the _top
left bomb_ explodes destroys all bombs or not.

### Examples

    all_explode([
      ["+", "+", "+", "+", "+", "+", "x"]
    ]) ➞ True
    
    all_explode([
      ["+", "+", "+", "+", "+", "0", "x"]
    ]) ➞ False
    
    all_explode([
      ["+", "+", "0", "x", "x", "+", "0"],
      ["0", "+", "+", "x", "0", "+", "x"]
    ]) ➞ False
    
    all_explode([
      ["x", "0", "0"],
      ["0", "0", "0"],
      ["0", "0", "x"]
    ]) ➞ False
    
    all_explode([
      ["x", "0", "x"],
      ["0", "x", "0"],
      ["x", "0", "x"]
    ]) ➞ True

### Notes

  * Both "+" and "x" bombs have an "explosion range" of 1.
  * Part #2 can be [found here](https://edabit.com/challenge/8tDW5gt4SAX2LKALJ).

"""

def all_explode(grid):
  bomb_directions = {
    '+': [
      (-1, 0),
      (1, 0),
      (0, 1),
      (0, -1)
    ],
    'x': [
      (-1, -1),
      (-1, 1),
      (1, -1),
      (1, 1)
    ],
    '0': []
  }
  grid_width, grid_height = len(grid[0]), len(grid)
  
  explode_queue = [(0, 0)]
  while explode_queue:
    exploded_bomb = explode_queue.pop(0)
    row, column = exploded_bomb
    bomb_kind = grid[row][column]
    grid[row][column] = '0'
    for direction in bomb_directions[bomb_kind]:
      row_change, column_change = direction
      new_row = row + row_change
      new_column = column + column_change
      if 0 <= new_row < grid_height and 0 <= new_column < grid_width:
        explode_queue.append((new_row, new_column))
​
  all_exploded = len([elem
    for subgrid in grid
    for elem in subgrid
    if elem in ['+', 'x']
  ]) == 0
  return all_exploded

