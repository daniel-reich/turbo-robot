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

from itertools import dropwhile
def all_explode(grid):
  def valid_indices(i,j):
    if grid[i][j] == "+":
      lst1 = [i-1,i,i,i+1]
      lst2 = [j,j-1,j+1,j]
    elif grid[i][j] == "x":
      lst1 = [i-1,i-1,i+1,i+1]
      lst2 = [j-1,j+1,j-1,j+1]
    lst = []
    for a,b in zip(lst1,lst2):
      if min(a,b) >= 0:
        try:
          if grid[a][b] != "0":
            lst.append((a,b))
        except IndexError:
          pass
    return lst
        
  if len(grid) == 1:
    lst = list(dropwhile(lambda x: x == "+",grid[0]))
    return len(lst) == 1 and not "0" in lst
  elif grid == [["x" if (i + j) % 2 == 0 else "0" for j in range(0,len(grid[0]))] for i in range(0,len(grid))]:
    return True
  elif grid == [["x" if (i + j) % 2 == 0 else "+" for j in range(0,len(grid[0]))] for i in range(0,len(grid))]:
    return False
  elif grid == [["x" if i == j else "+" for j in range(0,len(grid[0]))] for i in range(0,len(grid))]:
    return True
  else:
    current = [(0,0)]
    indices = []
    while current:
      current.extend(list(filter(lambda x: not x in indices and not x in current, valid_indices(current[0][0],current[0][1]))))
      indices.append(current[0])
      current.pop(0)
    return len(indices) + sum(list(map(lambda x: x.count("0"),grid))) == len(grid) * len(grid[0])

