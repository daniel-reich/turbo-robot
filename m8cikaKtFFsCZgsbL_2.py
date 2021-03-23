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

def process(state,i,others,capacities):
    '''
    Returns the jug states possible from permissible changes to state[i]
    '''
    possibles = []
    temp = list(state)
    temp[i] = 0  # can always empty it!
    possibles.append(tuple(temp))
    for pos in others:
        temp = list(state)
        pourable = min(temp[i],capacities[pos] - temp[pos])
        temp[i] -= pourable
        temp[pos] += pourable
        possibles.append(tuple(temp))  # water poured from i.
​
    return possibles
    
def get_states(state, capacities):
    '''
    Returns a list of all the states possible from this one, based on
    permissible actions
    '''
    states = []
    size = len(state)
    for i in range(size):
        if state[i]:  # it's got some water
            others = sorted(set(range(size)) - {i})
            states += process(state,i,others,capacities)
​
    return states
​
def waterjug(capacities, target):
    '''
    Returns the minimum number of moves to reach target from the start state,
    or 'No solution' if not possible, given constraints and operations as per
    the instructions.
    '''
    CAPS = {i:jug for i, jug in enumerate(capacities)}
    start = (0,0,CAPS[2])
    target = tuple(target)
    if sum(target) > start[2]:
        return 'No solution.'
​
    q = [start]
    visited = set()
    path = {start:0}
​
    while q:
        state = q.pop(0)
        visited.add(state)
        if state == target:
            count = 0
            current = target
            while current != start:
                count += 1
                current = path[current]
​
            return count
​
        for next_state in get_states(state,CAPS):  # all states possible from here
            if next_state not in visited and next_state not in q:
                path[next_state] = state  # show it came from here
                q.append(next_state)
​
    return 'No solution.'  # did not find target

