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

def add_state(s, states, prev_states):
  s = (s[0], s[1], s[2])
  if s in prev_states:
    return
  states.append(s)
  prev_states.add(s)
def waterjug(start, goal):
  goal = (goal[0], goal[1], goal[2])
  states = []
  next_states = [(0, 0, start[2])]
  steps = -1
  prev_states = {(0, 0, start[2])}
  while len(next_states) > 0:
    states = next_states
    next_states = []
    steps += 1
    while len(states) > 0:
      state = states.pop()
      if state == goal:
        return steps
      for i in range(3):
        for i2 in range(3):
          if i != i2:
            new_state = list(state[:])
            diff = min(state[i], start[i2] - state[i2])
            new_state[i] -= diff
            new_state[i2] += diff
            add_state(new_state, next_states, prev_states)
  return "No solution."

