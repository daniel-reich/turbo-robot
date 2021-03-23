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

from collections import deque
​
​
def waterjug(start, goal):
    lastJugCapacity = start[-1]
    sizes = start
    goal = tuple(goal)
    initial = tuple(([0] * (len(start) - 1)) + [start[-1]])
​
    clones = deque([(initial, 0, "initial", [initial])])
    calculated = set()
​
    while clones:
        jugs, step, move, path = tuple(clones.popleft())
​
        if jugs in calculated:
            continue
        else:
            calculated.add(jugs)
​
        if jugs == goal and sum(jugs[:-1]) != lastJugCapacity:
            # for j, s, m in path:
            #     print("{} {} {}".format(j, s, m))
            return step
​
        for i, (jug, jugSize) in enumerate(zip(jugs, sizes)):
            # empty jug
            if jug > 0:
                clone = list(jugs)
                clone[i] = 0
                clone = tuple(clone)
                clones.append((tuple(clone), step + 1, "empty {}".format(i), path + [(jugs, step, move,)]))
            # fill jug
            if jug < jugSize:
                clone = list(jugs)
                clone[i] = jugSize
                clone = tuple(clone)
                clones.append((tuple(clone), step + 1, "fill {}".format(i), path + [(jugs, step, move,)]))
​
            for j, (targetJug, targetJugSize) in enumerate(zip(jugs, sizes)):
                if i == j:
                    continue
                if targetJug == targetJugSize:
                    continue
                if jug == 0:
                    continue
​
                before = jug + targetJug
                toTranfer = min(jug, targetJugSize - targetJug)
​
                clone = list(jugs)
                clone[i] -= toTranfer
                clone[j] += toTranfer
                assert clone[i] + clone[j] == before
​
                clone = tuple(clone)
                clones.append((tuple(clone), step + 1, "move {} to {}".format(i, j), path + [(jugs, step, move,)]))
    return "No solution."

