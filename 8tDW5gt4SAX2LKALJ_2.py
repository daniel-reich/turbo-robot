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
  return adjacents, matrice, num
​
def bfs(graph, root, matrice): 
  visited, queue = set(), deque([root])
  visited.add(root)
  while queue: 
    vertex = queue.popleft()
    for neighbour in graph[vertex]:
      if neighbour not in visited and matrice[neighbour] != "0": 
        visited.add(neighbour) 
        queue.append(neighbour)
  return visited
  
def min_bombs_needed(grid):
  adjacents, matrice, num = matrix(grid)
  start = (0,0)
  visited = bfs(adjacents,start, matrice)
  counter = 1
  print (num, start, visited, counter)
  while len(visited) < num:
    start = [u for u in adjacents.keys() if u not in visited][0]
    visited = visited | bfs(adjacents,start, matrice)
    counter += 1
    print (num, start, visited, counter)
  return counter

