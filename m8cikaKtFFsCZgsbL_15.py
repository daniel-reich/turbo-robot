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
    capA, capB, capC = start
    A, B, C = 0, 0, capC
    goal = tuple(goal)
    if sum(goal) != capC:
        return "No solution."
    moves = {(A, B, C): 0}
    queue = [(A, B, C)]
    while len(queue) > 0:
        curA, curB, curC = queue.pop(0)
        cur_moves = moves[(curA, curB, curC)]
        if curA > 0:
            if curB < capB:
                # water can be filled from jug A to jug B:
                t = min(capB - curB, curA)
                nextA, nextB = curA - t, curB + t
                state = (nextA, nextB, curC)
                if state not in moves:
                    moves[state] = cur_moves + 1
                    queue.append(state)
            if curC < capC:
                # water can be filled from jug A to jug C:
                t = min(capC - curC, curA)
                nextA, nextC = curA - t, curC + t
                state = (nextA, curB, nextC)
                if state not in moves:
                    moves[state] = cur_moves + 1
                    queue.append(state)
        if curB > 0:
            if curA < capA:
                # water can be filled from jug B to jug A:
                t = min(capA - curA, curB)
                nextB, nextA = curB - t, curA + t
                state = (nextA, nextB, curC)
                if state not in moves:
                    moves[state] = cur_moves + 1
                    queue.append(state)
            if curC < capC:
                # water can be filled from jug B to jug C:
                t = min(capC - curC, curB)
                nextB, nextC = curB - t, curC + t
                state = (curA, nextB, nextC)
                if state not in moves:
                    moves[state] = cur_moves + 1
                    queue.append(state)
        if curC > 0:
            if curA < capA:
                # water can be filled from jug C to jug A:
                t = min(capA - curA, curC)
                nextC, nextA = curC - t, curA + t
                state = (nextA, curB, nextC)
                if state not in moves:
                    moves[state] = cur_moves + 1
                    queue.append(state)
            if curB < capB:
                # water can be filled from jug C to jug B:
                t = min(capB - curB, curC)
                nextC, nextB = curC - t, curB + t
                state = (curA, nextB, nextC)
                if state not in moves:
                    moves[state] = cur_moves + 1
                    queue.append(state)
        if goal in moves:
            return moves[goal]
    return "No solution."

