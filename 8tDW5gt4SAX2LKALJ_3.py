"""


This is a sequel to [Chain Reaction (Part
#1)](https://edabit.com/challenge/bf3QRDxH9Ns2SZWZw), with the same setup, but
a different flavor.

As in the previous part, you will be given a rectangular array representing a
"map" with three types of spaces:

  * "+" bombs: when activated, their explosion activates any bombs directly above, below, left, or right of the "+" bomb.
  * "x" bombs: when activated, their explosion activates any bombs placed in any of the four diagonal directions next to the "x" bomb.
  * Empty spaces "0".

The goal is simple: **given a map, return the minimum number of bombs that
need to be set off for all bombs to be destroyed by the chain reaction**.

Let's look at some examples:

    [
      ["+", "+", "+", "0", "+", "+", "+"],
      ["+", "+", "+", "0", "0", "+", "+"]
    ]

For the map above, the answer is `2`; to explode all bombs you just need to
set off one "+" bomb in the right cluster and one in the left cluster.

    [
      ["x", "0", "x"],
      ["x", "x", "x"]
    ]

For the map above, the answer is `3`; clearly setting off the three bottom "x"
bombs is enough, and no less than three bombs suffice.

    [
      ["x", "x", "x", "0", "x"],
      ["x", "x", "x", "x", "x"],
      ["x", "x", "x", "0", "x"]
    ]

For the map above, the answer is `3`; setting off the three rightmost bombs in
the middle row will do the trick.

### Examples

    min_bombs_needed([
      ["+", "+", "+", "0", "+", "+", "+"],
      ["+", "+", "+", "0", "0", "+", "+"]
    ]) ➞ 2
    
    min_bombs_needed([
      ["x", "0", "x"],
      ["x", "x", "x"]
    ]) ➞ 3
    
    min_bombs_needed([
      ["x", "x", "x", "0", "x"],
      ["x", "x", "x", "x", "x"],
      ["x", "x", "x", "0", "x"]
    ]) ➞ 3

### Notes

  * Note that both "+" and "x" bombs have an "explosion range" of 1.
  * To limit the difficulty, in this challenge each map will have only "+" or only "x" bombs. The more challenging case of maps with both "+" and "x" bombs will be [part 3](https://edabit.com/challenge/LLieA2XafALFxXRT5)!
  * Figuring out what to do is half the fun, but if you'd prefer to just handle the coding, a hint on to how to attack this challenge can be found in the comments.

"""

from itertools import combinations
def min_bombs_needed(grid):
  bombs = []
  grid = tuple([tuple(i) for i in grid])
  for y in range(len(grid)):
    for x in range(len(grid[y])):
      if grid[y][x] in '+x':
        bombs.append([y,x])
  for l in range(1,len(bombs)+1):
    for c in combinations(bombs,l):
      if explode([list(i) for i in grid],c):
        return l
    
def explode(lst,bombs):
  for i in bombs:
    y,x = i
    if lst[y][x]=='+':
      lst = tbomb(lst,y,x)
    elif lst[y][x]=='x':
      lst = xbomb(lst,y,x)
  return all([all([i=='0' for i in j]) for j in lst])
​
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
  if x<len(lst[y])-1:
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
    if x<len(lst[y])-1:
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
    if x<len(lst[y])-1:
      if lst[y+1][x+1]=='+':
        lst = tbomb(lst,y+1,x+1)
      elif lst[y+1][x+1]=='x':
        lst = xbomb(lst,y+1,x+1)  
  return lst

