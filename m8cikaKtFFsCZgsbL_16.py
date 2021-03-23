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
    size = start
    level = 0
    this_level = [[0, 0, start[2]]]
    checked = [start]
    next_level = [[0, 0, start[2]]]
    if next_level[0] == goal:
        return level
    while next_level != []:
        this_level = next_level
        next_level = []
        checked.extend(this_level)
        level += 1
        for group in this_level:
            if group[0] != 0:
                if group[1] != size[1]:
                    if group[0] > (size[1] - group[1]):
                        child = [group[0] - (size[1] - group[1]), size[1], group[2]]
                    else:
                        child = [0, group[0] + group[1], group[2]]
                    if child == goal:
                        return level
                    elif child not in checked:
                        next_level.append(child)
                if group[2] != size[2]:
                    if group[0] > (size[2] - group[2]):
                        child = [group[0] - (size[2] - group[2]), group[1], size[2]]                
                    else:
                        child = [0, group[1], group[0] + group[2]]
                    if child == goal:
                        return level
                    elif child not in checked:
                        next_level.append(child)
            if group[1] != 0:
                if group[0] != size[0]:
                    if group[1] > (size[0] - group[0]):
                        child = [size[0], group[1] - (size[0] - group[0]), group[2]]
                    else:
                        child = [group[0] + group[1], 0, group[2]]
                    if child == goal:
                        return level
                    elif child not in checked:
                        next_level.append(child)
                if group[2] != size[2]:
                    if group[1] > (size[2] - group[2]):
                        child = [group[0], group[1] - (size[2] - group[2]), size[2]]                
                    else:
                        child = [group[0], 0, group[1] + group[2]]
                    if child == goal:
                        return level
                    elif child not in checked:
                        next_level.append(child)
            if group[2] != 0:
                if group[0] != size[0]:
                    if group[2] > (size[0] - group[0]):
                        child = [size[0], group[1], group[2] - (size[0] - group[0])]
                    else:
                        child = [group[0] + group[2], group[1], 0]
                    if child == goal:
                        return level
                    elif child not in checked:
                        next_level.append(child)
                if group[1] != size[1]:
                    if group[2] > (size[1] - group[1]):
                        child = [group[0], size[1], group[2] - (size[1] - group[1])]                
                    else:
                        child = [group[0], group[1] + group[2], 0]
                    if child == goal:
                        return level
                    elif child not in checked:
                        next_level.append(child)       
    return 'No solution.'

