"""


Road systems can be imagined as a graph of intersections connected by lines.
The advantage of this is it makes it easier to find the shortest path between
any two intersections.

### Task

Write a function that takes as arguments:

  * A string representing JSON graph of the road system
  * The starting intersection (node)
  * The ending intersection (node)

And returns a dictionary containing information about the shortest path.

### Format of the road graph

The road graph follows the JSON graph specification linked in the Resources
tab. As an example, this is what one road graph could look like (in JSON):

    {
      "graph": {
        "directed": false,
        "nodes": [
          { "id": 0 },
          { "id": 1 },
          { "id": 2 },
           { "id": 3 }
        ],
        "edges": [
          {
            "source": 0,
            "target": 1,
            "metadata": {
              "distance": 5
            }
          },
          {
            "source": 1,
            "target": 3,
            "metadata": {
              "distance": 9
            }
          },
          {
            "source": 3,
            "target": 2,
            "metadata": {
              "distance": 6
            }
          },
          {
            "source": 2,
            "target": 4,
            "metadata": {
              "distance": 3
            }
          },
          {
            "source": 4,
            "target": 3,
            "metadata": {
              "distance": 8
            },
          },
          {
           "source": 4,
           "target": 0,
           "metadata": {
             "distance": 2
           }
         }
        ]
      }
    }

Additionally, all edges are **two way roads** (undirected), so you don't need
to worry about that. Which node is in `source` and which is in `target` **does
not matter**. Edges may contain the property `label`, which is just a street
name and not necessary for you to use.

And remember, the goal is to **minimize** the sum of all the
`metadata.distance` properties of edges used.

### Format of return value

The return value should be a **dictionary** with keys `distance` and `path`.

`distance` should be the number that is the total sum of the distance metadata
on each edge used.

`path` should be a **list** of **integers** , where each number is the id of a
node used along the path from the start to the end.

For example, if the shortest path from node `1` to node id `2` was going from
node 1 to node 3 to node 2, then the result should be `[1, 3, 2]`. You
**must** include the starting and ending nodes in the path.

If two paths have the same distance, it **does not matter** which one you
return (which won't happen in the tests).

### Example

In the example road graph, if I asked you to find the path from node id 2 to
node id 0, the function call would be

    navigate(roads, 2, 0) # Where roads is the example graph structure

And you should return

    {
      "distance": 5,
      "path": [ 2, 4, 0 ]
    }

### Notes

  * If two paths have the same distance, it doesn't matter which one you return (which won't happen in the tests).
  * Make sure to include the starting and ending nodes in the path.
  * The order of the path list **does** matter.
  * Distance between 2 nodes is located in the `metadata.distance` property of the edge connecting them.

"""

import json
​
class Vertex:
  def __init__(self, key):
    self.id = key 
    self.connectedTo = {}
​
  def addNeighbor(self, nbr, weight=0):
    self.connectedTo[nbr] = weight
​
  def __str__(self):
    return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
​
  def getConnections(self):
    return self.connectedTo.keys()
​
  def getId(self):
    return self.id
​
  def getWeight(self, nbr):
    return self.connectedTo[nbr]
​
class Graph:
  def __init__(self):
    self.vertList = {}
    self.numVertices = 0 
​
  def addVertex(self, key):
    self.numVertices = self.numVertices + 1 
    newVertex = Vertex(key)
    self.vertList[key] = newVertex
    return newVertex
    
  def getVertex(self, n): 
    if n in self.vertList:
      return self.vertList[n]
    else:
      return None
​
  def addEdge(self, f, t, cost=0):
    if f not in self.vertList:
      nv = self.addVertex(f)
    if t not in self.vertList:
      nv = self.addVertex(t)
    self.vertList[f].addNeighbor(self.vertList[t], cost)
    self.vertList[t].addNeighbor(self.vertList[f], cost)
​
  def getVertices(self):
    return self.vertList.keys()
​
  def __iter__(self):
    return iter(self.vertList.values())
​
​
​
def navigate(roads, startingNode, endingNode):
  data = json.loads(roads)
  n = len(data['nodes'])
  visited = [False for i in range(n)]
  edges = data['edges']
  g = Graph()
  for edge in edges:
    g.addEdge(edge['source'], edge['target'], edge['metadata']['distance'])
    
  start = g.getVertex(startingNode)
  end = g.getVertex(endingNode)
  frontier = [(0,start)]
  queue = list() 
  came_from = {}
  came_from[start] = None
  return_dict = {}
  while frontier: 
    queue += frontier
    current = queue.pop(0)[1]
    if visited[current.getId()]:
      continue
    if current == end:
      return_dict['distance'] = 0
      return_dict['path'] = []
      node_source = current
            
      while node_source is not None:
        prev_node = came_from[node_source]
        if prev_node is None:
          return_dict['path'].insert(0, node_source.getId())
          return return_dict
​
        return_dict['distance'] +=  node_source.getWeight(prev_node)
        return_dict['path'].insert(0, node_source.getId())
        node_source = prev_node
​
    for vert in current.getConnections():
      if vert not in came_from.keys():
        came_from[vert] = current
      frontier.append((vert.getWeight(current), vert))
    visited[current.getId()] = True
    frontier.sort(key=lambda x: x[0])

