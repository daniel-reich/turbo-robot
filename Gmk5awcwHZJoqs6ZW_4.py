"""


An **island is a region of contiguous ones**. A contiguous one is a `1` that
is touched by at least one other `1`, either **horizontally** , **vertically**
or **diagonally**. Given a piece of the map, represented by a 2-D list, create
a function that returns the area of the largest island.

To illustrate, if we were given the following piece of the map, we should
return `4`.

    [
      [0, 0, 0],
      [0, 1, 1],
      [0, 1, 1]
    ]

Our function should yield `2` for the map below:

    [
      [1, 0, 0],
      [0, 0, 1],
      [0, 0, 1]
    ]

Our function should yield `4` for the map below: :

    [
      [1, 0, 0],
      [0, 1, 1],
      [0, 0, 1]
    ]

### Examples

    largest_island([
      [1, 0, 0], 
      [0, 0, 0], 
      [0, 0, 1]
    ])
    
    ➞ 1
    
    largest_island([
      [1, 1, 0], 
      [0, 1, 1], 
      [0, 0, 1]
    ])
    
    ➞ 5
    
    largest_island([
      [1, 0, 0], 
      [1, 0, 0], 
      [1, 0, 1]
    ])
    
    ➞ 3

### Notes

  * Maps can be any `m x n` dimension.
  * Maps will always have at least 1 element. `m >= 1` and `n >= 1`.

"""

class UndirectedGraph():
    def __init__(self, grid):
        N = len(grid)
        M = len(grid[0])
        self.edges = {}
        self.nodes = []
        for row in range(N):
            for col in range(M):
                if grid[row][col] == 1:
                    self.AddNode((row, col))
                    for row2 in range(max(0, row - 1), min(N, row + 2)):
                        for col2 in range(max(0, col - 1), min(N, col + 2)):
                            if 0 <= row2 < N and 0 <= col2 < M and (row != row2 or col != col2) and grid[row2][col2] == 1:
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
def largest_island(lst):
    G = UndirectedGraph(lst)
    CCs = G.GetConnectedComponents()
    return max([len(CC) for CC in CCs])

