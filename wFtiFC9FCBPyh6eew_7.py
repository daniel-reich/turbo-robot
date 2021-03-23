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

def partitions(n):
    partitions = [1]
    pentagonal = lambda x: int(x*(3*x-1) / 2)
    for i in range(1,n+1):
        partitions.append(0)
        for k in range(1,i+1):
            coeff = (-1)**(k+1)
            for t in [pentagonal(k), pentagonal(-k)]:
                if (i-t) >= 0:
                    partitions[i] = partitions[i] + coeff*partitions[i-t]
    return partitions[-1]

