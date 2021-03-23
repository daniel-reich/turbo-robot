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
    full = start
    start = [0, 0, full[2]]
    opFree = {
        "f_0": lambda x: [full[0], x[1], x[2]],
        "f_1": lambda x: [x[0], full[1], x[2]],
        "f_2": lambda x: [x[0], x[1], full[2]],
        "e_0": lambda x: [0, x[1], x[2]],
        "e_1": lambda x: [x[0], 0, x[2]],
        "e_2": lambda x: [x[0], x[1], 0]
    }
​
    def m(a, b, x): return min(x[a], full[b] - x[b])
    opCost = {
        "t01": lambda x: [x[0] - m(0, 1, x), x[1] + m(0, 1, x), x[2]],
        "t02": lambda x: [x[0] - m(0, 2, x), x[1], x[2] + m(0, 2, x)],
        "t10": lambda x: [x[0] + m(1, 0, x), x[1] - m(1, 0, x), x[2]],
        "t12": lambda x: [x[0], x[1] - m(1, 2, x), x[2] + m(1, 2, x)],
        "t20": lambda x: [x[0] + m(2, 0, x), x[1], x[2] - m(2, 0, x)],
        "t21": lambda x: [x[0], x[1] + m(2, 1, x), x[2] - m(2, 1, x)]
    }
​
    visited = [start]
    steps = 0
    flag = 0
​
    while goal not in visited:
        visitedLength = len(visited)
        for F in opFree:
            for x in visited:
                newState = opFree[F](x)
                if newState not in visited and sum(newState) <= full[2]:
                    visited.append(newState)
​
        if goal in visited:
            break
        else:
            flag = 0
            visitedPrev = visited.copy()
            for F in opCost:
                for x in visitedPrev:
                    newState = opCost[F](x)
                    if newState not in visited and sum(newState) <= full[2]:
                        visited.append(opCost[F](x))
                        flag = 1
            if flag:
                steps += 1
        if visitedLength == len(visited):
            return "No solution."
    return steps

