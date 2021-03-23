"""


Given a list of integers, return the _difference_ between the largest and
smallest integers in the list.

### Examples

    difference([10, 15, 20, 2, 10, 6]) ➞ 18
    # 20 - 2 = 18
    
    difference([-3, 4, -9, -1, -2, 15]) ➞ 24
    # 15 - (-9) = 24
    
    difference([4, 17, 12, 2, 10, 2]) ➞ 15

### Notes

N/A

"""

def difference(nums):
  max_nums = max(nums)
  min_nums = min(nums)
  return (max_nums - min_nums)

