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

class UndirectedGraph():
    def __init__(self, grid):
        self.W = len(grid[0])
        self.H = len(grid)
        self.edges = {}
        self.nodes = []
        for row in range(self.H):
            for col in range(self.W):
                if grid[row][col] == '+':
                    self.AddNode((row, col))
                    for [row2, col2] in [[row-1, col], [row+1, col], [row, col-1], [row, col+1]]:
                        if 0 <= row2 < self.H and 0 <= col2 < self.W and grid[row2][col2] in ['+', 'x']:
                            self.AddEdge((row, col), (row2, col2))
                elif grid[row][col] == 'x':
                    self.AddNode((row, col))
                    for [row2, col2] in [[row-1, col-1], [row+1, col+1], [row-1, col+1], [row+1, col-1]]:
                        if 0 <= row2 < self.H and 0 <= col2 < self.W and grid[row2][col2] in ['+', 'x']:
                            self.AddEdge((row, col), (row2, col2))
        
    def AddNode(self, node):
        if node not in self.nodes:
            self.nodes.append(node)
        if node not in self.edges:
            self.edges[node] = []
​
    def GetNodes(self):
        return self.nodes
​
    def GetEdges(self):
        return self.edges
​
    def AddEdge(self, node1, node2):
        self.AddNode(node1)
        self.AddNode(node2)
        if node1 not in self.edges[node2]:
            self.edges[node2].append(node1)
        if node2 not in self.edges[node1]:
            self.edges[node1].append(node2)
​
    def Degree(self, node):
        return len(self.edges[node])
​
    def GetNeighbors(self, node):
        return self.edges.get(node, [])
            
    def GetPath(self, source, target):
        # find path by BFS:
        predecessor = {node: -1 for node in self.GetNodes()}
        predecessor[source] = 0
        visited = {node: False for node in self.GetNodes()}
        queue = [source]
        while len(queue) > 0:
            current = queue.pop(0)
            visited[current] = True
            for neighbor in self.GetNeighbors(current):
                if not visited[neighbor] and neighbor not in queue:
                    queue.append(neighbor)
                    predecessor[neighbor] = current
                if neighbor == target:
                    queue = []
                    break
        # build path from predecessor info:
        if predecessor[target] == -1:
            return []
        path = [target]
        while path[0] != source:
            path = [predecessor[path[0]]] + path[:]
        return path
​
    def GetConnectedComponents(self):
        # identify connected components by BFS
        nodes = self.GetNodes()[:]
        connected_components = []
        while len(nodes) > 0:
            queue = [nodes.pop()]
            component = [queue[0]]
            while len(queue) > 0:
                current = queue.pop(0)
                for neighbor in self.GetNeighbors(current):
                    if neighbor in nodes and neighbor not in queue:
                        queue.append(neighbor)
                        nodes.remove(neighbor)
                        component.append(neighbor)
            connected_components.append(component)
        return connected_components
​
def min_bombs_needed(grid):
    G = UndirectedGraph(grid)
    return len(G.GetConnectedComponents())

