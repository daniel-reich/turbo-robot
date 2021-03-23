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
  if n == 1: return 1
  triangle = [[i]*i for i in range(1,n+1)]
  triangle[1][0] = 1
  for i in range(2,n):
    for j in range(0,i+1):
      if j == 0:
        triangle[i][j] = triangle[i-1][-1]
      else:
        triangle[i][j] = triangle[i-1][j-1] + triangle[i][j-1]
  return triangle[n-1][-1]

