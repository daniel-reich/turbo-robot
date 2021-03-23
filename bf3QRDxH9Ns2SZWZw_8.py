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
    counter = 0
    allex = True
    for i, row in enumerate(grid):
        if not allex:
            break
        for j, cell in enumerate(row):
            if cell == '+' or cell == 'x':
                counter += 1
                expl = ch_plus(grid, i, j) or ch_x(grid, i, j)
                if not expl and counter > 1:
                    allex = False
                    break
    return allex
​
​
def slg(l, i, j):
    if i < 0 or j < 0:
        return False
    try:
        return l[i][j]
    except IndexError:
        pass
    return False
​
​
def ch_plus(grid, i, j):
    up = slg(grid, i-1, j)
    down = slg(grid, i+1, j)
    left = slg(grid, i, j-1)
    right = slg(grid, i, j+1)
    if up == '+' or down == '+' or left == '+' or right == '+':
        return True
    else:
        return False
​
​
def ch_x(grid, i, j):
    left_up = slg(grid, i-1, j-1)
    right_up = slg(grid, i-1, j+1)
    left_down = slg(grid, i+1, j-1)
    right_down = slg(grid, i+1, j+1)
    if left_up == 'x' or right_up == 'x' or left_down == 'x' or right_down == 'x':
        return True
    else:
        return False

