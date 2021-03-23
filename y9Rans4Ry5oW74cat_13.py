"""


Create a function that accepts a list of numbers and return both the minimum
and maximum numbers, in that order (as a list).

### Examples

    min_max([1, 2, 3, 4, 5]) ➞ [1, 5]
    
    min_max([2334454, 5]) ➞ [5, 2334454]
    
    min_max([1]) ➞ [1, 1]

### Notes

All test lists will have at least one element and are valid.

"""

def min_max(nums):
    nums.sort()
    return [nums[0],nums[-1]]
​
​
def test():
    print("test has started")
    a_list = [14, 35, 6, 1, 34, 54]
    if min_max(a_list) != [1,54]:
        print("error1")
    b_list = [1.346, 1.6532, 1.8734, 1.8723]
    if min_max(b_list) != [1.346, 1.8734]:
        print("error2")

