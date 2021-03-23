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
    pad = ['0' for i in range(len(grid[0])+2)]
    grid = [pad] + [['0'] + row + ['0'] for row in grid] + [pad]
    explode(grid,1,1)
    total = sum([1 for i in grid if 'x' in i or '+' in i])
    return total == 0
​
def explode(grid,row,col):
    diag = [(row+1,col+1),(row+1,col-1),(row-1,col+1),(row-1,col-1)]
    sides = [(row+1,col),(row-1,col),(row,col-1),(row,col+1)]
    if grid[row][col] == '+':
        grid[row][col] = '0'
        for i in sides:
            if grid[i[0]][i[1]] != '0': 
                explode(grid,i[0],i[1])
    else:
        grid[row][col] = '0'
        for i in diag:
            if grid[i[0]][i[1]] != '0': 
                explode(grid,i[0],i[1])      
    return None

