"""


The function is given a list of numbers where each number appears three times
except for one which appears only one time. Find the single number and return
it.

### Examples

    single_number([2, 2, 3, 2]) ➞ 3
    
    single_number([0, 1, 0, 1, 0, 1, 99]) ➞ 99
    
    single_number([-1, 2, -4, 20, -1, 2, -4, -4, 2, -1]) ➞ 20

### Notes

To run under 12 seconds the function needs to be efficient.

"""

nums = [-1, 2, -4, 20, -1, 2, -4, -4, 2, -1]
def single_number(nums):
    sing = [x for x in set(nums) if nums.count(x)==1]
    return sing[0]
single_number(nums)

