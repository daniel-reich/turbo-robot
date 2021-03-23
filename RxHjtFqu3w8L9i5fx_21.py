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

import math
def binomial(n,k):
  top = math.factorial(n)
  bottom = math.factorial(k)*math.factorial(n-k)
  return top/bottom
def stirling(n,k):
  sum = 0
  for i in range(0,k+1):
    sum+=math.pow(-1,i)*binomial(k,i)*math.pow(k-i,n)
  return 1/math.factorial(k)*sum
def bell(n):
  sum = 0
  for k in range(0,n+1):
    sum+=stirling(n,k)
  return int(sum)

