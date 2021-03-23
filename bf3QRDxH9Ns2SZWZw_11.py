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

### I = ligne
### J = colonne
​
def all_explode(grid):
  nb_fin = 0
  for i in grid:
    for j in i:
      if j == "+" or j == "x":
        nb_fin +=1
  
  grid = explosion(grid, 0,0)
  verif = 0
  for i in grid:
    for j in i:
      if j == 1:
        verif +=1
  print(grid, nb_fin, verif)
  if verif == nb_fin:
    return True
  return False
​
​
def explosion(grid, i, j):
  if grid[i][j] == "+":
    grid[i][j] = 1
    grid = explosion_plus(grid,i,j)
  elif grid[i][j] == "x":
    grid[i][j] = 1
    grid = explosion_croix(grid,i,j)
  return grid
[[1, 1, '0', 'x', 1, '+', '0'],
 ['0', 1, 1, 1, '0', '+', 'x']]
def explosion_plus(grid, i, j):
  lignes = len(grid)
  colonnes = len(grid[0])
  if i > 0:
    grid = explosion(grid, i-1, j)
  if j > 0:
    grid = explosion(grid, i, j-1)
  if i < lignes-1:
    grid = explosion(grid, i+1, j)
  if j < colonnes-1:
    grid = explosion(grid, i, j+1)
  return grid 
​
def explosion_croix(grid, i, j):
  lignes = len(grid)
  colonnes = len(grid[0])
  if i > 0 and j > 0:
    grid = explosion(grid, i-1, j-1)
  if i > 0 and j < colonnes-1:
    grid = explosion(grid, i-1, j+1)
  if i < lignes-1 and j > 0 :
    grid = explosion(grid, i+1, j-1)
  if i < lignes-1 and j < colonnes-1:
    grid = explosion(grid, i+1, j+1)
  return grid

