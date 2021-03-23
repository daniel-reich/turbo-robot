"""


Write a function that returns the number of ways a person can climb **n
stairs** , where the person may only climb **1** or **2** steps at a time.

To illustrate, if **n = 4** there are **5** ways to climb:

    [1, 1, 1, 1]
    [2, 1, 1]
    [1, 2, 1]
    [1, 1, 2]
    [2, 2]

### Examples

    ways_to_climb(1) ➞ 1
    
    ways_to_climb(2) ➞ 2
    
    ways_to_climb(5) ➞ 8

### Notes

A staircase of height `0` should return `1`.

"""

def ways_to_climb(n):
  from itertools import permutations
  import math
​
  paths = []
  shortest = math.ceil(n/2)
​
  #iterate over different string lengths
  for l in range(shortest,n+1): 
    nums = []
​
    #figure out how many different 2s and 1s I should use for a given length l
    for i in range(n-l):
      nums.append(2)
​
    for i in range(l - len(nums)):
      nums.append(1)
​
    #get permutations. Add if not already in path
    new_paths = list(set([p for p in permutations(nums)]))
    for p in new_paths:
      if p not in paths:
        paths.append(p)
  return len(paths)

