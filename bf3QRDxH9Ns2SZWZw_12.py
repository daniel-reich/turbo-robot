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
    bombs = [(i,j) for i,x in enumerate(grid) for j, y in enumerate(x) if y in '+x']
    moves,movesd = [(0,1),(1,0),(-1,0),(0,-1)], [(-1,-1),(1,1),(-1,1),(1,-1)]
    stack, visited = [(0,0)], [(0,0)]
​
    while stack:
        i,j = stack.pop()
        move = moves if grid[i][j] == '+' else movesd
        neighbors = [(i+a,j+b)for a, b in move if 0 <= i+a < len(grid) and 0<=j+b <len(grid[0])]
​
        for m,n in neighbors:
            if (m,n) not in visited and grid[m][n] in '+x':
                visited.append((m,n))
                stack.append((m,n))
    return len(bombs) == len(visited)

