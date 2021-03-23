"""


For each number in a list, check if that number is _greater than_ the _sum_ of
all numbers that appear _before_ it in the list. If _all_ numbers in the list
pass this test, return `True`. Return `False` otherwise.

### Examples

    greater_than_sum([2, 3, 7, 13, 28]) ➞ True
    
    # 3 > 2 = True
    # 7 > 2 + 3 = True
    # 13 > 2 + 3 + 7 = True
    # 28 > 2 + 3 + 7 + 13 = True
    
    greater_than_sum([1, 2, 4, 6, 13]) ➞ False
    
    # 2 > 1 = True
    # 4 > 1 + 2 = True
    # 6 > 1 + 2 + 4 = False
    # 13 > 1 + 2 + 4 + 6 = False

### Notes

The first number in any list will always pass the test.

"""

def greater_than_sum(nums):
  return all(sum(nums[:i])<nums[i] for i in range(len(nums)))

