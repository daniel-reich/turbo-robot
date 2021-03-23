"""


The _mode_ of a group of numbers is the value (or values) that occur most
often (values have to occur more than once). Given a sorted list of numbers,
return a list of all modes in ascending order.

### Examples

    mode([4, 5, 6, 6, 6, 7, 7, 9, 10]) ➞ [6] 
    
    mode([4, 5, 5, 6, 7, 8, 8, 9, 9]) ➞ [5, 8, 9]
    
    mode([1, 2, 2, 3, 6, 6, 7, 9]) ➞ [2, 6] 

### Notes

In this challenge, all group of numbers will have at least one mode.

"""

def mode(nums):
  a = []
  for i in range(1, len(nums)):
    if nums[i] == nums[i-1]:
      a.append(nums[i])
  for i in range(1, len(a)):
    if a[i] != a[i-1]:
      pass
    else: 
      return mode(a)
  return a

