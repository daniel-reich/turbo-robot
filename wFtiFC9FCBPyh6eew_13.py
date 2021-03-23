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
  if n == 0:
    return 1
  if n <= 3:
    return n
    
  parts = all_parts([1] * n)
  parts = organize_parts(parts, 0)  
​
  return len(parts)
  
  
  
def organize_parts(parts, i):
  if len(parts) <= 1:
    return parts
  ret = []
  for part in parts:
    if len(part)>1 and isinstance(part[1], list):
      for p in organize_parts(part[1:], i + 1):
        newpart = sorted([part[0]] + p)
        if newpart not in ret:
          ret.append(newpart)
    elif sorted(part) not in ret:
      ret.append(sorted(part))
  return ret
    
  
def all_parts(parts):
  if len(parts) <= 1:
    return parts
  return [[i+1] + all_parts(parts[i+1:]) for i in range(len(parts))]

