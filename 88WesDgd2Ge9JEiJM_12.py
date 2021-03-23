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
  A=[]
  for i in range(len(nums)):
    B=[j for j in range(i+1, len(nums)) if nums[j]==nums[i] or nums[j]==nums[i]+1]
    T=[x for x in nums[i:B[-1]+1] if x==nums[i] or x==nums[i]+1] if B else []
    if T:
      A.append(T)
    C=[j for j in range(i+1, len(nums)) if nums[j]==nums[i] or nums[j]==nums[i]-1]
    S=[x for x in nums[i:C[-1]+1] if x==nums[i] or x==nums[i]-1] if C else []
    if S:
      A.append(S)
  res=[x for x in A if len(set(x))>1]
  return (len(max(res, key=len)) if res else 0) or quit()

