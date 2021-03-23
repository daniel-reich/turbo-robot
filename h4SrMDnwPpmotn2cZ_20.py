"""


Create a function that takes a list of numbers and returns the sum of its
cubes.

### Examples

    sum_of_cubes([1, 5, 9]) ➞ 855
    # Since 1^3 + 5^3 + 9^3 = 1 + 125 + 729 = 855
    
    sum_of_cubes([3, 4, 5]) ➞ 216
    
    sum_of_cubes([2]) ➞ 8
    
    sum_of_cubes([]) ➞ 0

### Notes

If given an empty list, return `0`.

"""

def sum_of_cubes(nums):
  _sum = 0;
  x = len(nums);
  y = 0;
  while y < x:
    _sum += nums[y] ** 3;
    y += 1
  return _sum

