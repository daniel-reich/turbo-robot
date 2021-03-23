"""


Given a list of integers, create a function that will find the **smallest**
positive integer that is evenly divisible by all the members of the list. In
other words, find the least common multiple (LCM).

### Examples

    lcm([1, 2, 3, 4, 5, 6, 7, 8, 9]) ➞ 2520
    
    lcm([5]) ➞ 5
    
    lcm([5, 7, 11]) ➞ 385
    
    lcm([5, 7, 11, 35, 55, 77]) ➞ 385

### Notes

N/A

"""

def lcm(nums):
  prod = 1
  while any([n != 1 for n in nums]):
    for i in range(len(nums)):
      for i2 in range(2, nums[i]+1):
        if nums[i]%i2 == 0:
          nums = [n2//i2 if n2%i2 == 0 else n2 for n2 in nums]
          prod *= i2
  return prod

