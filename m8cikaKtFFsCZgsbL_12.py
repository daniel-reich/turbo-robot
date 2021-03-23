"""


Given a set of 3 jugs of water that have capacities of _a_ , _b_ , and _c_
liters, find the minimum number of operations performed before each jug has
_x_ , _y_ , and _z_ liters. Only jug C will start completely filled.

An operation is any of the following: A jug is emptied, a jug is filled, or
water is poured from one jug to another until one of the jugs is either empty
or full.

For example, jugs "A", "B", and "C" with capacities of 3, 5, and 8, where jugs
"A" and "B" start empty and "C" has the full 8, require 2 operations to reach
the state of 0, 3, and 5 liters in the jugs.

Create a function that, given an array of jug capacities `[A, B, C]` and an
goal state array `[x, y, z]`, returns the minimum number of operations needed
to reach the goal state. If the inputs are invalid or there is no solution,
return `"No solution."`

### Examples

    waterjug([3, 5, 8], [0, 3, 5]) ➞ 2
    
    waterjug([1, 3, 4],  [0, 2, 2]) ➞ 3
    
    waterjug([8, 17, 20], [0, 10, 10]) ➞ 9
    
    waterjug([4, 17, 22], [2, 5, 15]) ➞ "No solution."
    
    waterjug([3, 5, 8], [0, 0, 9]) ➞ "No solution."

### Notes

  * The amount of water in a jug can never exceed the capacity of that jug.
  * The total liters in the goal state must be equal to the capacity of jug "C".

"""

from heapq import heappop, heappush
from itertools import combinations
​
def pours(curr, avail):
    for a, b in combinations(range(len(avail)), 2):
        # pour from a to b and b to a
        for x, y in [(a, b), (b, a)]:
            if curr[x] < avail[x] and curr[y] > 0:
                new = list(curr)
                to_give = min(avail[x]-curr[x], curr[y])
                new[x] += to_give
                new[y] -= to_give
                yield tuple(new)
​
def waterjug(start, goal):
  state = [0 for _ in start]
  state[-1] = start[-1]
  
  Q = []
  dists = {tuple(state): 0,}
  heappush(Q, (0, tuple(state)))
​
  while Q:
      d, u = heappop(Q)
      if u == tuple(goal):
          return d
      for v in pours(u, start):
          d2 = d + 1
          if tuple(v) in dists:
              continue
          dists[v] = d2
          heappush(Q, (d2, v))
  return 'No solution.'

