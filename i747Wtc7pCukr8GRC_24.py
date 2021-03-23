"""


Write **two** functions:

  1. One that returns the **maximum product** of three numbers in a list.
  2. One that returns the **minimum product** of three numbers in a list.

### Examples

    max_product([-8, -9, 1, 2, 7]) ➞ 504
    
    max_product([-8, 1, 2, 7, 9]) ➞ 126
    
    min_product([1, -1, 1, 1]) ➞ -1
    
    min_product([-5, -3, -1, 0, 4]) ➞ -15

### Notes

N/A

"""

def max_product(nums):
    nums = sorted(nums)
​
    return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])
​
def min_product(nums):
    nums = sorted(nums)
    
    return min(nums[0]*nums[1]*nums[2], nums[0]*nums[-1]*nums[-2])

