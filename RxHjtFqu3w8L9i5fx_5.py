"""


The Bell number is the number of ways a list of `n` items can be partitioned
into non-empty sublists. See the resources section for an in-depth
explanation.

Create a function that takes a number `n` and returns the corresponding Bell
number.

### Examples

    bell(1) ➞ 1
    # sample_lst = [1]
    # possible_partitions = [[[1]]]
    
    bell(2) ➞ 2
    # sample_lst = [1, 2]
    # possible_partitions = [[[1, 2]], [[1], [2]]]
    
    bell(3) ➞ 5
    # sample_lst = [1, 2, 3]
    # possible_partitions = [[[1, 2, 3]], [[1, 2], [3]], [[1], [2, 3]], [[1, 3], [2]], [[1], [2], [3]]]

### Notes

N/A

"""

def f(n):
    return 1 if n <1 else n*f(n-1)
def bell(n):
    return n or 1 if n <3 else sum(bell(k)*f(n-1)//(f(k)*f(n-1-k)) for k in range(n))

