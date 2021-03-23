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
  if n <= 1:
    return 1
  parts = [(n, [n])]
  trials = []
  for i in range(1,n//2+1):
    trials.append((i, [i]))
  while len(trials) > 0:
    trial = trials.pop()
    for i in range(trial[0],n-trial[0]+1):
      if sum(trial[1]) + i <= n:
        newTrial = (i,trial[1].copy())
        newTrial[1].append(i)
        if sum(newTrial[1]) == n:
          parts.append(newTrial)
        else:
          trials.append(newTrial)
  return len(parts)
  
  print("testing")
  print(partitions(0))

