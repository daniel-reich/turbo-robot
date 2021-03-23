"""


It's been a long day for Matt. After working on Edabit for quite a bit, he
decided to go out and get a beer at the local bar a few miles down the road.
However, what Matt didn't realise, was that with too much drinks you can't
find the way home properly anymore. Your goal is to help Matt get back home by
telling him how long the path to his house is if he drives the optimal route.

Matt lives in a simple world: there is only dirt (represented by a dot), a
single house (Matt's house, represented by the letter "h") and there are trees
(represented by the letter "t") which he obviously can't drive through. Matt
has an unlimited amount of moves and each move he can go north, north-east,
east, south-east, south, south-west, west and north-west. There will only be
one Matt and one house, which is Matt's.

The world is given to you as a comma-delimited string which represents the
cells in the world from top-left to bottom-right. A 3x3 world with Matt on the
top-left and his house on the bottom-right, with a tree in the middle would be
represented as:

    m,.,.,.,t,.,.,.,h

The answer to this world would be 3: Matt would first move east, then south-
east, then south (or south > south-east > east). The function call related to
this example would be the following:

    get_path_length("m,.,.,.,t,.,.,.,h", 3, 3)

If Matt is unable to get home from his current location, return `-1`,
otherwise return the amount of moves Matt has to make to get home if he
follows the optimal path. You are given the world, it's width and it's height.

 **Good luck!**

"""

from heapq import heapify, heappop, heappush
from itertools import product
​
def moves(the_map, x, y):
    neigh = []
    h = len(the_map)
    w = len(the_map[0])
    for dx, dy in product([-1, 0, 1], repeat=2):
        if dx == 0 and dy == 0:
            continue
        x2 = x + dx
        y2 = y + dy
        if x2 < 0 or y2 < 0 or x2 >= w or y2 >= h:
            continue
        if the_map[y2][x2] != 't':
            neigh.append((x2, y2)), 
    return neigh
​
def get_path_length(world, width, height):
  vals = world.split(',')
  w = [''.join(vals[width*r:(r+1)*width]) for r in range(height)]
  s = vals.index('m')
  start = (s % width, s//height)
  
  Q = []
  dists = {start: 0,}
  heappush(Q, (0, start))
​
  while Q:
      d, u = heappop(Q)
      if w[u[1]][u[0]] == 'h':
          return d
      for v in moves(w, *u):
          d2 = d + 1
          if v in dists:
            continue
          dists[v] = d2
          heappush(Q, (d2, v))
  return -1

