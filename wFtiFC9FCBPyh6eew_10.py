"""
Create a function that determines the number of partitions of a natural
number.

A partition of a number `n` is an unordered sum of one or more numbers which
totals `n`. For example, the partitions of the number 4 are:

    1 + 1 + 1 + 1 = 4
    1 + 1 + 2 = 4
    1 + 3 = 4
    2 + 2 = 4
    4 = 4

Since partitions are unordered, the sums `1 + 1 + 2 = 1 + 2 + 1 = 2 + 1 + 1 =
4` are considered the same partition.

### Examples

    partitions(4) ➞ 5
    
    partitions(10) ➞ 42
    
    partitions(0) ➞ 1
    
    partitions(1) ➞ 1
    
    partitions(2) ➞ 2

### Notes

Remember the trivial partition `n = n`. Also, we say there is one way to
partition zero; namely, `0 = 0`.

"""

def partitions(n, verbose=0):
    if n <= 1:
        return 1
    ctr = 0
    q = [[x] for x in range(n,0,-1)]
    while q:
        x = q.pop(0)
        sum_x = sum(x)
        if sum_x == n:
            ctr += 1
        else:
            for k in range(1, min(n-sum_x, x[-1])+1):
                q.append(x + [k])
    return ctr

