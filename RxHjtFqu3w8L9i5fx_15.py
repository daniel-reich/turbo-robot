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

def bell(n):
  x = [[0 for i in range(n+1)] for j in range(n+1)]
  print(x)
  x[0][0] = 1
  print(x)
  for i in range(1, n+1):
    x[i][0] = x[i-1][i-1]
    for j in range(1,i+1):
      x[i][j] = x[i-1][j-1] + x[i][j-1]
    print(x)
  return x[n][0]

