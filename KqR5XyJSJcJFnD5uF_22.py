"""


The _median_ of a group of numbers is the _middle_ number when the group is
sorted. If the size of the group is even, the median is the _average_ of the
middle two numbers. Given a sorted list of numbers, return the median (rounded
to one decimal place if the median isn't an integer).

### Examples

    median([1, 2, 4, 5, 6, 8, 8, 8, 10]) ➞ 6
    
    median([2, 2, 6, 8, 8, 10, 10]) ➞ 8
    
    median([1, 2, 2, 4, 7, 8, 9, 10]) ➞ 5.5

### Notes

N/A

"""

def median(nums):
    import math
    if len(nums)%2 != 0:
        index = math.floor(len(nums) / 2)
        return nums[index]
​
    else: 
        index = math.floor(len(nums) / 2)
        index_1 = index - 1
        return round((nums[index] + nums[index_1]) / 2,1)

