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

class State:
    def __init__(self, c = [], a = [], h = []):
        self.c = c
        self.a = a
        self.h = h
​
    def __hash__(self):
        h = 0
        for x in range(0, len(self.c)):
            h += hash(self.c[x])
        for x in range(0, len(self.a)):
            h += hash(self.a[x])
        return h
​
    def __eq__(self, other):
        return self.c == other.c and self.a == other.a
​
    def copy(self):
        return State(self.c.copy(), self.a.copy(), self.h.copy())
​
    def __lt__(self, other):
        return len(self.h) < len(other.h)
​
def waterjug(start, goal, printHistory = False):
    amounts = [0, 0, start[2]]
    queue = []
    queue.append(State(start.copy(), amounts.copy()))
    prev = set()
    while len(queue) > 0:
        n = queue.pop()
        if n.a == goal:
            if printHistory:
                print("start:")
                for x in range(0, len(start)):
                    if x != len(start) - 1:
                        print(" 0/{0}".format(start[x]))
                    else:
                        print(" {0}/{0}".format(start[x]))
                for i in range(0, len(n.h)):
                    print(n.h[i])
            return len(n.h)
        for i in range(0, len(n.a)):
            # fill
#            if n.a[i] != n.c[i]:
#                c = n.copy()
#                c.a[i] = c.c[i]
#                if not c in prev:
#                    s = "fill {0}".format(i)
#                    for x in range(0, len(n.a)):
#                        s += " {0}/{1}".format(c.a[x], c.c[x])
#                    c.h.append(s)
#                    queue.append(c)
#                    queue.sort(reverse=True)
#                    prev.add(c.copy())
            # empty
            if n.a[i] > 0:
                c = n.copy()
                c.a[i] = 0
                if not c in prev:
                    s = "empty {0}".format(i)
                    for x in range(0, len(n.a)):
                        s += " {0}/{1}".format(c.a[x], c.c[x])
                    c.h.append(s)
                    queue.append(c)
                    queue.sort(reverse=True)
                    prev.add(c.copy())
            # pour from one to another
            for j in range(0, len(n.a)):
                if i != j:
                    c = n.copy()
                    if c.a[i] + c.a[j] > c.c[j]:
                        c.a[i] -= c.c[j] - c.a[j]
                        c.a[j] = c.c[j]
                    else:
                        c.a[j] += c.a[i]
                        c.a[i] = 0
                    if not c in prev:
                        s = "pour from {0} to {1}".format(i, j)
                        for x in range(0, len(n.a)):
                            s += " {0}/{1}".format(c.a[x], c.c[x])
                        c.h.append(s)
                        queue.append(c)
                        queue.sort(reverse=True)
                        prev.add(c.copy())
    return "No solution."

