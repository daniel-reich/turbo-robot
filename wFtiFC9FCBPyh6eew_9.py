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
  c=1 if n<2 else 2
  x=[0 for i in range(n-1)]
  while x:
    sumx=sum(x)
    while n-sumx>=x[0]>0:
      c+=1
      x[0]+=1
      sumx+=1
    for i in range(n-1):
      x[i]+=1
      x=[x[i]+0 for j in range(i)]+x[i:]
      if n-sum(x)>=x[0]>0:break
    if all(x):break
  return c

