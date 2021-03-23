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
def navigate(roads_str, source, destination):
    
    roads = json.loads(roads_str)
    #print(roads)
​
    nodes = roads["nodes"]
    nodes_total = len(nodes)
    edges = roads["edges"]
     
    
    nodes_prev = [-1]*(nodes_total)
    
    nodes_dist = [-1]*(nodes_total)
    nodes_dist[source] = 0
​
    working_list = []
    for i in range(nodes_total):
        working_list.append(i)
    length = len(working_list)
    while(length != 0):
        min_index = working_list[0]
        min_dist = nodes_dist[min_index]
        working_node = -1
        for i in range(length):
            if working_list[i] != -1:
                
                if min_dist == -1 or (min_dist > nodes_dist[working_list[i]] and nodes_dist[working_list[i]] != -1):
                    
                    min_index = working_list[i]
                    min_dist = nodes_dist[min_index]
        if min_dist != -1:
            
            working_node = min_index
 
            working_list.remove(min_index) 
            for edge in edges:
                neighbor_node = -1
                if working_node == edge["source"]:
                    neighbor_node = edge["target"]
                    
                elif working_node == edge["target"]:
                    neighbor_node = edge["source"]
                    
                if neighbor_node != -1:
                    if nodes_dist[working_node] + edge["metadata"]["distance"] < nodes_dist[neighbor_node] or nodes_dist[neighbor_node] == -1:
                        nodes_dist[neighbor_node] = nodes_dist[working_node] + edge["metadata"]["distance"]
                        nodes_prev[neighbor_node] = working_node
  
        else:
            break
        length = len(working_list)
    
​
    result = {}
    result["distance"] = 0
    result["path"] = []
    
    result["distance"] = nodes_dist[destination]
    current = destination
    while current != -1:
        result["path"].append(current)
        current = nodes_prev[current]
    result["path"].reverse()
    return result

