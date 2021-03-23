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
import heapq
​
class UndirectedGraph():
​
    def __init__(self):
        self.nodes = []
        self.edges = {}
​
    def AddNode(self, node):
        # add node; do nothing if node already exists
        if node in self.nodes:
            return
        self.nodes.append(node)
        self.edges[node] = {}
​
    def AddEdge(self, node1, node2, weight=1):
        # add edge (optionally with weight)
        assert node1 in self.nodes and node2 in self.nodes
        if node1 not in self.edges[node2]:
            self.edges[node2][node1] = weight
        if node2 not in self.edges[node1]:
            self.edges[node1][node2] = weight
​
    def GetNodes(self):
        return self.nodes
​
    def GetEdges(self, node):
        return self.edges.get(node, {})
​
    def GetWeightedEdges(self, node):
        return self.edges[node].items()
​
    def GetDegree(self, node):
        return len(self.edges.get(node, {}).keys())
​
    def Dijkstra(self, s, t):
        BIGNUM = 2**31
        X = set()
        key = {node: BIGNUM for node in self.GetNodes()}
        key[s] = 0
        H = [(v, k) for k, v in key.items()]
        Len = {s: 0}
        heapq.heapify(H)
        prev = {node: None for node in self.GetNodes()}
        while len(H) > 0:
            key_wstar, wstar = heapq.heappop(H)
            X.add(wstar)
            Len[wstar] = key[wstar]
            for y, weight in self.GetWeightedEdges(wstar):
                if prev[y] == None:
                    prev[y] = wstar
                if (key[y], y) in H:
                    H.remove((key[y], y))
                    if Len[wstar] + weight < key[y]:
                        key[y] = Len[wstar] + weight
                        prev[y] = wstar
                    key[y] = min(key[y], Len[wstar] + weight)
                    if y not in X:
                        heapq.heappush(H, (key[y], y))
            heapq.heapify(H)
        path = [t]
        cur = t
        while cur != s:
            cur = prev[cur]
            path.append(cur)
        ans = {"distance": Len[t], "path": path[::-1]}
        return ans
     
        
        
def navigate(roads, startingNode, endingNode):
    data = json.loads(roads)
    G = UndirectedGraph()
    for item in data['nodes']:
        G.AddNode(item['id'])
    for item in data['edges']:
        node1 = item['source']
        node2 = item['target']
        distance = item['metadata']['distance']
        G.AddEdge(node1, node2, distance)
        G.AddEdge(node2, node1, distance)
    return G.Dijkstra(startingNode, endingNode)

