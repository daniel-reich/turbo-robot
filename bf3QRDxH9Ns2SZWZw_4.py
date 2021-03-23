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

from collections import defaultdict, deque
​
def matrix(grid): 
  adjacents = defaultdict(lambda: "0")
  matrice = defaultdict(lambda: "0")
  shifts = {"+": [(1,0),(-1,0),(0,1),(0,-1)],
            "x": [(1,1),(1,-1),(-1,1),(-1,-1)]}
  num = 0
  for i, line in enumerate(grid):
    for j, char in enumerate(line):
        matrice[(i,j)]= char
        if char != "0":
          num += 1
          adjacents[(i,j)] = [(i+shift[0],j+shift[1]) 
                              for shift in shifts[char]
                              ]
  print (num)
  return adjacents, matrice, num
​
def bfs(graph, root, matrice): 
  visited, queue = set(), deque([root])
  while queue: 
    vertex = queue.popleft()
    for neighbour in graph[vertex]:
      if neighbour not in visited and matrice[neighbour] != "0": 
        visited.add(neighbour) 
        queue.append(neighbour)
  print (len(visited))
  return visited
  
def all_explode(grid):
  adjacents, matrice, num = matrix(grid)
  if len(bfs(adjacents,(0,0), matrice)) == num:
    return True
  else:
    return False

