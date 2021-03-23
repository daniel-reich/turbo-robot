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

from json import loads
def navigate(roads, startingNode, endingNode):
  roads = loads(roads)
  visited = set()
  graph = dict()
  data = dict()
  for edge in roads["edges"]:
    graph[edge["source"]] = graph.get(edge["source"], []) + [[edge["target"], edge["metadata"]["distance"]]]
    graph[edge["target"]] = graph.get(edge["target"], []) + [[edge["source"], edge["metadata"]["distance"]]]
    if edge["source"] not in data: data[edge["source"]] = {"distance": float("inf"), "previous": None}
    if edge["target"] not in data: data[edge["target"]] = {"distance": float("inf"), "previous": None}
  data[startingNode]["distance"] = 0
​
  nxt = startingNode
​
  while True:
    for i in [j for j in graph[nxt] if j[0] not in visited]:
      if data[i[0]]["distance"] > data[nxt]["distance"] + i[1]:
        data[i[0]]["distance"] = data[nxt]["distance"] + i[1]
        data[i[0]]["previous"] = nxt
    visited.add(nxt)
    nxt = sorted([k for k in data if k not in visited], key=lambda x: data[x]["distance"])
    if not nxt: break
    nxt = nxt[0]
    
  path = [endingNode]
  
  while True:
    if data[path[-1]]["previous"] is not None:
      path.append(data[path[-1]]["previous"])
    else:
      break
  
  return {'distance': data[endingNode]["distance"], 'path': path[::-1]}

