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
  if grid[0][0]=='+':
    grid = tbomb(grid,0,0)
  elif grid[0][0]=='x':
    grid = xbomb(grid,0,0)
  return all([all([j=='0' for j in i]) for i in grid])
  
def tbomb(lst,y,x):
  lst[y][x] = '0'
  if y>0:
    if lst[y-1][x]=='+':
      lst = tbomb(lst,y-1,x)
    elif lst[y-1][x]=='x':
      lst = xbomb(lst,y-1,x)
  if y<len(lst)-1:
    if lst[y+1][x]=='+':
      lst = tbomb(lst,y+1,x)
    elif lst[y+1][x]=='x':
      lst = xbomb(lst,y+1,x)
  if x>0:
    if lst[y][x-1]=='+':
      lst = tbomb(lst,y,x-1)
    elif lst[y][x-1]=='x':
      lst = xbomb(lst,y,x-1)
  if x<len(lst[0])-1:
    if lst[y][x+1]=='+':
      lst = tbomb(lst,y,x+1)
    elif lst[y][x+1]=='x':
      lst = xbomb(lst,y,x+1)
  return lst
  
def xbomb(lst,y,x):
  lst[y][x] = '0'
  if y>0:
    if x>0:
      if lst[y-1][x-1]=='+':
        lst = tbomb(lst,y-1,x-1)
      elif lst[y-1][x-1]=='x':
        lst = xbomb(lst,y-1,x-1)
    if x<len(lst[0])-1:
      if lst[y-1][x+1]=='+':
        lst = tbomb(lst,y-1,x+1)
      elif lst[y-1][x+1]=='x':
        lst = xbomb(lst,y-1,x+1)
  if y<len(lst)-1:
    if x>0:
      if lst[y+1][x-1]=='+':
        lst = tbomb(lst,y+1,x-1)
      elif lst[y+1][x-1]=='x':
        lst = xbomb(lst,y+1,x-1)
    if x<len(lst[0])-1:
      if lst[y+1][x+1]=='+':
        lst = tbomb(lst,y+1,x+1)
      elif lst[y+1][x+1]=='x':
        lst = xbomb(lst,y+1,x+1)
  return lst

