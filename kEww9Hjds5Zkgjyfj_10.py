"""


Write a function that replaces each integer with the next largest in the list.

### Examples

    replace_next_largest([5, 7, 3, 2, 8]) ➞ [7, 8, 5, 3, -1]
    
    replace_next_largest([2, 3, 4, 5]) ➞ [3, 4, 5, -1]
    
    replace_next_largest([1, 0, -1, 8, -72]) ➞ [8, 1, 0, -1, -1]

### Notes

  * Replace the maximum with **-1**.
  * Elements in the list will be unique.
  * You don't have to swap the elements.

"""

def replace_next_largest(lst):
    res = []
    for x in lst:
        if x == max(lst):
            res.append(-1)
        else:
            nums = sorted(n for n in lst if n > x)[::-1] + [x]
            idx = nums.index(x)
            res.append(nums[idx - 1])
    return res

