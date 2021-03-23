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
def navigate(roads,start_node,end_node):
  roads = json.loads(roads)
  routes = []
  def find_routes(path=[start_node],dist=0):
    for i in roads["edges"]:
      if i["source"]==path[-1] and i["target"] not in path[:-1]:
        if i["target"]==end_node:
          routes.append([dist+i["metadata"]["distance"],path+[end_node]])
        else:
          find_routes(path+[i["target"]],dist+i["metadata"]["distance"])
      elif i["target"]==path[-1] and i["source"] not in path[:-1]:
        if i["source"]==end_node:
          routes.append([dist+i["metadata"]["distance"],path+[end_node]])
        else:
          find_routes(path+[i["source"]],dist+i["metadata"]["distance"])
  find_routes()
  routes.sort()
  return {"distance": routes[0][0], "path": routes[0][1]}

