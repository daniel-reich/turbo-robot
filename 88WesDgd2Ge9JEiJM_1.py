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

from collections import Counter
def almost_uniform(nums):
  cnt = Counter(nums)
  cnt2 = cnt.copy()
  for x in cnt:
    cnt2[x] += cnt[x-1]
  
  return max([0]+[cnt2[x] for x in cnt if x-1 in cnt])

