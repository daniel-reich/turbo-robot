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

def bell_triangle_row(n):
    if n <= 1: return [1]
    previous = bell_triangle_row(n-1) 
    result, i = [previous[-1]], 1
    while len(result) <= len(previous):
        result.append(result[i-1] + previous[i-1])
        i += 1
    return result
​
def bell(n):
    return bell_triangle_row(n)[-1]

