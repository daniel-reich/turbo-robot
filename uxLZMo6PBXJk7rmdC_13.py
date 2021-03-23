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
roads = """
{
  "directed": false,
  "nodes": [
    { "id": 0 },
    { "id": 1 },
    { "id": 2 },
    { "id": 3 },
    { "id": 4 },
    { "id": 5 },
    { "id": 6 },
    { "id": 7 },
    { "id": 8 },
    { "id": 9 }
  ],
  "edges": [
    {
      "source": 1,
      "target": 6,
      "label": "Oak Street",
      "metadata": {
        "distance": 5
      }
    },
    {
      "source": 6,
      "target": 8,
      "label": "Oak Street",
      "metadata": {
        "distance": 6
      }
    },
    {
      "source": 8,
      "target": 9,
      "label": "Oak Street",
      "metadata": {
        "distance": 11
      }
    },
    {
      "source": 8,
      "target": 7,
      "label": "Robin Way",
      "metadata": {
        "distance": 3
      }
    },
    {
      "source": 7,
      "target": 4,
      "label": "Robin Way",
      "metadata": {
        "distance": 5
      }
    },
    {
      "source": 6,
      "target": 7,
      "label": "Mountain Road",
      "metadata": {
        "distance": 8
      }
    },
    {
      "source": 7,
      "target": 9,
      "label": "Mountain Road",
      "metadata": {
        "distance": 9
      }
    },
    {
      "source": 4,
      "target": 3,
      "label": "National Street",
      "metadata": {
        "distance": 6
      }
    },
    {
      "source": 1,
      "target": 0,
      "label": "Sunrise Drive",
      "metadata": {
        "distance": 4
      }
    },
    {
      "source": 0,
      "target": 3,
      "label": "Short Street",
      "metadata": {
        "distance": 3
      }
    },
    {
      "source": 5,
      "target": 4,
      "label": "Rickety Creek",
      "metadata": {
        "distance": 7
      }
    },
    {
      "source": 4,
      "target": 0,
      "label": "Rickety Creek",
      "metadata": {
        "distance": 5
      }
    },
    {
      "source": 9,
      "target": 5,
      "label": "Uphill Grove",
      "metadata": {
        "distance": 6
      }
    },
    {
      "source": 5,
      "target": 2,
      "label": "Uphill Grove",
      "metadata": {
        "distance": 5
      }
    },
    {
      "source": 2,
      "target": 3,
      "label": "Uphill Grove",
      "metadata": {
        "distance": 7
      }
    }
  ]
}
"""
#-----------------------------------------------------------------------
def getDistance(mp, p1, p2):
    #print("\n\nDistances")
    for x in mp['edges']:
        #print('S {} T {} D {}'.format(x['source'], x['target'], x['metadata']['distance']))
        if(x['source'] == p1 and x['target'] == p2):
            return x['metadata']['distance']
        elif(x['target'] == p1 and x['source'] == p2):
            return x['metadata']['distance']
    else:
        return 9999
​
#-----------------------------------------------------------------------
def getNodes(mp):
    lst = []
    for x in mp['nodes']:
        lst.append(x['id'])
    return lst
​
#-----------------------------------------------------------------------
def getUnvisitedNeighbors(mp, visiting, notVisited, table):
    res = []
    nwMp = mp['edges']
    for node in notVisited:
        for mpEnt in nwMp:
            # node not same as 'visiting node' and node connected to visiting
            if(visiting != node and
               ((mpEnt['source'] == node) and
                (mpEnt['target'] == visiting)) or
               ((mpEnt['target'] == node) and
                (mpEnt['source'] == visiting))):
​
                # Add [node, distace to start] to list
                distStartToNode = getDistance(mp, node, visiting)
                distStartToNode += table[visiting][1]
                res.append([node, distStartToNode])
    res.sort(key= lambda v: v[1])
    return res
​
#-----------------------------------------------------------------------
# Get next node to visit
# Table[[a, b, c],...]
#   a = node index
#   b = distance to start node
#   c = previous node
def getNextNode(table, notVisited):
    nd = -1
    min = 1000000
    for entry in table:
        if(entry[0] in notVisited and entry[1] < min):
            nd = entry[0]
            min = entry[1]
    return nd
    
​
​
def navigate(roads, start, end):
    mp = json.loads(roads)
    #print(mp)
    d = getDistance(mp, 0, 3)
​
    # Initialize data
    nds = getNodes(mp)    
    visited = []
    notVisited = nds[:]
​
    # Initialize table
    table = []
    for n in nds:
        table.append([n, 1000, 1000])
    table[start][1] = 0
    table[start][2] = start
    #print('TABLE {}'.format(table))
​
​
    while(len(notVisited) > 0):
        #print('\nTABLE {} NOT VIS {}'.format(table, notVisited))
        visiting = getNextNode(table, notVisited)
        #print('Vistiting {}'.format(visiting))
        vals = getUnvisitedNeighbors(mp, visiting, notVisited, table)
        #print('LIST {}'.format(vals))
        for v in vals:
            ind = v[0]
            if(v[1] < table[ind][1]):
                table[ind][1] = v[1]
                table[ind][2] = visiting
        indxNd = notVisited.index(visiting)
        visited.append(notVisited.pop(indxNd))
​
    nd = end
    path = []
    path.append(nd)
    while nd != start:
        n = table[nd][2]
        path.append(n)
        nd = n
    path.reverse()
    #print(path)
    ret = {'distance': table[end][1], 'path':path}
    return ret

