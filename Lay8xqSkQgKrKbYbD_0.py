"""


A staircase is given with a non-negative cost per each step. Once you pay the
cost, you can either climb one or two steps. Create a solution to find the
minimum sum of costs to reach the top (finishing the payments including
`cost[-2]` or `cost[-1]`). You can either start at `cost[0]` or `cost[1]`.

### Examples

    climbing_stairs([0, 2, 2, 1]) ➞ 2
    
    climbing_stairs([0, 2, 3, 2]) ➞ 3
    
    climbing_stairs([10, 15, 20]) ➞ 15
    
    climbing_stairs([0, 0, 0, 0, 0, 0]) ➞ 0

### Notes

N/A

"""

def climbing_stairs(cost):
  if len(cost)==0:
    return cost[0]
  ans = [0]*len(cost)
  ans[-2:] = cost[-2:]
  for i in range(len(cost)-3, -1,-1):
    ans[i] = cost[i] + min(ans[i+1],ans[i+2])
  
  return min(ans[0:2])

