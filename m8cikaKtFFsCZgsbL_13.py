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

import math
​
def waterjug(start, goal):
  global found
  hst = {}
  stc = []
  found = False
  def asStr(ls):
    return str(ls[0]) + ',' + str(ls[1]) + ',' + str(ls[2])
​
  def pour(state, _from, _to, _other):
    res = [-1,-1,-1]
    cap = start[_to] - state[_to]
    amt = min(cap, state[_from])
    if amt is 0:
      return
    res[_from] = state[_from] - amt
    res[_to] = state[_to] + amt
    res[_other] = state[_other]
    stc.append(res)
  
  def iter(state):
    global found
    try:
      h = hst[asStr(state)]
      return
    except:
      hst[asStr(state)] = True
      #print(asStr(state))
      #print(asStr(goal))
      if asStr(state) == asStr(goal):
        found = True
        return
      pour(state, 0, 1, 2)
      pour(state, 0, 2, 1)
      pour(state, 1, 0, 2)
      pour(state, 1, 2, 0)
      pour(state, 2, 0, 1)
      pour(state, 2, 1, 0)
    
  count = 0
  run = True
  left = []
  stc.append([0, 0, start[2]])
  while run:
    run = False
    left = stc
    stc = []
    for x in left:
      run = True
      iter(x)
    if found:
      return count
    count += 1
  return 'No solution.'

