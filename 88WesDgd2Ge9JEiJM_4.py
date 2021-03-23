"""


Find the length of the longest sub-sequence of two distinct numbers whose
difference is `1`. A sub-sequence can be made by deleting any numbers in
between.

### Examples

    almost_uniform([1, 3, 2, 2, 5, 2, 3, 7]) ➞ 5
    # [3, 2, 2, 2, 3]
    
    almost_uniform([1, 2, 3, 4]) ➞ 2
    # [1, 2] or [2, 3] or [3, 4]
    
    almost_uniform([1, 1, 1, 1]) ➞ 0
    # There is no sub-sequence of two distinct numbers.

### Notes

N/A

"""

def almost_uniform(nums):
    max_length = 0
    for i in range(len(nums)):
       if nums[i] - 1 in nums:
            cnt = nums.count(nums[i]) + nums.count(nums[i]-1)
            max_length = max(max_length, cnt)
       if nums[i] + 1 in nums:
            cnt = nums.count(nums[i]) + nums.count(nums[i]+1)
            max_length = max(max_length, cnt)
    return max_length

