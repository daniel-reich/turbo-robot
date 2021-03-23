"""


Create a function to partition a list from left to right.

### Examples

    moving_partition([-1, -1, -1, -1])
    ➞ [[[-1], [-1, -1, -1]], [[-1, -1], [-1, -1]], [[-1, -1, -1], [-1]]]
    
    moving_partition([1, 2, 3, 4, 5])
    ➞ [[[1], [2, 3, 4, 5]], [[1, 2], [3, 4, 5]], [[1, 2, 3], [4, 5]], [[1, 2, 3, 4], [5]]]
    
    moving_partition([]) ➞ []

### Notes

  * With an `n` input, your output should be a list containing `n-1` sublists. Each sublist should have two elements: the left and the right side of the partition (both should be non-empty, unless the input list is empty).
  * An empty list should return an empty list: `[]`

"""

def moving_partition(lst):
  return [[lst[:i+1], lst[i+1:]] for i in range(len(lst)-1)]

