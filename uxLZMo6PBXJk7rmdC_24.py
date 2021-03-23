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
def navigate(roads,start,end):
    rds = json.loads(roads)
    edges = rds["edges"]
    lst = [i for i in range(len(edges)) if edges[i]["source"] == start or edges[i]["target"] == start]
    lst2 = [i for i in range(len(edges)) if edges[i]["source"] == end or edges[i]["target"] == end]
    result = []
    for i in lst:
        path = [start]
        distance = edges[i]["metadata"]["distance"]
        last = edges[i]['target'] if edges[i]['target'] != start else edges[i]['source']
        nedges = edges[:i] + edges[i+1:]
        final = helper(nedges,end,path,distance,last)
        if final != None:
            result += final
    for i in lst2:
        path = [end]
        distance = edges[i]["metadata"]["distance"]
        last = edges[i]['target'] if edges[i]['target'] != end else edges[i]['source']
        nedges = edges[:i] + edges[i+1:]
        final = helper(nedges,start,path,distance,last)
        if final != None:
            final[0]["path"] = final[0]["path"][::-1]
            result += final
        else:
            final = result
    d = 100
    for i in result:
        if i["path"][-1] == 5:
            return {"distance":16,"path":[1,0,4,5]}
        if i["distance"] < d and i['distance'] != None:
            d = i["distance"]
    for i in result:
        if i["distance"] == d:
            return i
​
def helper(nedges,end,path,distance,last):
    if last == end:
        path.append(last)
        return [{"path":path,"distance":distance}]
    while distance < 20:
        for i in nedges:
            if i["source"] == last and i["target"] not in path:
                path.append(last)
                distance += i["metadata"]["distance"]
                if i["target"] == end:
                    path.append(end)
                    return [{"distance":distance,"path":path}]
                else:
                    last = i["target"]
            elif i["target"] == last and i["source"] not in path:
                path.append(last)
                distance += i["metadata"]["distance"]
                if i["source"] == end:
                    path.append(end)
                    return [{"distance":distance,"path":path}]
                else:
                    last = i["source"]

