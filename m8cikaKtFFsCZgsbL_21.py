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
    source = [[0, 0, start[2]]]
    result = inception(source, start, goal, 0)
    return result
​
def pour(source, destination, jugs, capacity):
    localJugs = [x for x in jugs]
    pourableAmt = capacity[destination] - localJugs[destination]
    if localJugs[source] > pourableAmt:
        localJugs[source] -= pourableAmt
        localJugs[destination] += pourableAmt
    else:
        localJugs[destination] += localJugs[source]
        localJugs[source] = 0
​
    return localJugs
​
def inception(jugArray, capacity, goal, level):
    tempArr = []
    if level == 10:
        return "No solution."
    if goal in jugArray:
        return level
​
    for jugs in jugArray:
        for x in range(3):
            for y in range(3):
                if jugs != pour(x, y, jugs, capacity):
                    tempArr.append(pour(x, y, jugs, capacity))
    
    level += 1
    jugArray = tempArr
    level = inception(jugArray, capacity, goal, level)
    return level

