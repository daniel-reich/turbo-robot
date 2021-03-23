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

def largest_island(lst):
  coordinates = {}
  x_cord = 0
  y_cord = 0
  for row in reversed(lst):
    for i_point in row:
      if i_point:
        coordinates[(x_cord, y_cord)] = [(x_cord+1, y_cord), (x_cord+1, y_cord-1),(x_cord, y_cord-1), (x_cord-1, y_cord-1),(x_cord-1, y_cord), (x_cord-1, y_cord+1),(x_cord, y_cord+1), (x_cord+1, y_cord+1)]
      x_cord += 1
    y_cord += 1
    x_cord = 0
  neigh_cords = {}
  for l_island, poss_neigh in coordinates.items():
    neigh_cords[l_island] = {}
    neigh_cords[l_island]["neighbors"] = []
    for neigh_c in poss_neigh:
      if neigh_c in coordinates.keys():
        neigh_cords[l_island]["neighbors"] += [neigh_c]
  for isl, ns in neigh_cords.items():
    neigh_cords[isl]["no_ns"] = len(ns["neighbors"])
  return get_neighbors(neigh_cords)
​
def get_neighbors(coord_sys):
  for l_i, neighs in coord_sys.items():
    for n_i in neighs["neighbors"]:
      for f_i, f_n in coord_sys.items():
        if (n_i in f_n["neighbors"]) and not (f_i in neighs["neighbors"]):
          neighs["no_ns"] += 1
          neighs["neighbors"].append(f_i)
  largest_i = max([x["no_ns"] for x in coord_sys.values()])
  if largest_i == 0:
    largest_i = 1
  return largest_i

