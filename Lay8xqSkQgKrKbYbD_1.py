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
    n = len(cost)
    price = [0] * n
    for i in range(2, n):
        price[i] = min(price[i-2] + cost[i-2], price[i-1] + cost[i-1])
    return min(price[-2] + cost[-2], price[-1] + cost[-1])

