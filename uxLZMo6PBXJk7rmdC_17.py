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

def get_graph(j_graph):
    '''
    Generates a graph suitable for the problem from the json j_graph.
    '''
    import json
???
    g = json.loads(j_graph)
    nodes = sorted([item['id'] for item in g['nodes']])
    edges = [(item['source'],item['target'],item['metadata']['distance']) \
             for item in g['edges']]  # node, node, weight(distance)
    edges = sorted(edges + [(b,a,w) for a,b,w in edges]) # add reverse links & sort
    
    return {node:[(b,w) for a,b,w in edges if a == node] for node in nodes} # link them
    
???
def navigate(roads, s, e):
    '''
    Returns the shortest distance and path between nodes s and e as per instructions.
    roads is a JSON style graph. Uses Dijkstra's algorithm with priority queue.
    '''
    import heapq as h
    
    graph = get_graph(roads)  # convert to more usable format
    distances = {node: float('inf') for node in graph}
    prev = {node: -1 for node in graph}  # to trace the path
    q = []
    distances[s] = 0
    h.heappush(q, (0, s))  # start node in the queue at distance 0
???
    while q:
        u = h.heappop(q)[1]
        if u == e:
            break  # reached target node
        
        for edge, dis in graph[u]:
            if distances[edge] > distances[u] + dis:
                distances[edge] = distances[u] + dis
                prev[edge] = u
                h.heappush(q, (distances[edge], edge))  # queue at distance priority
???
    distance = distances[e]
    path = []
    node = e
    while node != -1:
        path.append(node)
        node = prev[node]
???
    return {'distance': distance, 'path': path[::-1]}

