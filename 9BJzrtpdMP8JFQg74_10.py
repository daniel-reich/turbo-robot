"""


Create a function that given a list, it returns the index where if split in
two-subarrays (last element of the first array has index of (foundIndex-1)),
the sum of them are equal.

### Examples

    twins([10, 20, 30, 5, 40, 50, 40, 15]) ➞ 5
    # foundIndex 5 : [10+20+30+5+40]=[50+40+15]
    
    twins([1, 2, 3, 4, 5, 5]) ➞ 4
    # [1, 2, 3, 4] [5, 5]
    
    twins([3, 3]) ➞ 1

### Notes

Return only the foundIndex, not the divided list.

"""

def twins(lst):
  left = 0
  lSum = lst[0]
  right = len(lst) - 1
  rSum = lst[-1]
  while right - left > 0:
    if lSum > rSum:
      right -= 1
      rSum += lst[right]
    elif rSum > lSum:
      left += 1
      lSum += lst[left]
    else:
      right -= 1
      rSum += lst[right]
      left += 1
      lSum += lst[left]
  return left

