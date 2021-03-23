"""


Given a list of numbers, return the _pair_ of numbers that give the minimum
absolute _difference_. Return the pair as a _list_ , sorted in _ascending_
order. If multiple pairs have the same difference, return the pair with the
smallest sum.

### Examples

    min_difference_pair([40, 16, 8, 17, 15]) ➞ [15, 16]
    # [15, 16] has smaller sum than [16, 17]
    
    min_difference_pair([1, -31, -27, -18, -48, -15, -11, -34]) ➞ [-34, -31]
    
    min_difference_pair([0, 2, 35, 42, 45, 14, -6, -1]) ➞ [-1, 0]
    
    min_difference_pair([32, 33, 4, 6, 48, 18, 20, -7, -4, 31]) ➞ [31, 32]

### Notes

There will be no duplicate numbers in the list.

"""

def min_difference_pair(nums):
  nums.sort()
  minimo=abs(nums[0]-nums[1])
  lista=[nums[0],nums[1]]
  for x in range (len(nums)-1):
    if abs(nums[x]-nums[x+1])<minimo:
      minimo=abs(nums[x]-nums[x+1])
      lista=[nums[x],nums[x+1]]
    elif abs(nums[x]-nums[x+1])==minimo:
      lista=lista+[nums[x],nums[x+1]]
  return lista[:2]

