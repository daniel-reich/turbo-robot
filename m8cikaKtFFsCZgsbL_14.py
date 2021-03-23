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

from itertools import permutations as pt
​
def waterjug(s, goal):
    comb, lst, gen = list(pt([2, 1, 0],2)), [[[0, 0, s[2]]]], 0; cp ={str(lst[0][0]):0}
    if str(goal) in cp: return gen
    while len(lst[gen]) != 0:
        gen += 1; lst.append([])
        for i in lst[gen-1]:
            for j in comb:
                n = i[:]
                if n[j[0]] == 0: continue
                t= min(s[j[1]] - n[j[1]], n[j[0]]); n[j[1]] += t; n[j[0]] -= t
                if n == goal: return gen
                if str(n) not in cp: cp[str(n)] = gen; lst[gen].append(n)
    return "No solution."

