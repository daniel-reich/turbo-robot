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
  def fact(n):
    s=1
    for i in range(1,n+1):
      s=s*i
    return s
  
  def comb(n,k):
    return fact(n)//(fact(k)*fact(n-k))
    
  if n == 1 or n==0: return 1
  return sum(comb(n-1,k-1)*bell(n-k) for k in range(1,n+1))

