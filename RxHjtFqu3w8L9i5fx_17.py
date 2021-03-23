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
import numpy
import sys
​
def bell(n):
  c = {}
  c[0,0] = 1
  for i in range(1,n):
    c[i,0] = c[i-1,i-1]
    for j in range(1,i+1):
      c[i,j] = c[i-1,j-1]+c[i,j-1]
  return c[n-1,n-1]

