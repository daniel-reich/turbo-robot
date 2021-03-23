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
  temp_set = set()
  for i in range(len(nums) - 1):
    if(nums[i] == nums[i + 1]):
      temp_set.add(nums[i])
  unique_multiples = list(temp_set)
  unique_multiples.sort()
  count = [0] * len(unique_multiples)
  for i in range(len(nums)):
    if nums[i] in unique_multiples:
      count[unique_multiples.index(nums[i])] += 1
  max_count = max(count)
  result = []
  for i in range(len(count)):
    if count[i] == max_count:
      result.append(unique_multiples[i])
  return result

