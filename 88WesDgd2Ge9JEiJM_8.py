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
  count_dict = {}
  for n in nums:
    count_dict[n] = count_dict.get(n, 0) + 1
  sorted_count = sorted(count_dict.items())
  diffs = [sorted_count[i + 1][1] + sorted_count[i][1] for i in range(len(sorted_count) - 1) if sorted_count[i + 1][0] - sorted_count[i][0] == 1]
  return max(diffs) if len(diffs) > 0 else 0

