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
    if start[2]==goal[2]:
        return 0
    if start[2]!=sum(goal):
        return 'No solution.'
    pour=((0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,0,1),(2,1,0))
    q=[[[0,0,start[2]]]];k=0
    while k<10:
        t=[]
        for i in range(len(q[k])):
            for p in pour:
                temp=[0,0,0]
                if q[k][i][p[0]]!=0 and q[k][i][p[1]]!=start[p[1]]:
                    dif=start[p[1]]-q[k][i][p[1]]
                    if dif>=q[k][i][p[0]]:                 
                        temp[p[1]]=q[k][i][p[1]]+q[k][i][p[0]]
                        temp[p[0]]=0
                        temp[p[2]]=q[k][i][p[2]]
                    else:
                        temp[p[1]]=start[p[1]]
                        temp[p[0]]=q[k][i][p[0]]-dif
                        temp[p[2]]=q[k][i][p[2]]
                if temp!=[0,0,0]:
                    t.append(temp)
                    if temp==goal:
                        return k+1
        q.append(t)
        k+=1
    return 'No solution.'

