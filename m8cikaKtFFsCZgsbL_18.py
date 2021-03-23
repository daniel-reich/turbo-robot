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

def waterjug(start, goal):
    if not start or not goal or not len(start) == len(goal) == 3:
        return "No solution."
​
    checked_configs = set()  
    from collections import deque
    open_configs = deque()
    open_configs.append(([0, 0, start[2]], 0))
    
    def pour(config, i_from, i_to):
        config = config[:]
        if config[i_from] <= start[i_to] - config[i_to]:
          config[i_to] += config[i_from]
          config[i_from] = 0
        else:
          config[i_from] -= start[i_to] - config[i_to]
          config[i_to] = start[i_to]
​
        return config
​
    
    while open_configs:
        config, ops = open_configs.popleft()
        
        if config == goal:
            return ops
            
        candidates = [
            pour(config, 0, 1),
            pour(config, 0, 2),
            pour(config, 1, 0),
            pour(config, 1, 2),
            pour(config, 2, 0),
            pour(config, 2, 1)
        ]
        
        for c in candidates:
            # simple 'hashing' of configurations - works as long as capacities stay relatively small
            key = c[0]+1000*c[1]+1000000*c[2]
            if not key in checked_configs:
                checked_configs.add(key)
                open_configs.append((c, ops+1))
        
            
    return "No solution."

