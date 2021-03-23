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
  return [x for x in nums[0::2] if x%2==0]

