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
    a = sorted(nums)
    pairs = [(a[i],a[i + 1]) for i in range(len(a) - 1) if a[i] == a[i + 1] - 1]
    if not pairs:
        return 0
    return max(nums.count(i[0]) + nums.count(i[1]) for i in pairs)

