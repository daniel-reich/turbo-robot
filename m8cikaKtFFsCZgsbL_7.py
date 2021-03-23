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

def waterjug(cap, goal):
    cap = tuple(cap + [cap[2]])
    goal = tuple(goal + [0])
    starting_state = (0, 0, cap[2], 0)
    steps = 0
    if starting_state[:3] == goal[:3]:
        return steps
    # depth first search
    prev_states = set()
    curr_states = set([starting_state])
    while curr_states:
        steps += 1
        next_states = set()
        for cs in curr_states:
            prev_states.add(cs)
            succ = possible_successors(cs, cap)
            for ns in succ:
                if ns not in prev_states:
                    if ns[:3] == goal[:3]:
                        return steps
                    next_states.add(ns)
        curr_states = next_states
    return "No solution."
​
​
def possible_successors(cs, cap):
    ret = []
    # a jug is poured into another until either is full or empty
    has_water = [i for i in range(len(cs)) if cs[i] > 0]
    under_cap = [i for i in range(len(cs)) if cs[i] < cap[i]]
    for h in has_water:
        for u in under_cap:
            if h != u:
                k = [0, 1, 2, 3]; k.remove(h); k.remove(u)
                unused = cap[u] - cs[u]
                if cs[h] > unused: # fill under_cap
                    poured = [(h, cs[h]-unused), (u, cap[u]), (k[0], cs[k[0]]), (k[1], cs[k[1]])]
                elif cs[h] <= unused: # empty has_water
                    if h == 3 and cs[h] != unused: # cannot partially fill empty jug
                        break
                    poured = [(h, 0), (u, cs[u]+cs[h]), (k[0], cs[k[0]]), (k[1], cs[k[1]])]
                poured = [p[1] for p in sorted(poured)]
                ret.append(tuple(poured))
    return list(set(ret))

