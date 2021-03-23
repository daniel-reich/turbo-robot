"""


Given a list of numbers, return a list which contains all the even numbers in
the orginal list, which also have _even indices_.

### Examples

    get_only_evens([1, 3, 2, 6, 4, 8]) ➞ [2, 4]
    
    get_only_evens([0, 1, 2, 3, 4]) ➞ [0, 2, 4]
    
    get_only_evens([1, 2, 3, 4, 5]) ➞ []

### Notes

Lists start at index 0.

"""

def get_only_evens(nums):
  lst = []
  for i in range(len(nums)):
    if i%2 == 0 and nums[i]%2 == 0:
      lst.append(nums[i])
  return lst

