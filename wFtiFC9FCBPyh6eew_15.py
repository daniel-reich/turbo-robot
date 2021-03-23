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

def split_into_lists(n):
    if n == 0:
        return [[0]]
    if n == 1:
        return [[1]]
    elif n == 2:
        return [[2], [1, 1]]
    elif n == 3:
        return [[3], [2, 1], [1, 1, 1]]
    else:
        res = [[n]]
        for k in range(n - 1, 0, -1):
            for lst in split_into_lists(n - k):
                tmp_lst = sorted([k] + lst, reverse=True)
                if tmp_lst not in res:
                    res.append(tmp_lst)
        return res
​
​
def partitions(n):
    return len(split_into_lists(n))

