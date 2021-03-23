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

import copy
​
​
class Jug(object):
    def __init__(self, water, volume):
        self.water = water
        self.volume = volume
​
    def __eq__(self, other):
        return self.water == other.water and self.volume == other.volume
​
    def __repr__(self):
        return 'JUG: {} // {}'.format(self.water, self.volume)
​
    def pour_from_to(self, other):
        while other.water < other.volume and self.water:
            self.water -= 1
            other.water += 1
        return self, other
​
​
def perform_pours_on_state(state):
    result = [copy.deepcopy(state) for i in range(6)]
    Jug.pour_from_to(result[0][0], result[0][1])
    Jug.pour_from_to(result[1][0], result[1][2])
    Jug.pour_from_to(result[2][1], result[2][0])
    Jug.pour_from_to(result[3][1], result[3][2])
    Jug.pour_from_to(result[4][2], result[4][0])
    Jug.pour_from_to(result[5][2], result[5][1])
    return [entry for entry in result if entry != state]
​
​
def waterjug(start, goal):
    initial = [
        Jug(0, start[0]),
        Jug(0, start[1]),
        Jug(start[2], start[2])
    ]
​
    target = [
        Jug(goal[0], start[0]),
        Jug(goal[1], start[1]),
        Jug(goal[2], start[2])
    ]
​
    reached_states, this_level_states = [initial], [initial]
    next_operation_states, performed_operations = [], 0
​
    while target not in reached_states:
        performed_operations += 1
        for state in this_level_states:
            next_operation_states.extend([
                new_state for new_state in perform_pours_on_state(state) if
                new_state not in reached_states
            ])
        reached_states.extend(next_operation_states)
        this_level_states, next_operation_states = next_operation_states, []
        if not this_level_states:
            return "No solution."
    return performed_operations

