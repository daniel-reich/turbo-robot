"""


Create a function that accepts a list of numbers and return both the minimum
and maximum numbers, in that order (as a list).

### Examples

    min_max([1, 2, 3, 4, 5]) ➞ [1, 5]
    
    min_max([2334454, 5]) ➞ [5, 2334454]
    
    min_max([1]) ➞ [1, 1]

### Notes

All test lists will have at least one element and are valid.

"""

def min_max(nums):
  nums.sort()
  answers = []
  minimum = nums[0]
  maximum = nums[len(nums) - 1]
  answers.append(minimum)
  answers.append(maximum)
  return answers

