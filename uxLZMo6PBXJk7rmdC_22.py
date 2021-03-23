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
from collections import namedtuple
​
Edge = namedtuple('Edge', 'target distance')
Node = namedtuple('Node', 'distance route visited')
​
# Could improve with a heap.
def lowest_unvisited(nodes):
  lowest = None
  lowest_id = -1
  for id, node in nodes.items():
    if not node.visited and node.distance is not None:
      if lowest is None or lowest.distance > node.distance:
        lowest = node
        lowest_id = id
  return lowest_id, lowest
​
def navigate(roads, startingNode, endingNode):
  graph = json.loads(roads)
  edges = {}
  nodes = {}
  for node in graph['nodes']:
    edges[node['id']] = set()
    nodes[node['id']] = Node(None, [], False)
  for edge in graph['edges']:
    edges[edge['source']].add(Edge(edge['target'], edge['metadata']['distance']))
    edges[edge['target']].add(Edge(edge['source'], edge['metadata']['distance']))
  nodes[startingNode] = Node(0, [startingNode], False)
  while not nodes[endingNode].visited:
    id, node = lowest_unvisited(nodes)
    nodes[id] = Node(node.distance, node.route, True)
    for edge in edges[id]:
      other = nodes[edge.target]
      if not other.visited:
        new_distance = node.distance + edge.distance
        if other.distance is None or other.distance > new_distance:
          nodes[edge.target] = Node(new_distance, node.route + [edge.target], False)
  return {"distance": nodes[endingNode].distance,
          "path": nodes[endingNode].route }

