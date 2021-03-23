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

def verify(dire,grid, act, new, i, lin, col):
    for j in dire:
        nr, nc = i[0] + j[0], i[1] + j[1]
        if 0 <= nr <= lin and 0 <= nc <= col and (nr, nc) not in act:
            if grid[nr][nc] != '0': new.append((nr, nc))
    return new
​
def all_explode(grid):
    bombs, lin, col, new, act = dict(), len(grid)-1, len(grid[0])-1, [(0,0)], {(0,0):True}
    pls, tim = [(-1,0),(1,0),(0,-1),(0,1)], [(-1,-1),(-1,1),(1,-1),(1,1)]
    for  i in range(lin+1):
        for j in range(col+1):
            if grid[i][j] != '0': bombs[(i,j)] = True
    while new:
        tests = new.copy(); new=[]
        for i in tests:
            if grid[i[0]][i[1]] == '+': new = verify(pls,grid, act, new, i, lin, col)
            else: new = verify(tim,grid, act, new, i, lin, col)
        for i in new: act[i] = True
    return True if act.keys() == bombs.keys() else False

