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

def water_transfer(source, destination, limit):
    available = limit - destination
    if source <= available:
        return 0, destination + source
    return source - available, limit
​
​
def waterjug(start, goal):
    initial_state = [0, 0, start[2]]
    if initial_state == goal:
        return 0
    elif sum(initial_state) != sum(goal):
        return 'No solution.'
    count = 0
    known_states = [initial_state]
    current_states = [initial_state]
    while current_states:
        new_states = []
        for state in current_states:
            for tpl in [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]:
                new_state = state[:]
                idx_source, idx_destination = tpl
                source_amount = state[idx_source]
                destination_amount = state[idx_destination]
                destination_limit = start[idx_destination]
                if (source_amount > 0 and
                        destination_amount < destination_limit):
                    new_s, new_d = water_transfer(source_amount,
                                                  destination_amount,
                                                  destination_limit)
                    new_state[idx_source] = new_s
                    new_state[idx_destination] = new_d
                    if new_state == goal:
                        return count + 1
                if new_state not in known_states:
                    known_states.append(new_state)
                    new_states.append(new_state)
        current_states = new_states
        count += 1
    return 'No solution.'

